import json

from loguru import logger

from loopr.exceptions import LooprInternalServerError, LooprInvalidResourceError


def response_handler(input_function):
    def call_function(*args, **kwargs):
        try:
            response = input_function(*args, **kwargs)
            if response.status_code >= 500:
                raise LooprInternalServerError(error_message="Internal server error")
            elif response.status_code >= 400:
                res = json.loads(response.text)["errors"][0]
                raise LooprInvalidResourceError(
                    error_message=res["error"], reason=res["message"]
                )
            elif response.status_code >= 200:
                return json.loads(response.text)
        except Exception as e:
            logger.error(e)
            raise e

    return call_function
