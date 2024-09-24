import logging
import math
from typing import Callable, Iterator, List, Union, Any
import warnings

from wrike.rest_adapter import RestAdapter
from wrike.exceptions import WrikeException
from wrike.models import *
from wrike.warnings import DataCappedWarning, GreaterThanOneWarning, ZeroWarning

# TODO: Special syntax https://developers.wrike.com/special-syntax/


class Wrike:
    def __init__(
        self,
        hostname: str = "www.wrike.com/api",
        api_key: str = "",
        ver: str = "v4",
        ssl_verify: bool = True,
        logger: logging.Logger = None,
        page_size: int = 1000,
    ):
        self._rest_adapter = RestAdapter(hostname, api_key, ver, ssl_verify, logger)
        self._page_size = page_size

    def _page(
        self, endpoint: str, model: Callable[..., Model], max_amt: int = 1000
    ) -> Iterator[Model]:
        # Init variables
        amt_yielded = 0
        curr_page = 0
        last_page = 0
        ep_params = {"pageSize": self._page_size}

        # Keep fetching pages of tasks until the last page
        while curr_page <= last_page:
            result = self._rest_adapter.get(endpoint=endpoint, ep_params=ep_params)

            # Increment curr_page by 1 and update the last_page based on header info returned
            ep_params["nextPageToken"] = result.next_page_token
            response_size = result.response_size
            if response_size > 0:
                last_page = int(math.ceil(response_size / self._page_size))
            curr_page += 1

            # Yield 1 task from the page; break/end loop if beyond max_amt
            for datum in result.data:
                yield model(**datum)
                amt_yielded += 1
                if amt_yielded >= max_amt:
                    last_page = 0
                    break

    def _models(self, result: Result, model: Callable[..., Model]) -> List[Model]:
        model_list = [model(**datum) for datum in result.data]
        return model_list

    def _one(self, models: [Callable[..., Model]]) -> Model:
        if len(models) > 1:
            warnings.warn(
                f"""More than 1 data value received from the HTTP response, 
                only 1 value expected. Narrow down your search criteria to 
                reduce the returned data values to 1 or use the related 
                function that returns a list.""",
                GreaterThanOneWarning,
            )
        elif len(models) == 0:
            warnings.warn(
                f"""No data values received from the HTTP response, only 1 
                value expected. Check your search criteria for erroes or 
                expand your search criteria to reduce the returned data 
                values to 1 or use the related function that returns a list.""",
                ZeroWarning,
            )
            return None
        outcome = models[0]
        return outcome

    def _add_param(
        self, ed_params: Dict, key: Any, value: Any, expected_type: type
    ) -> None:
        if value:
            if isinstance(value, expected_type):
                ed_params[key] = value
            else:
                raise TypeError(
                    f"Expected type for {key} is {value}, {type(value)} was provided"
                )

    def _create_filter(self, param_dict: Dict, remove_params: List = []) -> Dict:
        optional_params = ["self", "optional_params"] + remove_params
        new_param_dict = param_dict.copy()
        for key, value in param_dict.items():
            if key in optional_params or value is None:
                new_param_dict.pop(key, None)
        if not new_param_dict:
            raise ValueError(
                f"At least one of the required parameters cannot be None.\n{new_param_dict}"
            )
        return new_param_dict

    def _filter(self, param_dict: Dict, model_list: List[Model]) -> List[Model]:
        new_model_list = []
        for model in model_list:
            if param_dict.items() <= model.__dict__.items():
                new_model_list.append(model)
        return new_model_list

    def get_me(self) -> Contact:
        result = self._rest_adapter.get(endpoint="contacts?me")
        contact = self._one(self._models(result, Contact))
        return contact

    def get_tasks(self) -> List[Task]:
        result = self._rest_adapter.get(endpoint="tasks")
        task_list = self._models(result, Task)
        if len(task_list) == 1000:
            warnings.warn(
                f"""Your data may be incomplete! Max of 1000 items per page was 
                returned. If you expect greater than 1000 items to be returned 
                use the related paged function.""",
                DataCappedWarning,
            )
        return task_list

    def get_task(self) -> Task:
        result = self.get_tasks()
        task = self._one(result)
        return task

    def get_tasks_paged(self, max_amt: int = 1000) -> Iterator[Task]:
        return self._page(endpoint="tasks", model=Task, max_amt=max_amt)

    def get_comments(self) -> List[Comment]:
        result = self._rest_adapter.get(endpoint="commments")
        comment_list = self._models(result, Comment)
        return comment_list

    def get_version(self) -> Version:
        result = self._rest_adapter.get(endpoint="version")
        version = self._one(self._models(result, Version))
        return version

    def _get_spaces(
        self,
        expect_one: bool = False,
        id: str = None,
        with_archived: bool = None,
        user_is_member: bool = None,
        fields: List[str] = None,
    ) -> Union[List[Space], Space]:
        ed_params = {}
        endpoint = "spaces"
        if id:
            if isinstance(id, str):
                endpoint += f"/{id}"
            else:
                raise TypeError(f"Expected type for id is str, {type(id)} was provided")
        else:
            self._add_param(ed_params, "withArchived", with_archived, bool)
            self._add_param(ed_params, "userIsMember", user_is_member, bool)
        self._add_param(ed_params, "fields", fields, List[str])
        result = self._rest_adapter.get(endpoint=endpoint, ed_params=ed_params)
        output = self._models(result, Space)
        if expect_one:
            output = self._one(output)
        return output

    def get_spaces(
        self,
        with_archived: bool = None,
        user_is_member: bool = None,
        fields: List[str] = None,
    ) -> Space:
        return self._get_spaces(
            with_archived=with_archived, user_is_member=user_is_member, fields=fields
        )

    def get_space(
        self,
        with_archived: bool = None,
        user_is_member: bool = None,
        fields: List[str] = None,
    ) -> Space:
        return self._get_spaces(
            expect_one=True,
            with_archived=with_archived,
            user_is_member=user_is_member,
            fields=fields,
        )

    def get_space_by_id(self, id: str, fields: List[str] = None) -> Space:
        return self._get_spaces(expect_one=True, id=id, fields=fields)

    def get_space_and_filter(
        self,
        title: str = None,
        avatar_url: str = None,
        access_type: AccessType = None,
        guest_role_id: str = None,
        default_project_workflow_id: str = None,
        default_task_workflow_id: str = None,
        description: str = None,
        with_archived: Optional[bool] = None,
        user_is_member: Optional[bool] = None,
        fields: Optional[List[str]] = None,
    ) -> Space:
        optional_params = ["with_archived", "user_is_member", "fields"]
        param_dict = self._create_filter(
            param_dict=locals(), remove_params=optional_params
        )
        space_list = self._get_spaces(
            with_archived=with_archived, user_is_member=user_is_member, fields=fields
        )
        return self._filter(param_dict=param_dict, model_list=space_list)
