from __init__ import *
from user import Users

class Event(DynamicDocument):
	name = StringField()
	description = StringField()

class userTickets(DynamicDocument):
	user = ReferenceField(Users)
	event = ReferenceField(Event)