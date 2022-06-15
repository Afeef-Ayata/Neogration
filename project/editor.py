from flask import Blueprint, render_template

editor = Blueprint('editor', __name__)

@editor.route('/editor')
def index():
    return render_template('editor.html')
