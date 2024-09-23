from json import JSONDecodeError
import logging
import requests
import requests.packages
from typing import List, Dict

from wrike.models import Result
from wrike.exceptions import WrikeException


class RestAdapter:
    def __init__(
        self,
        hostname: str = "www.wrike.com/api",
        api_key: str = "",
        ver: str = "v4",
        ssl_verify: bool = True,
        logger: logging.Logger = None,
    ):
        """Constructor for RestAdapter

        Args:
            hostname (str, optional): base url. Defaults to "www.wrike.com/api".
            api_key (str, optional): string used for authentication. Defaults to "".
            ver (str, optional): always v4. Defaults to "v4".
            ssl_verify (bool, optional): Normally set to True,
                but if having SSL/TLS cert validation issues, can turn off with False.
                Defaults to True.
            logger (logging.Logger, optional): If your app has a logger, pass it in here.
                Defaults to None.
        """
        self._logger = logger or logging.getLogger(__name__)
        self.url = "https://{}/{}/".format(hostname, ver)
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            # noinspection PyUnresolvedReferences
            requests.packages.urllib3.disable_warnings()

    def _do(
        self, http_method: str, endpoint: str, ep_params: Dict = None, data: Dict = None
    ) -> Result:
        """Private method for get(), post(), delete(), etc. methods

        Args:
            http_method (str): GET, POST, DELETE, etc.
            endpoint (str): URL Endpoint as a string
            ep_params (Dict, optional): Dictionary of Endpoint parameters. Defaults to None.
            data (Dict, optional): Dictionary of data to pass to Wrike. Defaults to None.

        Raises:
            WrikeException: Request failed
            WrikeException: Unable to deseralize JSON
            WrikeException: Successful status code not returned

        Returns:
            Result: a Result object
        """
        full_url = self.url + endpoint
        headers = {"Authorization": "bearer " + self._api_key}
        log_line_pre = f"method={http_method}, url={full_url}, params={ep_params}"
        log_line_post = ", ".join(
            (log_line_pre, "success={}, status_code={}, message={}")
        )

        # Log HTTP params and perform an HTTP request, catching and re-raising any exceptions
        try:
            self._logger.debug(msg=log_line_pre)
            response = requests.request(
                method=http_method,
                url=full_url,
                verify=self._ssl_verify,
                headers=headers,
                params=ep_params,
                json=data,
            )
        except requests.exceptions.RequestException as e:
            self._logger.error(msg=(str(e)))
            raise WrikeException("Request failed") from e

        # Deserialize JSON output to Python object, or return failed Result on exception
        try:
            data_out = response.json()
        except (TypeError, JSONDecodeError) as e:
            self._logger.error(msg=log_line_post.format(False, None, e))
            raise WrikeException("Bad JSON in response") from e

        # If status_code in 200-299 range, return success Result with data, otherwise raise exception
        is_success = 299 >= response.status_code >= 200  # 200 to 299 is OK
        # NOTE: log_line_post has resulted in errors in the past
        log_line = log_line_post.format(
            is_success, response.status_code, response.reason
        )
        if is_success:
            self._logger.debug(msg=log_line)
            return Result(
                response.status_code,
                response.headers,
                message=response.reason,
                data=data_out,
            )
        self._logger.error(msg=log_line)
        raise WrikeException(f"{response.status_code}: {response.reason}")

    def get(self, endpoint: str, ep_params: Dict = None) -> Result:
        """Query - HTTP GET setup for Wrike

        Args:
            endpoint (str): URL Endpoint as a string
            ep_params (Dict, optional): Dictionary of Endpoint parameters. Defaults to None.

        Returns:
            Result: a Result object
        """
        return self._do(http_method="GET", endpoint=endpoint, ep_params=ep_params)

    def post(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        """Create - HTTP POST setup for Wrike

        Args:
            endpoint (str): URL Endpoint as a string
            ep_params (Dict, optional): Dictionary of Endpoint parameters. Defaults to None.
            data (Dict, optional): Dictionary of data to pass to Wrike. Defaults to None.

        Returns:
            Result: a Result object
        """
        return self._do(
            http_method="POST", endpoint=endpoint, ep_params=ep_params, data=data
        )

    def put(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        """Modify - HTTP PUT setup for Wrike

        Args:
            endpoint (str): URL Endpoint as a string
            ep_params (Dict, optional): Dictionary of Endpoint parameters. Defaults to None.
            data (Dict, optional): Dictionary of data to pass to Wrike. Defaults to None.

        Returns:
            Result: a Result object
        """
        return self._do(
            http_method="PUT", endpoint=endpoint, ep_params=ep_params, data=data
        )

    def delete(
        self, endpoint: str, ep_params: Dict = None, data: Dict = None
    ) -> Result:
        """Delete - HTTP DELETE setup for Wrike

        Args:
            endpoint (str): URL Endpoint as a string
            ep_params (Dict, optional): Dictionary of Endpoint parameters. Defaults to None.
            data (Dict, optional): Dictionary of data to pass to Wrike. Defaults to None.

        Returns:
            Result: a Result object
        """
        return self._do(
            http_method="DELETE", endpoint=endpoint, ep_params=ep_params, data=data
        )
