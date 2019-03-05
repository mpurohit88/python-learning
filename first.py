from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template('first.html', name='mukesh')
    else:
        return render_template('first.html', name='mukesh')