from flask import g, url_for, redirect
from flask_appbuilder import IndexView, expose

class MyIndexView(IndexView):
	@expose('/')
	def index(self):
		user = g.user
		if user.is_anonymous():
			return redirect(url_for('AuthDBView.login'))
		else:
			if user.first_name == 'John':
				return redirect(url_for('HomeView.user'))
			else:
				#return redirect(url_for('HomeView.general'))
				return redirect('/mymodelview/list/')
'''				
	class MyIndexView(IndexView):
	index_template = 'my_index.html'
'''