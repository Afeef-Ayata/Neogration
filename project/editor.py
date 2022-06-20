from flask import Blueprint, render_template
from flask_login import login_required
from .mongoDb import get_database

editor = Blueprint('editor', __name__)

@editor.route('/editor')
@login_required
def index():
    db = get_database('IntegrationDb')

    dbCollection = db['Scipts']
    
    item_details = dbCollection.find()
    for item in item_details:
        print(item)

    return render_template('editor.html')
