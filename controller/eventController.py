from __init__ import *
from models import user,event
from flask import request,abort
from flask_restful import Resource
from auth import auth

class eventController(Resource):	
	def get(self):
		events = event.Event.objects()
		data=[]
		for e in events:
			data.append({"id":str(e.id),"name":e.name,"description":e.description})
		return data

	@auth.login_required
	def post(self):
		name = request.json.get('name')
		description = request.json.get('description')

		if name is not None and description is not None:
			me = event.Event()
			me.name = name
			me.description = description
			me.save()
			return {"Response":"Event sucessfully added"}	