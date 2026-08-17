from flask import Flask

app = Flask(__name__)


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


@app.route("/")
def home():
    return """
    <h1>Python CI/CD Pipeline</h1>
    <p>Application is running successfully!</p>
    <p>CI/CD Pipeline: Active</p>
"""


@app.route("/add/<int:a>/<int:b>")
def add_numbers(a, b):
    return f"Result: {add(a, b)}"


@app.route("/multiply/<int:a>/<int:b>")
def multiply_numbers(a, b):
    return f"Result: {multiply(a, b)}"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)