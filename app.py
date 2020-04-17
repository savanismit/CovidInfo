from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import requests,json

app = Flask(__name__) 

@app.route("/")
def hello():
    return "Hello world!"

@app.route('/bot',methods=['GET','POST'])
def test():
    incoming_msg = request.form.get('Body')
    resp = MessagingResponse()
    responded = False
    inmsg = incoming_msg.lower()

    if 'hi' in inmsg or 'hy' in inmsg or 'menu' in inmsg : 
        text = f'🙋🏻‍♂️ ```Hello``` 🙋🏻‍♂️\nThis is a Covid-Gideon-Bot to provide latest information updates i.e cases in different countries and create awareness to help you and your family stay safe.\n\n 👇For any emergency 👇 \n☎️ Helpline :- 011-23978046 \n📩 Email :- ncov2019@gov.in\n\nPlease enter one of the following option 📝\n *A*. Covid-19 statistics *Worldwide*.\n *B*. Covid-19 status for any *Country*.\n *C*. Symptoms of *Covid19*\n *D*. How does it *Spread?*\n *E*. *Preventive steps* to be taken.'
        msg = resp.message(text)
        responded = True
        
    if 'a' in inmsg:
        r = requests.get('https://covidgideon.herokuapp.com/all')
        if r.status_code == 200:
            data = r.json()
            text = f'```Covid-19 Cases Worldwide``` \n\nNew Cases : *{data["new_cases"]}* \n\nTotal Cases : *{data["total_cases"]}* \n\nRecovered : *{data["recovered"]}* \n\nTotal Deaths : *{data["deaths"]}* \n\n 👉 Type *B, C, D, E* to see other options \n 👉 Type *Menu* to go to the Main Menu'
        else:
            text = 'I could not find the result, Please Try Again!'
        msg = resp.message(text)
        responded = True
    
    if 'b' in inmsg:
        msg1 = resp.message("Enter country name:-")
        
        responded = True

    if 'F' in incoming_msg:
        text = f'```Coronavirus spreads from an infected person through``` 👇 \n\n ✅ Small droplets from the nose or mouth which are spread when a person coughs or sneezes \n\n ✅ Touching an object or surface with these droplets on it and then touching your mouth, nose, or eyes before washing your hands \n \n ✅ Close personal contact, such as touching or shaking hands \nPlease watch the video for more information \n👉 https://youtu.be/0MgNgcwcKzE \n\n👉 Type *Menu* to go to the Main Menu'
        msg = resp.message(text)
        msg.media('https://user-images.githubusercontent.com/34777376/77290801-f2421280-6d02-11ea-8b08-fdb516af3d5a.jpeg')
        responded = True
    
    if 'G' in incoming_msg:
        text = f'```Coronavirus infection can be prevented through the following means``` 👇 \n ✔️ Clean hand with soap and water or alcohol-based hand rub \n\n ✔️ Cover nose and mouth when coughing & sneezing with a tissue or flexed elbow \n\n ✔️ Avoid close contact & maintain 1-meter distance with anyone who is coughing or sneezin \n\n ✔️ Isolation of persons traveling from affected countries or places for at least 14 day \n\n 👉 Type *Menu* to go to the Main Menu'
        msg = resp.message(text)
        msg.media('https://user-images.githubusercontent.com/34777376/77290864-1c93d000-6d03-11ea-96fe-18298535d125.jpeg')
        responded = True

    if responded == False:
        msg = resp.message('Input is Invalid, sorry!')
    return(str(resp))

if __name__ == '__main__':
	app.run(debug=True)