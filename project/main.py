import json
from flask import Blueprint, render_template
from flask_login import current_user, login_required
from project.editor import getScriptById

from project.models import NeoWork

main = Blueprint('main', __name__)
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html',name = current_user.name)

@main.route('/success')
def success():
    return render_template('success.html', name = current_user.name)

@main.route('/run-work/<string:workId>', methods = ['GET'])
@login_required
def runWork(workId):
    # Get the NeoWork by id 
    work = NeoWork.objects(pk=workId)[0]
    # make sure the current user have permission to work on provided workId
    authenticated = work.author == str(current_user.id)
    if not authenticated:
        return json.dumps({"status":401,"message":'Ho sorry you dont have permission to access this neowork'}),401
    
    try:
        for index,scriptId in enumerate(work.neoScriptsList):
            print(f'fetching neoScript with id {scriptId}, index : {index}')
            neoScript = getScriptById(scriptId)
            print(f'about to execute the neoScript {scriptId}')
            exec(neoScript.script)
            print(f'neoScript with id {scriptId} is executed')

        return json.dumps({"status":200,"message":'Executed all scripts successfully'}),200
    except:
        print('Some error occured')
        return json.dumps({"status":500,"message":'Executing script failed'}),500

