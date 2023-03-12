from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
  return render_template("home.html")

@app.route("/studlogin/")
def studlogin_page():
  return render_template("studlogin.html")

  app = Flask(__name__)
  
@app.route("/")
def lecturelogin_page():
  return render_template("lecturlogin.html")
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

@app.route("/admilogin/")
def admilogin_page():
  return render_template("admilogin.html")
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  