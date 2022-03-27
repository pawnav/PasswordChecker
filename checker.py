from flask import Flask
from flask import request
from flask import render_template
from password_api import PasswordChecker

app = Flask(__name__)

pwd_checker = PasswordChecker()


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pwd = request.form.get('pass')
        if pwd is not None:
            count = pwd_checker.pwnd_api_check(password=pwd)
            count = int(count)
            if count is not None:
                return render_template('strength.html', count=count)

    return render_template('form.html')



