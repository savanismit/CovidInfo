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

    if 'hiiii' in inmsg or 'hyyy' in inmsg or 'hi' == inmsg or 'hy' == inmsg or 'hey' == inmsg or 'hyy' == inmsg or 'hyyy' == inmsg or 'hii' == inmsg or 'hiii' == inmsg or 'hiiii' == inmsg or 'hye' == inmsg or 'hyee' == inmsg or 'menu' == inmsg : 
        text = f'🙋🏻‍♂️ ```Hello``` 🙋🏻‍♂️\nThis is a Covid-Gideon-Bot developed by _Smit Savani_ to provide latest information updates i.e cases in different countries and create awareness to help you and your family stay safe.\n\n 👇For any emergency 👇 \n☎️ Helpline :- 011-23978046 \n📩 Email :- ncov2019@gov.in\n\nPlease enter one of the following option 📝\n *A*. Covid-19 statistics *Worldwide*.\n *B*. Symptoms of *Covid19*\n *C*. How to stop *Spreading?*\n *D*. *Do\'s* and *Don\'ts*. \n\n*Enter country name to get status of Covid19 for that country:-*'
        msg = resp.message(text)
        msg.media('https://i.ibb.co/r6c8SMn/intro.jpg')
        responded = True
    #Worldwide    
    if 'a' == inmsg:
        r = requests.get('https://covidgideon.herokuapp.com/all')
        if r.status_code == 200:
            data = r.json()
            text = f'```Covid-19 Cases Worldwide 🌎```\n\nNew Cases : *{data["new_cases"]}* \n\nTotal Cases : *{data["total_cases"]}* \n\nRecovered : *{data["recovered"]}* \n\nTotal Deaths : *{data["deaths"]}*\n\n_The best way to prevent illness from Coronavirus is to avoid being exposed to this virus_\n*#NoToCorona* \n\n👉 Type *Menu* to go to the Main Menu'
        else:
            text = 'I could not find the result, Please Try Again!'
        msg = resp.message(text)
        responded = True
    
    #Symptoms
    if 'b' == inmsg:
        text = f'```The COVID-19 virus``` affects different people in different ways. Most infected people will develop mild to moderate symptoms.\n\n_Common symptoms:_\n✅ Fever\n✅ Tiredness\n✅ Dry Cough\n\n_Some people may experience:_\n✅ Aches and Pains\n✅ Nasal Congestion\n✅ Runny Nose\n✅ Sore Throat\n✅ Diarrhoea\nOn average it takes *5–6 days* from when someone is infected with the virus for symptoms to show, however it can take up to *14 days*.\n\n👉 Type *Menu* to go to the Main Menu' 
        msg = resp.message(text)
        msg.media('https://i.ibb.co/m4nZKYb/symptoms.jpg')
        responded = True

    #Stop spreading
    if 'c' == inmsg:
        text = f'```Coronavirus infection can be prevented through the following means``` 👇 \n\n ✅ Small droplets from the nose or mouth which are spread when a person coughs or sneezes \n\n ✅ Touching an object or surface with these droplets on it and then touching your mouth, nose, or eyes before washing your hands \n \n ✅ Close personal contact, such as touching or shaking hands \nPlease watch the video for more information \n👉 https://youtu.be/0MgNgcwcKzE \n\n👉 Type *Menu* to go to the Main Menu'
        msg = resp.message(text)
        msg.media('https://i.ibb.co/M1svbHC/stop.png')
        responded = True
    
    #Do's and Don'ts 
    if 'd' == inmsg:
        text = f'```Do\'s and Don\'ts for fighting against COVID19``` \n\n ✅ Clean hands with soap and water or alcohol-based hand rub \n\n ✅ Cover nose and mouth when coughing & sneezing with a tissue or flexed elbow \n\n ✅ Avoid close contact & maintain 1-meter distance with anyone who is coughing or sneezin \n\n ✅ Isolation of persons traveling from affected countries or places for at least 14 day \n\n👉 Type *Menu* to go to the Main Menu'
        msg = resp.message(text)
        msg.media('https://i.ibb.co/Tbs1Hc5/DOS.jpg')
        responded = True

    if responded == False:
        r = requests.get('https://covidgideon.herokuapp.com/'+inmsg)
        if r.status_code == 200:
            data = r.json()
            text1 = f'```Covid-19 Cases in {incoming_msg.upper()}``` \n\nNew Cases : *{data["new_cases"]}* \n\nTotal Cases : *{data["total_cases"]}* \n\nRecovered : *{data["recovered"]}* \n\nTotal Deaths : *{data["deaths"]}*\n\n_The best way to prevent illness from Coronavirus is to avoid being exposed to this virus_\n*#NoToCorona*\n\n👉 Type *Menu* to go to the Main Menu'
        else:
            text1 = 'I could not find the result, Please Try Again!'
        msg = resp.message(text1)
    
    return(str(resp))

if __name__ == '__main__':
	app.run(debug=True)