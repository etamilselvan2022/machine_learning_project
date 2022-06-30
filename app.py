from flask import Flask


app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "Love u Prema.I miss u too.Don't forget to had ur breakfast and lunch.Take care of urself.Bye!..."

if __name__=="__main__":
    app.run(debug=True)    