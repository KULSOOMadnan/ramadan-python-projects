from fastapi import FastAPI # importing fast Api
import random # random module 
app = FastAPI()

# List of side hustle ideas that users can get inspiration from
side_hustles = [
    "Freelance Writing - Start Offering you Writting Skills online !",
    "Web Development - Create a website for your business or for yourself !",
    "Social Media Management - Manage your social media accounts for your business or for yourself !",
    "Online Tutoring - Tutor students online for any subject you are good at !",
    "Graphic Design - Design a logo or a poster for your business or for yourself !",
    "Virtual Assistant - Be a virtual assistant for a business or for yourself !",
    "Photography - Take photos for a business or for yourself !",
    "Food Delivery - Deliver food for a business or for yourself !",
    "Ride-sharing - Drive for a ride-sharing company like Uber or Lyft !",
    "Dropshipping - Start a dropshipping business and sell products online !",
    "Blogging - Start a blog and make money from ads or affiliate marketing !",
    "YouTube Content Creation - Create a YouTube channel and make money from ads or affiliate marketing !",
    "Digital Marketing - Market your business online using social media or search engines !",
    "Pet Sitting - Take care of pets for a business or for yourself !",
    "Online Survey Taking - Take surveys for a business or for yourself !",
    "Transcription Services - Transcribe audio or video files for a business or for yourself !",
    "Proofreading - Proofread documents for a business or for yourself !",
    "Personal Shopping - Shop for a business or for yourself !",
    "Handmade Crafts Selling - Sell handmade crafts online !",
    "Fitness Training - Train people in fitness !"
]

# List of motivational quotes about money and success from famous people
money_making_qoutes = [
   'The best way to predict the future is to invent it. - Alan Kay',
   'The only way to do great work is to love what you do. - Steve Jobs',
   'Your time is limited, don\'t waste it living someone else\'s life. - Steve Jobs',
   'The way to get started is to quit talking and begin doing. - Walt Disney',
   'The only way to do great work is to love what you do. - Steve Jobs',
   'Money is like gasoline during a road trip. You do not want to run out of gas on your way to success. - Tim Fargo',
   'The only thing worse than starting something and failing... is not starting something. - Seth Godin',
   'Money is like a sixth sense without which you cannot make a good use of the other five. - Mohandas Gandhi',
   
]

@app.get('/side-hustle')
def get_side_hustle(api_key: str):
    """Return a random side huslte ideas from the list 
    Args:
        api_key (str): Authentication key required to access the endpoint
    Returns:
        dict: Contains either a random side hustle idea or an error message
    """
    if api_key != "12345678":
        return {'error' : 'Invalid API key '}
    return {"side_hustles": random.choice(side_hustles)}

@app.get('/money_quotes')
def get_money_quotes(api_key : str):
    """Return a random money making qoute from the list
    Args:
        api_key (str): Authentication key required to access the endpoint
    Returns:
        dict: Contains either a random motivational quote or an error message
    """
    if api_key != '7890':
        return {'error' : 'Invalid API Key'}
    return{"money_quotes": random.choice(money_making_qoutes)}


# Entry point for running the FastAPI application
# if __name__ == "__main__":
