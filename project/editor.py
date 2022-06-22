from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from project.models import NeoScript
from dotenv import dotenv_values

config = dotenv_values(".env")

editor = Blueprint('editor', __name__)

@editor.route('/editor')
@login_required
def index():
    return render_template('editor.html')

@editor.route('/editor', methods=['POST'])
@login_required
def create_new_script():
    name = request.form.get('name')

    new_script = NeoScript(
        name = name,
        description = request.form.get('description'),
        author = current_user.name,
        script = request.form.get('scriptarea'),
    )

    new_script.save()

    flash(f"Your script {name} is saved into mongodb")
    
    return redirect(url_for('main.success'))

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