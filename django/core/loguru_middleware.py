import logging
import sys

from loguru import logger

from django.core.handlers.asgi import ASGIRequest
from django.core.handlers.wsgi import WSGIRequest


logger.remove(0)
logger.add(sys.stderr, colorize=True, format="<b><green>{time}</green> <level>{level}</level> <blue>{message}</blue></b>")

class DjangoLoguruMiddleware:
    """
    Logs all the requests and responses from the application
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest):
        """
        Code to be executed on every request/response call.
        """
        print("-" * 50)
        print(type(request))
        print(request)
        print(type(request.method))
        print(request.method)
        print("-" * 50)
        logger.info(f"URL: {request.build_absolute_uri()}")
        logger.info(f"Method: {request.method}")


        response = self.get_response(request)
        logger.info(f"Status Code: {response.status_code}")

        return response


class LoguruHandler(logging.Handler):

    def __init__(self, level = 0, *args, **kwargs) -> None:
        print(args, kwargs)
        print(super().get_name())
        super().__init__(level)

    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = sys._getframe(6), 6
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())
