from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, from paas practical session"

if __name__ == "__main__":
    app.run()