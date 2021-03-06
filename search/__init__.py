from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from search.config import Config
from flask_docs import ApiDoc


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
doc = ApiDoc(app)



from search import routes, models

