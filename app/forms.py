from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, FormField, FieldList, SubmitField, SelectField
from wtforms.validators import DataRequired, Optional

class AuthConfigForm(FlaskForm):
    enabled = BooleanField('Usermanagement verwenden?', validators=[Optional()])
    google = BooleanField('Google', validators=[Optional()])
    apple = BooleanField('Apple', validators=[Optional()])
    github = BooleanField('GitHub', validators=[Optional()])
    keycloak = BooleanField('Keycloak', validators=[Optional()])
    microsoft = BooleanField('Microsoft', validators=[Optional()])
    discord = BooleanField('Discord', validators=[Optional()])
    facebook = BooleanField('Facebook', validators=[Optional()])
    # Weitere Felder für andere Provider nach Bedarf

class TopicForm(FlaskForm):
    topic = StringField('Name', validators=[Optional()])
    color = SelectField('Farbe', choices=[
        ('amber'),
        ('blue'),
        ('cyan'),
        ('emerald'),
        ('fuchsia'),
        ('gray'),
        ('green'),
        ('indigo'),
        ('lime'),
        ('neutral'),
        ('orange'),
        ('pink'),
        ('purple'),
        ('red'),
        ('rose'),
        ('sky'),
        ('slate'),
        ('stone'),
        ('teal'),
        ('violet'),
        ('yellow'),
        ('zinc'),
    ], validators=[Optional()])

class ConfigForm(FlaskForm):
    primary = StringField('Primary', validators=[DataRequired()])
    secondary = StringField('Secondary', validators=[DataRequired()])
    accent = StringField('Accent', validators=[DataRequired()])
    dark = StringField('Dark', validators=[DataRequired()])
    bright = StringField('Bright', validators=[DataRequired()])
    success = StringField('Success', validators=[DataRequired()])
    warn = StringField('Warn', validators=[DataRequired()])
    error = StringField('Error', validators=[DataRequired()])
    font = StringField('Schriftart', validators=[Optional()])
    font_provider = StringField('Font Provider', validators=[Optional()])
    institution_name = StringField('Institution Name', validators=[DataRequired()])
    institution_web = StringField('Institution Webseite', validators=[DataRequired()])
    auth = FormField(AuthConfigForm)
    topics = FieldList(FormField(TopicForm), min_entries=1)
    submit = SubmitField('Konfiguration generieren')
