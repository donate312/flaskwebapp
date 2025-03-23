from flask_login import UserMixin
from extensions import db



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(150), nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    appointment_date = db.Column(db.Date)
    appointment_time = db.Column(db.Time)
    service = db.Column(db.String(50))
    special_requests = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
