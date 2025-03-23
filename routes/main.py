from flask import Blueprint,render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime
from models import Booking
from extensions import db

main = Blueprint('main', __name__)

@main.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        date_str = request.form.get('date')
        time_str = request.form.get('time')
        service = request.form.get('service')

        # Convert date and time strings into Python date/time objects
        appointment_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        appointment_time = datetime.strptime(time_str, '%H:%M').time()

        new_booking = Booking(
            name=name,
            email=email,
            phone=phone,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            service=service
        )

        db.session.add(new_booking)
        db.session.commit()

        flash('Your appointment has been booked successfully!', 'success')
        return redirect(url_for('main.booking'))

    return render_template('booking.html')

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/profile')
@login_required
def profile():
    return f"Welcome, {current_user.name}!"
