from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
    
from home import views