from home.views import home_bp
from property.views import property_bp
from applying.views import applyling_bp
from home import app

app.register_blueprint(home_bp)
app.register_blueprint(property_bp)
app.register_blueprint(applying_bp)

app.run('localhost', 5555)