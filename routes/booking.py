from flask import Blueprint, render_template, request, flash, redirect, url_for
from models import Booking
from . import db, mail
from flask_login import login_required, current_user
from flask_mail import Message

booking = Blueprint('booking', __name__)

@booking.route('/book', methods=['GET', 'POST'])
@login_required
def book():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        service = request.form.get('service')
        date_time = request.form.get('date_time')
        #barber = request.form.get('barber')
        special_requests = request.form.get('special_requests')

        # Validate input
        if not name or not email or not phone or not service or not date_time:
            flash('All fields are required!', category='error')
            return redirect(url_for('booking.book'))

        # Save booking to the database
        new_booking = Booking(
            name=name,
            email=email,
            phone=phone,
            service=service,
            date_time=date_time,
            special_requests=special_requests,
            user_id=current_user.id
        )
        db.session.add(new_booking)
        db.session.commit()
    msg = Message(
    subject="Appointment Confirmation - Salah's Salon",
    sender='your_email@gmail.com',
    recipients=[email],
    body=f'''Hi {name},

    Thanks for booking a {service} on {date_time}.

    We look forward to seeing you!

    – Salah's Salon Team
    '''
    )
    try:
        mail.send(msg)
        flash('Appointment booked and confirmation email sent!', category='success')
    except Exception as e:
        print(e)
    flash('Appointment booked, but email could not be sent.', category='warning')

    return redirect(url_for('views.home'))

    return render_template('booking.html', user=current_user)
