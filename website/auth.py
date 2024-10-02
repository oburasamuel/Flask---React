from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<P>Login</p>"

@auth.route('/logout')
def logout():
      return "<P>Logout</p>"

@auth.route('/sign-up')
def sign_up():
     return "<p>Sign-up</p>"