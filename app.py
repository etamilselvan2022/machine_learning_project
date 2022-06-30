from flask import Flask


app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "Love u Prema.\n I miss u too.\n Don't forget to had ur breakfast and lunch.\n Take care of urself.\n Bye!..."

if __name__=="__main__":
    app.run(debug=True)    