from flask import Flask, render_template, request
from werkzeug import secure_filename
import tensorflow as tf
import shutil

model = load_model("../Invasive Species Detector")

app = Flask(__name__)

def getName(speciesID):
    return "";

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

      shutil.move(f.filename,"../static/images/"+f.filename.ToString())

      predictions = model.predict(f)

      invasive = True;  #This will control which page to go to
      speciesID = 0; # other numbers for other species

      speciesName = "";

      if invasive:
          return render_template("invasive.html", name = f.filename, speciesName=getName(speciesID))
      else:
          return render_template("notinvasive.html", name = f.filename)

@app.route("/invasive")
def invasive():
    return render_template("invasive.html")

@app.route("/notinvasive")
def notinvasive():
    return render_template("notinvasive")

if __name__ == "__main__":
    app.run(debug=True)
