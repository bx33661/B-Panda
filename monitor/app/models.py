from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Website(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), unique=True, nullable=False)
    monitor_data = db.relationship('MonitorData', backref='website', lazy=True)

class MonitorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    status_code = db.Column(db.String(50), nullable=False)
    response_time = db.Column(db.Float, nullable=True)
    website_id = db.Column(db.Integer, db.ForeignKey('website.id'), nullable=False)