from flask import Flask
from flask import render_template
from flask import url_for
app=Flask(__name__)
@app.route("/")
def hello():
    return render_template("richardo.html")
@app.route("/About_me")
def hello2():
    return render_template("About_me.html")
if __name__=="__main__":
    app.debug=True
    app.run()
