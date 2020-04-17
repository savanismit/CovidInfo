from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import datetime

app = Flask(__name__) 

@app.route('/', ,methods=['GET','POST'])
def test():
	return ("Hello!")

if __name__ == '__main__':
	app.run(debug=True)