# config.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///monitoring.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)  # 用于 session 的加密
