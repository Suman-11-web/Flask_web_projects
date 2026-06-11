from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
	return "<h1>welcome to first flask website</h1>"
	
if __name__=='__main__':
	app.run(debug=True, port=5500)