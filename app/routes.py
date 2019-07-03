import requests
from flask import redirect
from flask import url_for


from app import app

@app.route('/')
@app.route('/index')
def index():
	return '''
<html>
	<head>
		<title>GummyTest</title>
	</head>
	<body>
		<a href=/hello><input type=”button” value=”call_flask_function”></a>
	</body>
</html>'''


payload = {"text":"Hello, World!"}
r = requests.post('https://hooks.slack.com/services/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', json=payload)

@app.route('/hello')
def hello(): 
	requests.post('https://hooks.slack.com/services/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', json=payload)
	return redirect(url_for('index')) 
