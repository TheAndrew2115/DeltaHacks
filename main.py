from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/scanner")
def scanner():
    return render_template("about.html")

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      print("success")
      print(f.filename)

      invasive = True;  #This will control which page to go to

      return 'file uploaded successfully'

@app.route("/invasive")
def invasive():
    return render_template("invasive.html")

@app.route("/notinvasive")
def notinvasive():
    return render_template("notinvasive")

if __name__ == "__main__":
    app.run(debug=True)
