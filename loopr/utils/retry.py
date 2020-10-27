import time

from loguru import logger


def retry(exception, max_tries=3, backoff_factor=0.2):
    def retry_decorator(wrapped_func):
        def func_with_retries(*args, **kwargs):
            _try = 0
            _delay = 0
            while _try < max_tries:
                logger.info("executing request...")
                try:
                    return wrapped_func(*args, **kwargs)
                except exception as e:
                    _delay = backoff_factor * ((2 ** _try) - 1)
                    _try += 1
                    logger.info(f"request failed, retrying attempt: {_try}")
                    time.sleep(_delay)
                    if _try == max_tries:
                        raise e

        return func_with_retries

    return retry_decorator
