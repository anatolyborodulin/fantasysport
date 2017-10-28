from flask import Flask, render_template, request

my_flask_app = Flask(__name__)

@my_flask_app.route('/')
def index():
	return render_template('index.html')

@my_flask_app.route('/main/')
def news():
	return render_template('index.html')

@my_flask_app.route('/games/')
def leagues():
	return render_template('games.html')

@my_flask_app.route('/players/')
def ranking():
	return render_template('players.html')

@my_flask_app.route('/rules/')
def rules_game():
	return render_template('rules.html')

@my_flask_app.route('/login/', methods=['POST'])
def login():
	return render_template('login.html', email=request.form.get('email'), password=request.form.get('passwrd'))

@my_flask_app.route('/addteam/')
def addteam():
	return render_template('addteam.html')

if __name__ =='__main__':
	my_flask_app.run(port=5015, debug=True)
	
