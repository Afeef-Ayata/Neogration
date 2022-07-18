import json
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from project.models import NeoScript, NeoWork
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
        author = str(current_user.id),
        script = request.form.get('scriptarea'),
    )

    new_script.save()

    flash(f"Your script {name} is saved into mongodb")
    
    return redirect(url_for('main.success'))

@login_required
def my_neoscripts():
    return {'myscripts':json.loads(NeoScript.objects(author=str(current_user.id)).order_by('-date').to_json())}

@login_required
def my_neoworks():
    return {'myworks':json.loads(NeoWork.objects(author=str(current_user.id)).order_by('-date').to_json())}

@editor.route("/create-new-work", methods=['POST'])
@login_required
def create_new_work():
    name = request.form.get('name')

    new_work = NeoWork(
        name = name,
        description = request.form.get('description'),
        author = str(current_user.id),
        neoScriptsList = [],
    )

    new_work.save()

    flash(f"Your Work {name} is saved")
    
    return redirect(url_for('main.success'))

@editor.route('/neoworks/<string:work_id>', methods = ['GET','PUT'])
@login_required
def workeditor(work_id):
    # Get the NeoWork by id 
    work = NeoWork.objects(pk=work_id)[0]
    # make sure the current user have permission to work on provided workId
    isAuthenticated = work.author == str(current_user.id)
    if not isAuthenticated:
        return json.dumps({"status":401,"message":'Ho sorry you dont have permission to access this neowork'}),401

    if request.method == 'PUT':
        jsonData = request.json
        result = work.update(neoScriptsList=jsonData['neoScriptIds'])
        return str(result)
    else :
        return render_template('work_editor.html', work_id = work_id)