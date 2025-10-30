import sys
from src.logger import logger

def error_message_deatails(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error Occur in python script name [{0}] line number [{1}] error message [{2}]".format(filename,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_deatails(error_message,error_details=error_details)

        logger.error(self.error_message)

    def __str__(self):
        return self.error_message



# if __name__ == "__main__":
#     try:
#         a = 10/0
        
#     except Exception as e:
#         raise CustomException(e,sys)
    

