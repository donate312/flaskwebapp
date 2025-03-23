from app import create_app, db
from models import Booking

app = create_app()
app.app_context().push()
db.create_all()

print("Datbase created successfully!")

Booking.query.all()    