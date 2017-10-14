from flask import Flask, render_template, request

my_flask_app = Flask(__name__)

@my_flask_app.route('/')
def index():
	return render_template('index.html')

@my_flask_app.route('/news/')
def news():
	return render_template('all_the_news.html')

@my_flask_app.route('/leagues/')
def leagues():
	return render_template('khl_league.html')

@my_flask_app.route('/ranking/')
def ranking():
	return render_template('top_ranking.html')

@my_flask_app.route('/rules/')
def rules_game():
	return render_template('how_to_play.html')

@my_flask_app.route('/login/', methods=['POST'])
def login():
	return render_template('login.html', email=request.form.get('email'), password=request.form.get('passwrd'))

if __name__ =='__main__':
	my_flask_app.run(port=5015, debug=True)