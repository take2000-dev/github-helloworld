from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Cloud Shell Editor!'

if __name__ == '__main__':
    app.run()
