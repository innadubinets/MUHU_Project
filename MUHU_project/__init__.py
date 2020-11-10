from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    with app.app_context():
        from .home import home
        from .property import property
        from .applying import applying
        from .users import users

        app.register_blueprint(home.home_bp)
        app.register_blueprint(applying.applying_bp)
        app.register_blueprint(property.property_bp)
        app.register_blueprint(users.users_bp)

        return app

    