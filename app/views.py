from flask import render_template
#from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder import ModelView
from app import appbuilder, db
from flask_appbuilder import AppBuilder, expose, BaseView, has_access
from flask_appbuilder.models.sqla.filters import FilterEqualFunction, FilterContains

from flask import render_template, flash
from flask_appbuilder import SimpleFormView
from flask_babel import lazy_gettext as _
from .forms import MyForm
from .models import NomeCustom
from app import appbuilder, db

from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from flask_login import current_user
"""
	Create your Views::


	class MyModelView(ModelView):
		datamodel = SQLAInterface(MyModel)


	Next, register your Views::


	appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

"""
	Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()




class HomeView(BaseView):
	route_base = "/home"

	@expose('/user/')
	def user(self):
		greeting = "Hello John"
		return self.render_template('logged_user.html', greeting=greeting)


	@ expose('/general/')
	def general(self):
		greeting = "Hello ordinary user"
		return self.render_template('logged_user.html', greeting=greeting)
'''

class MyView(BaseView):

	default_view = 'method1'

	@expose('/method1/')
	@has_access
	def method1(self):
		# do something with param1
		# and return to previous page or index
		return self.render_template('my_index_auth.html')

	@expose('/method2/<string:param1>')
	@has_access
	def method2(self, param1):
		# do something with param1
		# and render template with param
		param1 = 'Goodbye %s' % (param1)
		return param1


	@expose('/method3/<string:param1>')
	@has_access
	def method3(self, param1):
		# do something with param1
		# and render template with param
		param1 = 'Goodbye %s' % (param1)
		self.update_redirect()
		return self.render_template('method3.html',
							   param1 = param1)
'''
class MyModelView(ModelView):
	datamodel = SQLAInterface(NomeCustom)
	label_columns = {'nome':'NOME', 'my_custom':'COGNOME'}
	list_columns = ['nome', 'my_custom']
	#base_filters = [['nome', FilterContains, 'bbb']]
	edit_columns = ['nome', 'cognome']
	add_columns = ['nome', 'cognome']
'''
class MyFormView(SimpleFormView):
	form = MyForm
	form_title = 'This is my first form view'
	message = 'My form was submitted'

	def form_get(self, form):
		form.field1.data = 'This was prefilled'

	def form_post(self, form):
		# post process form
		flash(self.message, 'info')
'''
appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
'''
appbuilder.add_view(MyFormView, "My form View", icon="fa-key", label=_('My form View'), category="My Forms", category_icon="fa-cogs")
appbuilder.add_view(MyView, "Method1", category='My View')
appbuilder.add_separator("My View")
appbuilder.add_link("Method2", href='/myview/method2/john', category='My View')
appbuilder.add_link("Method3", href='/myview/method3/john', category='My View1')
appbuilder.add_link("google", href="http://www.google.com", icon = "fa-google-plus")
'''
appbuilder.add_view_no_menu(HomeView())
