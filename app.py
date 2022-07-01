from logging import exception
from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception('we are testing custom exception')
    except Exception as e:
        housing=HousingException(e,sys) 
        logging.info(housing.error_message)   
        logging.info('we are testing logging module')
    return "Love u Prema.\n I miss u too.\n Don't forget to had ur breakfast and lunch.\n Take care of urself.\n Bye!..."

if __name__=="__main__":
    app.run(debug=True)    