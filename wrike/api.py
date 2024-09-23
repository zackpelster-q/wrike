import logging
import math
from typing import Callable, Iterator, List
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

    def _one(self, result: Result, model: Callable[..., Model]) -> Model:
        if len(result.data) > 1:
            warnings.warn(
                f"""More than 1 data value received from the HTTP response, 
                only 1 value expected. Narrow down your search criteria to 
                reduce the returned data values to 1 or use the related 
                function that returns a list. {result.data}""",
                GreaterThanOneWarning,
            )
        elif len(result.data) == 0:
            warnings.warn(
                f"""No data values received from the HTTP response, only 1 
                value expected. Check your search criteria for erroes or 
                expand your search criteria to reduce the returned data 
                values to 1 or use the related function that returns a list. 
                {result.data}""",
                ZeroWarning,
            )
            return None
        outcome = model(**result.data[0])
        return outcome

    def get_me(self) -> Contact:
        result = self._rest_adapter.get(endpoint="contacts?me")
        contact = self._one(result, Contact)
        return contact

    def get_tasks(self) -> List[Task]:
        result = self._rest_adapter.get(endpoint="tasks")
        task_list = [Task(**datum) for datum in result.data]
        if len(task_list) == 1000:
            warnings.warn(
                f"""Your data may be incomplete! Max of 1000 items per page was 
                returned. If you expect greater than 1000 items to be returned 
                use the related paged function.""",
                DataCappedWarning,
            )
        return task_list

    def get_task(self) -> Task:
        result = self._rest_adapter.get(endpoint="tasks")
        task = self._one(result, Task)
        return task

    def get_tasks_paged(self, max_amt: int = 1000) -> Iterator[Task]:
        return self._page(endpoint="tasks", model=Task, max_amt=max_amt)

    def get_comments(self) -> List[Comment]:
        result = self._rest_adapter.get(endpoint="commments")
        comment_list = [Comment(**datum) for datum in result.data]
        return comment_list

    def get_version(self) -> Version:
        result = self._rest_adapter.get(endpoint="version")
        version = self._one(result, Version)
        return version
