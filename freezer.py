#pip install Frozen-Flask
from flask_frozen import  Freezer
from app import app

freezer = Freezer(app)
if __name__ =='main':
    freezer.freeze()