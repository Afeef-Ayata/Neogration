import sys
from flask import Blueprint

from project.models import NeoScript, NeoWork

job = Blueprint('job', __name__)

@job.route('/trigger/<string:workId>', methods = ['POST','GET'])
def runWork(workId):

    try: 
        # Get the NeoWork by id
        work = NeoWork.objects(pk=workId)[0]
        # make sure the api credentials have permission to work on provided workId
    
        # fetch all the scipts first
        # execute only after that.
        
        allScritps = []
        # for scriptId in work.neoScriptsList:
        for scriptId in work.neoScriptsList:
            neoScript = NeoScript.objects(pk=scriptId).first()
            # append the fetched script to the array of allScript
            allScritps.append(str(neoScript.script))
        print('just fetched all the scripts from mongoDb')
        
        for index,s in enumerate(allScritps):
            print(f'executing script index : {index}')
            exec(s)
        print('the execution of all script is completed')

        return 'Completed the Work'
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")

        error = str(sys.exc_info()[0])
        return f"Oh! some error occured {error}",500