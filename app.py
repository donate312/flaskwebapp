from flask import Flask
from extensions import db
from flask_login import LoginManager, current_user
from flask_migrate import Migrate
from flask_mail import Mail

mail = Mail()

def create_app():

    app = Flask(__name__, static_folder='static')
#   app.config['SECRET_KEY'] = os.enviorn.get('SECRET_KEY', 'default-secret-key')
    app.config['SECRET_KEY'] = '1626'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'david83152@gmail.com'
    app.config['MAIL_PASSWORD'] = 'zxbl mwku katr lnje'  # Use app-specific password

    mail.init_app(app)

    db.init_app(app)
    migrate = Migrate(app, db)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth_login'

    from models import Booking
    from models import User
    
    @app.context_processor
    def inject_user():
        return dict(user=current_user)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from routes.auth import auth
    from routes.main import main

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(main, url_prefix='/')

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
