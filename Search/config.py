import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'sdfgFRSGE$34gg53'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'base.db')
    JSON_AS_ASCII = False
    API_DOC_MEMBER = ['api', 'plaatform']
    RESTFUL_API_DOC_EXCLUDE = []
