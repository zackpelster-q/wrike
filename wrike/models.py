from datetime import datetime
from enum import Enum
from requests.structures import CaseInsensitiveDict
from typing import Dict, List, Optional, TypeVar
import warnings

from wrike.exceptions import KindException, WrikeException

Model = TypeVar("Model", covariant=True)


class TypeEnum(Enum):
    BACKLOG = "Backlog"
    MILESTONE = "Milestone"
    PLANNED = "Planned"


class Importance(Enum):
    HIGH = "High"
    LOW = "Low"
    NORMAL = "Normal"


class Scope(Enum):
    WS_TASK = "WsTask"
    RB_TASK = "RbTask"


class Status(Enum):
    ACTIVE = "Active"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"
    DEFERRED = "Deferred"


class Dates:
    type: TypeEnum
    duration: Optional[int]
    start: Optional[datetime]
    due: Optional[datetime]
    work_on_weekends: Optional[bool]

    def __init__(
        self,
        type: TypeEnum,
        duration: Optional[int],
        start: Optional[datetime],
        due: Optional[datetime],
        work_on_weekends: Optional[bool],
    ) -> None:
        self.type = type
        self.duration = duration
        self.start = start
        self.due = due
        self.work_on_weekends = work_on_weekends


class Result:
    status_code: int
    headers: CaseInsensitiveDict
    message: str
    kind: str
    state: str
    next_page_token: str
    response_size: int
    data: List[Dict]
    _response_data: Dict
    _data: List[Dict]

    def __init__(
        self,
        status_code: int,
        headers: CaseInsensitiveDict,
        message: str = "",
        data: Dict = None,
    ):
        """Result returned from low-level RestAdapter

        Args:
            status_code (int): Standard HTTP Status code
            message (str, optional): Human readable result. Defaults to ''.
            data (Dict, optional): Python Dictionary. Defaults to None.
        """
        self.status_code = int(status_code)
        self.headers = headers
        self.message = str(message)
        self._response_data = data if data else {}
        self._parse_data(**self._response_data)

    def _parse_data(
        self,
        kind: str = "",
        state: str = "",
        nextPageToken: str = "",
        responseSize: int = 0,
        data: List[Dict] = None,
        **kwargs,
    ):
        """Parses the data from the response, split into the Wrike model of
            kind, state, and data

        Args:
            kind (str, optional): The entity type. Defaults to ''.
            state (str, optional): Client can pass an additional state parameter. Defaults to ''.
            nextPageToken (str, optional): The returned pagination token.
                Returned in response if page size was provided. Defaults to ''.
            responseSize (int, optional): Total number of responses available.
                Divide by your page size to get the number of pages.
                Returned in response if page size was provided. Defaults to 0.
            data (List[Dict], optional): Python List of Dictionaries. Defaults to None.
        """
        self.kind = str(kind)
        self.state = str(state)
        self.next_page_token = str(nextPageToken)
        self.response_size = int(responseSize)
        self._data = data if data else []
        self.data = [
            {
                "kind": self.kind,
                "state": self.state,
                "next_page_token": self.next_page_token,
                "response_size": self.response_size,
            }
            | d
            for d in self._data
        ]
        self.__dict__.update(kwargs)


class Method:
    kind: str
    state: str
    next_page_token: str
    response_size: int
    _expected_kind: str

    def __init__(
        self,
        expected_kind: str = "",
        kind: str = "",
        state: str = "",
        next_page_token: str = "",
        response_size: int = 0,
        **kwargs,
    ):
        """Base class for Wrike based method classes that confirms the response kind matches
            the expected kind, and passes along state

        Args:
            expected_kind (str, optional): The expected entity type. Defaults to ''.
            kind (str, optional): The entity type. Defaults to ''.
            state (str, optional): Client can pass an additional state parameter. Defaults to ''.
            next_page_token (str, optional): The returned pagination token.
                Returned in response if page size was provided. Defaults to ''.
            response_size (int, optional): Total number of responses available.
                Divide by your page size to get the number of pages.
                Returned in response if page size was provided. Defaults to 0.
        """
        self._expected_kind = expected_kind
        self.kind = kind
        self.state = state
        self.next_page_token = next_page_token
        self.response_size = response_size
        if self._expected_kind != self.kind:
            warnings.warn(
                f"Response kind ({self.kind}) does not match expected kind ({self._expected_kind})",
                KindWarning,
            )


class Version(Method):
    major: str
    minor: str

    def __init__(
        self,
        major: int,
        minor: int,
        **kwargs,
    ):
        """API version info

        Args:
            major (int): Major version number
            minor (int): Minor version number
        """
        super().__init__("version", **kwargs)
        self.major = major
        self.minor = minor
        self.__dict__.update(kwargs)


class Comment(Method):
    id: str
    author_id: str
    text: str
    updated_date: datetime
    created_date: datetime
    task_id: Optional[str]
    folder_id: Optional[str]

    def __init__(
        self,
        id: str,
        author_id: str,
        text: str,
        updated_date: datetime,
        created_date: datetime,
        task_id: Optional[str],
        folder_id: Optional[str],
        **kwargs,
    ) -> None:
        """Comments

        Args:
            id (str): Comment ID
            author_id (str): Author ID
            text (str): Comment text
            updated_date (datetime): Deprecated because this field gets created date instead of updated date.
                Please use the createdDate field instead.
            created_date (datetime): Created date
            task_id (Optional[str]): ID of related task. Only one of taskId/folderId fields is present
            folder_id (Optional[str]): ID of related folder. Only one of taskId/folderId fields is present
        """
        super().__init__("comments", **kwargs)
        self.id = id
        self.author_id = author_id
        self.text = text
        self.updated_date = updated_date
        self.created_date = created_date
        self.task_id = task_id
        self.folder_id = folder_id
        self.__dict__.update(kwargs)


class Task(Method):
    id: str
    account_id: Optional[str]
    title: str
    status: Status
    importance: Importance
    created_date: Optional[datetime]
    updated_date: Optional[datetime]
    completed_date: Optional[datetime]
    dates: Dates
    scope: Scope
    custom_status_id: Optional[str]
    permalink: str
    priority: str

    def __init__(
        self,
        id: str,
        title: str,
        status: Status,
        importance: Importance,
        dates: Dates,
        scope: Scope,
        permalink: str,
        priority: str,
        account_id: str = "",
        created_date: datetime = None,
        updated_date: datetime = None,
        completed_date: datetime = None,
        custom_status_id: str = "",
        **kwargs,
    ) -> None:
        super().__init__("tasks", **kwargs)
        self.id = id
        self.account_id = account_id
        self.title = title
        self.status = status
        self.importance = importance
        self.created_date = created_date
        self.updated_date = updated_date
        self.completed_date = completed_date
        self.dates = dates
        self.scope = scope
        self.custom_status_id = custom_status_id
        self.permalink = permalink
        self.priority = priority
        self.__dict__.update(kwargs)


class Dependency(Method):
    def __init__(
        self,
        id: str,
        predecessor_id: str,
        successor_id: str,
        relation_type: str,
        lag_time: int,
        **kwargs,
    ):
        super().__init__("version", **kwargs)
        self.id = id
        self.predecessor_id = predecessor_id
        self.successor_id = successor_id
        self.relation_type = relation_type
        self.lag_time = lag_time
        self.__dict__.update(kwargs)
