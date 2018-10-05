from flask import Flask, request, redirect, render_template
import cgi
import os
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def display_signup_form():
    return render_template('signup.html')

def is_valid(string):
    if len(string) < 3 or len(string) > 20:
        return False
    else:
        return True

def is_email(string):
    
    #valid_email = re.compile('[a-zA-Z0-9_]+\.?[a-zA-Z0-9_]+@[a-z]+\.[a-z]+')
    #if valid_email.match(string):

    if (string.count('@') == 1) and (string.count('.') == 1):
        return True
    else:
        return False
        
@app.route('/', methods=['POST'])
def validate_signup():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if (not username) or (not is_valid(username)) or (' ' in username):
        username_error = 'That is not a valid username'
    
    if (not password) or (not is_valid(password)) or (' ' in password):
        password_error = 'That is not a valid password'

    if (verify_password != password) or (not verify_password):
        verify_password_error = 'Passwords do not match'

    if email:
        if (not is_valid(email)) or (' ' in email) or (not is_email(email)):
            email_error = 'That is not a valid email'

    if (not username_error) and (not password_error) and (not verify_password_error) and (not email_error):
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup.html', username=username, email=email, username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error)

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    
    return '<h1>Welcome, {0}!</h1>'.format(username)

app.run()