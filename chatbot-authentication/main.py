import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv
from typing import Dict , Optional

load_dotenv()

gemini_api_key = os.getenv('GOOGLE_GEMINI_API_KEY')

genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(model_name='gemini-2.0-flash')

@cl.oauth_callback
def oauth_callbacks(provider_id : str , token : str, raw_user_data : Dict[str , str], default_user : cl.User) -> Optional[cl.User]:
    """
    Handle the Oauth callback from Gitgub
    Return the user object if authentication is successfull , Otherwise None
    """
    print('Provider :' , provider_id)
    print('User Data' , raw_user_data)
    return default_user

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set('History' , [])
    await cl.Message(content='Hello how can i assist you todat ? ').send()
    


@cl.on_message
async def handle_message(message : cl.Message):
    
    history = cl.user_session.get('History')
    
    history.append({'role' : 'user' , "content" : message.content})
    
    format_history = []
    for msg in history:
        role = 'user' if msg['role'] == "user" else "model"
        format_history.append({"role" : role , "parts" : [{"text" : msg['content']}]})
        
    
    response = model.generate_content(format_history)
    
    response_x = response.text if hasattr(response , 'text') else ""
    
    history.append({'role' : "assistant" , "content" : response_x})
    cl.user_session.set('history' , history)
    
    await cl.Message(content=response_x).send()
