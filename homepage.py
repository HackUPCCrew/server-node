from flask import render_template
from config import app, mongo

@app.route("/")
def hello():
    return render_template('homepage.html')

@app.route("/generate")
def updateData():
    # mock
    return "Data successfully imported!"

if __name__ == "__main__":
    app.run()