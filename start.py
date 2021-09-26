from flask import Flask

app = Flask(__name__)
from app import routers

if __name__ == '__main__':
    app.run('127.0.0.1', 7000)
