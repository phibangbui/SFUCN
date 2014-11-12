from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Main Page'

@app.route('/hello')
def index():
	return 'Login Page'

@app.route('/signup')
def signup():
	return 'Signup Page'

@app.route('/courses')
def courses():
	return 'Courses Page'


if __name__ == '__main__':
	app.run()


