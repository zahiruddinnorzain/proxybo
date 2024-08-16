from flask import Flask, request
import requests
app = Flask(__name__)

@app.route("/")
def home():
    
    url = request.args.get("url")
    target_url = url
    response = requests.get(target_url, params=request.args)
    output = response.content
    output = output.decode('utf-8')
    return output

if __name__ == '__main__':
	app.run(port=8000, debug=True, host='0.0.0.0')