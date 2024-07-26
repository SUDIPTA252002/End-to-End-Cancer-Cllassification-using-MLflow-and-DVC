import sys


def get_error_info(err, err_detail: sys):
    _, _, exc_tb = err_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in py script name [{0}] line number [{1}] message [{2}]".format(
        filename, exc_tb.tb_lineno, str(err)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, err_detail):
        super().__init__(error_message)
        self.error_message = get_error_info(error_message, err_detail=err_detail)

    def __str__(self):
        return self.error_message
