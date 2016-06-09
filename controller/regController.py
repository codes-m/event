from __init__ import *
from models import user,event
from flask import request,abort,g
from flask_restful import Resource
from auth import auth

class regController(Resource):
	@auth.login_required
	def get(self):
		goingEvent = event.userTickets.objects(user=g.user)
		data=[]
		for e in goingEvent:
			data.append({"Event Name":e.event.name,"Event Description":e.event.description})

		return data

	@auth.login_required
	def post(self):
		me = g.user
		id_event = request.json.get('id')
		event_interested = event.userTickets()
		event_interested.user = me
		event_interested.event = event.Event(id=id_event)
		event_interested.save()
		return {"Response":"Sucess"}	