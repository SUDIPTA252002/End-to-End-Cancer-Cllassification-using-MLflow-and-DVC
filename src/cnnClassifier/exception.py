import sys

def get_error_info(err,err_detail:sys):
    _,_,exc_tb=err_detail.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in py script name [{0}] line number [{1}] message [{2}]".format(filename,exc_tb.tb_lineno,str(err))
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail):
        super().__init__(error_message)
        self.error_message=get_error_info(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message