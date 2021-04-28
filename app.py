from flask import Flask
from flask_restful import Api, Resource
# import os
# from flask import send_from_directory


app = Flask(__name__)
api = Api(app)

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return 'Welcome to flask-learn'

###
# Hello Endpoint
###
class Hello(Resource):
    def get(self):
        return {"msg": "hello"}

api.add_resource(Hello, '/hello')

###
# Hello Endpoint with name
###
class HelloName(Resource):
    def get(self, name):
        return {"msg": "hello " + name}

api.add_resource(HelloName, '/hello/<string:name>')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')