from flask import request,abort,g
from flask_restful import Resource
#Imports user.py file from models folder
from models import user
#Global Variable
from auth import *

class userController(Resource):

	@auth.login_required
	def get(self):
		me = g.user
		#return {"Name":me.name,"Email":me.email,"Password":me.password,"Events":str(me.events)}
		return {"Name":me.name,"Email":me.email,"Events":me.events,"Events Counter":str(me.counter)}
	def post(self):
		# import pdb;pdb.set_trace()
	 	name = request.json.get('name')
	 	email = request.json.get('email')
	 	password = request.json.get('password')	
	 	events = request.json.get('events')

	 	if name is not None and email is not None and password is not None and events is not None:
	 		me = user.Users()
	 		me.name = name
	 		me.email = email	 		
	 		me.encrypt_password(password)
	 		me.save()
	 		return 	{"response":"Sucess","id":str(me.id)}
	 	else :
	 		abort(400)
