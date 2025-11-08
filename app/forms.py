from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, FormField, FieldList, SubmitField, SelectField
from wtforms.validators import DataRequired, Optional

class AuthConfigForm(FlaskForm):
    enabled = BooleanField('Use usermanagement?', validators=[Optional()])
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
    color = SelectField(
        'Farbe', 
        choices=[('amber', 'Amber'),
                 ('blue', 'Blau'),
                 ('cyan', 'Cyan'),
                 ('emerald', 'Emeraude'),
                 ('fuchsia', 'Fuchsia'),
                 ('gray', 'Grau'),
                 ('green', 'Grün'),
                 ('indigo', 'Indigo'),
                 ('lime', 'Limette'),
                 ('neutral', 'Neutral'),
                 ('orange', 'Orange'),
                 ('pink', 'Rosa'),
                 ('purple', 'Lila'),
                 ('red', 'Rot'),
                 ('rose', 'Rosen'),
                 ('sky', 'Himmel'),
                 ('slate', 'Schiefer'),
                 ('stone', 'Stein'),
                 ('teal', 'Teal'),
                 ('violet', 'Violett'),
                 ('yellow', 'Gelb'),
                 ('zinc', 'Zink')
                 ],
        validators=[Optional()])

class ConfigForm(FlaskForm):
    primary = StringField('Primary', validators=[DataRequired()])
    secondary = StringField('Secondary', validators=[DataRequired()])
    accent = StringField('Accent', validators=[DataRequired()])
    dark = StringField('Dark', validators=[DataRequired()])
    bright = StringField('Bright', validators=[DataRequired()])
    success = StringField('Success', validators=[DataRequired()])
    warn = StringField('Warn', validators=[DataRequired()])
    error = StringField('Error', validators=[DataRequired()])
    font = StringField('Font', validators=[Optional()])
    font_provider = StringField('Font Provider', validators=[Optional()])
    institution_name = StringField('Institution Name', validators=[DataRequired()])
    institution_web = StringField('Institution Website', validators=[DataRequired()])
    auth = FormField(AuthConfigForm)
    topics = FieldList(FormField(TopicForm), min_entries=1)
    submit = SubmitField('Generate Config')
