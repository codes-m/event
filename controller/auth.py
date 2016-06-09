from __init__ import *
from flask_httpauth import HTTPBasicAuth
from flask import g
from models import user

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(email,password):
	me = user.Users.objects(email=email).first()
	if me is not None:
		if me.verify_password(password,me.password):
			g.user = me
			return True
		else:
			return False
	
	else:
		return False