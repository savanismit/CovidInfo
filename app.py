from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import datetime

app = Flask(__name__) 

@app.route('/',methods=['GET','POST'])
def test():
    num = request.form.get("From")
    num = num.replace("whatsapp:","")
    msg = request.form.get("Body")

    resp = MessagingResponse()
    msg = resp.message("Hey,Good Morning!") 
    
    return(str(resp))

if __name__ == '__main__':
	app.run(debug=True)