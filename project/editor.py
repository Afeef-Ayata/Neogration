from flask import Blueprint, render_template
from flask_login import login_required
from .mongoDb import get_database

from project.models import NeoScript
from dotenv import dotenv_values

config = dotenv_values(".env")

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

@editor.route("/create")
def add_new_script():
    new_user = NeoScript(
        name = "name",
        description = "description",
        author = "author",
        script = "script",
    )
    new_user.save()
    return str(new_user.id)

@editor.route("/list")
def get_all_scripts():
    return str(NeoScript.objects.to_json())
    return str([i.name for i in NeoScript.objects])