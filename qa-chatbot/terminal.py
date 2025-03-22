import os
from dotenv import load_dotenv
import chainlit
import google.generativeai as genai


load_dotenv()

genai.configure(api_key=os.environ['GOOGLE_GEMINI_API_KEY'])

model = genai.GenerativeModel(model_name='gemini-2.0-flash')


while True:
    user_input = input('What\'s your Question or Enter to quit :  ')
   
    if user_input == "":
        print('Good Bye!')
        break
    
    response = model.generate_content(user_input)
    

    print("\nResponse : " , response.text)
