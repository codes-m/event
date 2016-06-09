from __init__ import *
from passlib.apps import custom_app_context as pwd_context

class Users(DynamicDocument):
	name = StringField()
	email = StringField(unique=True)
	password = StringField()
	events = ListField()
	counter = IntField()
	def encrypt_password(self,password):
		self.password=pwd_context.encrypt(password)

	@staticmethod
	def verify_password(password,encrypted_password):
		return pwd_context.verify(password,encrypted_password)

	