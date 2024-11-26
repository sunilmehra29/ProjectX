from flask import Flask

app = Flask(__name__)

@app.route('/<int:value>')
def home(value):
    square = value * value
    return f"Hey the square of {value} is {square}"


if __name__ == '__main__':
    app.run()
