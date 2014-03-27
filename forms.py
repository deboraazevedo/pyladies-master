from flask_wtf import Form
from wtforms import TextField, TextAreaField

class SerieForm(Form):
	name = TextField('Name')
	description = TextAreaField('Description')
	image = TextField('Image URL')
	
