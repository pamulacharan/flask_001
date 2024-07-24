
from flask import *
app = Flask(__name__)


@app.route('/login', methods=['GET'])
def login():
    uname = request.args.get('uname')
    password = request.args.get('password')
    if uname == "charan" and password == "chandu":
        return " Welcome %s" % uname
    else:
        return "oooooooooooooo Invalid User name and password %s" % uname

# Flask, url_for, redirect, render_template, request
#


if  __name__ == '__main__':
    app.run(debug=True)
