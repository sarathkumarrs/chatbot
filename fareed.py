from flask import Flask
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
import string    
import random
import time

  
  
application = Flask(__name__)


invoke_messages = ['hai','hi','hey','whatsup']
greetings = ['morning','evening','night','good']
good = ['good','sarath']
  
@application.route("/", methods=["POST"])
# chatbot logic
def bot():
    data = request.form 
    name = data.get('ProfileName')
    print(data)
    print('request received!')
    # user input
    user_msg = request.values.get('Body', '').lower()
    words = user_msg.split()
  
    # creating object of MessagingResponse
    response = MessagingResponse()
    print(user_msg)

    if set(user_msg.split()).intersection(invoke_messages):
        msg = response.message(f'''Hi {name},
    My self Klara Efuturex bot am your new hire.''')
        msg = response.message('What you would like to know about? You can reply \'roadmap\' for the roadmap and \'product\' for product launch')
    elif 'product' in user_msg:
        msg = response.message("https://drive.google.com/file/d/1GRf3DwKdaSmpVyuByn-tAb1DY95GOxGZ/view?usp=sharing")

    elif 'road' in user_msg:
        msg = response.message("https://drive.google.com/file/d/1cW-glMftbHh8aP8Sn7bsaL8DPA5SHODS/view?usp=sharing")
    else:
            msg = response.message("My knowledge is restricted to the given data! To know about roadmap reply \'roadmap\' and for product reply \'product\'")

        
    
  
    return str(response)
  
 



if __name__ == "__main__":
    application.run()
