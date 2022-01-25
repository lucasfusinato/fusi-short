import logging

custom_error_logger = logging.Logger('custom_error')

class CustomError(Exception):
    def __init__(self, original_error: Exception, message: str = None, *args):
        super().__init__(message, *args)
        custom_error_logger.exception(original_error)

    def get_message(self) -> str:
        raise NotImplementedError

class GenericError(CustomError):
    def get_message(self) -> str:
        return 'Sorry, but we got some problem when trying execute request'

class ClientError(CustomError):
    def __init__(self, message: str, original_error: Exception, *args):
        super().__init__(message=message, original_error=original_error, *args)
        self.__message = message
        
    def get_message(self) -> str:
        return self.__message