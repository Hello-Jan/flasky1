from flask import render_template
from . import main


@main.app_errorhandler(404) #handling error uses 'errorhandler'
def page_not_found(e):#what is it meaning of 'e'?if not e,this function will be useless.
	return render_template('404.html'),404#return has two parameters.

@main.app_errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500