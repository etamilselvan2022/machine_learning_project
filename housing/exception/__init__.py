from cmath import e
import os
import sys

class HousingException(Exception):

    def  __init__(self,error_message:Exception,error_detail:sys):
        super().__init__(error_message)
        self.error_message=HousingException.get_detailed_error_message(error_message=error_message,
                                                                       error_detail=error_detail)


    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:
        '''
        error_message:exception object
        error_details:object of sys module
        '''
        _ ,_ , exec_tb=error_detail.exc_info()
        exception_block_line_no=exec_tb.tb_frame.f_lineno
        try_block_line_no=exec_tb.tb_lineno
        file_name=exec_tb.tb_frame.f_code.co_filename
        error_message=f"""Error Occured in Script:[{file_name}] 
                      at exception block line number:[{exception_block_line_no}] 
                      and try block line number:[{try_block_line_no}] 
                      and error_message is {error_message}"""
        return error_message        



        def __str__(self):
            return self.error_message


        def __repr__(self) ->str:
            return HousingException.__name__.str()    