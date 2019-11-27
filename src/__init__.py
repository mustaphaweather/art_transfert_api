from flask import Flask

## initiate flask app
app = Flask(__name__)

## define sample route
@app.route('/')
def welcome():
    return 'welcom to art torch'

if __name__ == '__main__':
    app.run()
