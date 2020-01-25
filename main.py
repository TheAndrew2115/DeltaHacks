from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Add shit please"

if __name__ == "__main__":
    app.run(debug=True)