import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xdd\x95rJ\xf8\r\x90<\xbb?b\xd6\x0es4C'

    MONGODB_SETTINGS = {'db' : 'Schedule_Planner'
    # 'hosts' : 'mongodb://localhost:27017/Schedule_Planner',

    }