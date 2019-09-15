from datetime import datetime
from flask import render_template,session,redirect,url_for,flash,current_app
from . import main,auth
from .forms import NameForm
from .. import db
from ..models import User
from ..email import send_email






@main.route('/',methods=['POST','GET'])
def index():
	form=NameForm()
	if form.validate_on_submit():#? input name and press submit.It point to an action
		old_name=session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('looks like you have changed your name!')
		session['name']=form.name.data
		user=User.query.filter_by(username=form.name.data).first()
		if user is not None:
			session['known']=True
		else:
			session['known']=False
			user=User(username=form.name.data)
			db.session.add(user)
			db.session.commit()
			if current_app.config['FLASKY_ADMIN']:
				send_email(current_app.config['FLASKY_ADMIN'],'New user','mail/new_user',user=user)


		return redirect(url_for('.index'))#.index is the short of main.index main is the name of its blueprint.
	return render_template('index.html',form=form,name=session.get('name'),known=session.get('known',False)) 
