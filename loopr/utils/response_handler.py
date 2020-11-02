import json

from loguru import logger

from loopr.exceptions import (
    LooprAuthorizationError,
    LooprInternalServerError,
    LooprInvalidResourceError,
)


def response_handler(input_function):
    def call_function(*args, **kwargs):
        try:
            response = input_function(*args, **kwargs)
            logger.debug(response.text)
            if response.status_code >= 500:
                raise LooprInternalServerError(error_message="Internal server error")
            elif response.status_code == 401:
                raise LooprAuthorizationError(error_message="User is Unauthorized")
            elif response.status_code >= 400:
                res = json.loads(response.text)["errors"][0]
                raise LooprInvalidResourceError(
                    error_message=res["error"], reason=res.get("message", None)
                )
            elif response.status_code >= 200:
                return json.loads(response.text)
        except Exception as e:
            logger.error(e)
            raise e

    return call_function
