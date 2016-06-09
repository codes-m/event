from flask import Flask
from flask_restful import Api
from models import connector,user,event
from controller import userController,eventController,regController

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'Hello'

api.add_resource(userController.userController,'/user')
api.add_resource(eventController.eventController,'/event')
api.add_resource(regController.regController,'/register')

if __name__ == '__main__' :
	app.run(debug=True)
