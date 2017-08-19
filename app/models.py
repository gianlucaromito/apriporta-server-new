from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship
from flask_appbuilder.models.decorators import renders
from flask import Markup, url_for
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
from flask_appbuilder.actions import action

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who

"""
		
class NomeCustom(AuditMixin, Model):
	id = Column(Integer, primary_key=True)
	nome = Column(String(50), unique = True, nullable=False)
	cognome = Column(String(20))

	@action("myaction","Do something on this record","Do you really want to?","fa-rocket")
	def myaction(self, item):
		"""
			do something with the item record
		"""
		pass
		return redirect(self.get_redirect())

	@renders('cognome')
	def my_custom(self):
	# will render this columns as bold on ListWidget
		return Markup('<button type="button" class="btn btn-primary btn-block">' + self.cognome + '</button>')