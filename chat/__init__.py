import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

#Flask app configurations
app = Flask(__name__)
app.static_folder = 'static'
#Database configurations
app.config['SECRET_KEY'] = '0ca5e3a1c2dc3391f9a2bb9c54a532a3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
#Login configurations
login_manager = LoginManager(app)
login_manager.login_view = 'admin_login'
#Email configurations
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'gatewaychatbot@gmail.com'
app.config['MAIL_PASSWORD'] = 'nayan@123'
mail = Mail(app)

from chat import routes
