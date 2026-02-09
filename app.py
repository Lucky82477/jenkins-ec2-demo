from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Jenkins Pipeline is WORKING on EC2 sucessfully to new web page 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
