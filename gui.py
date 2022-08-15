from flask import Flask

#initialize the flask app
app = Flask(__name__)

#default route
@app.route('/')
def index():
    return 'Hello World'



if __name__ == '__main__':
    #run app in debug mode on port 5000
    app.run(debug=True, port=5000)
