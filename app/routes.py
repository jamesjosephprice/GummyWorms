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
		<a href=/yes><input type=”button” value=”There are Gummy Worms”></a>
		<a href=/no><input type="button" value="There are NO Gummy Worms"></a>
	</body>
</html>'''


payload1 = {"text":"Yes Test"})
payload2 = {"text":"No Test"}

@app.route('/yes')
def yes(): 
	requests.post('https://hooks.slack.com/services/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', json=payload1)
	return redirect(url_for('index')) 

@app.route('/no')
def no(): 
	requests.post('https://hooks.slack.com/services/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', json=payload2)
	return redirect(url_for('index')) 
