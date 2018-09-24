from flask import render_template, Blueprint,abort
from simpledu.models import Course,User

user = Blueprint("user",__name__,url_prefix="/user")

@user.route('/<username>')
def index(username):
    users = User.query.all()
    user_name = [user.username for user in users]
    if username not in user_name:
        abort(404)
    return render_template("user.html",username=username,users=users)


