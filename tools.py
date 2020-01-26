import functools
import logging
from flask import make_response

logger = logging.getLogger(__file__)


def auth_token_wapper(token):
    def _handler(func):
        @functools.wraps(func)
        def wrapper(request, *args, **kwargs):
            http_token = request.META.get('HTTP_TOKEN')
            logger.info(http_token)
            if not http_token:
                return make_response('403: HTTP_TOKEN is invalid')
            else:
                if token != http_token:
                    return make_response('403: HTTP_TOKEN is invalid')
            return func(request, *args, **kwargs)
        return wrapper
    return _handler
