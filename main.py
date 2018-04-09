from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def validate_info():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    error1 = ''
    error2 = ''
    error3 = ''
    error4 = ''
    


    if len(username) < 3 or len(username) > 20 or username == '':
        error1 = "Invalid user name.  Please enter a username between 3-20 characters and no spaces."
        username = username
    else:
        username = username

    if len(password) < 3 or len(password) > 20 or password == '' or ' ' in password:
        error3 = "Invalid Password.  Please enter a password that is between 3-20 characters and no spaces."

    if  verify != password or   verify == '':
        error4 = "The passwords did not match.  Please re-enter."
    
    if email != '':
        if '@' not in email or '.' not in email:
            error2 = "Invalid email address.  Please re-enter"
            email = email
        else:
            email = email
    
    if not error1 and not error2 and not error3 and not error4:
        return render_template('welcome.html', username = username)
    else:
        return render_template('login.html',error1=error1,
            error2=error2,error3=error3,error4=error4,
            username=username,email=email)


@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()