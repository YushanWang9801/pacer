import requests
from decouple import config

prompt_template = """
You are a very kind and friendly AI assistant specializing in parks and trails. 
You provide detailed information about parks or trails in a structured format.
Location and Directions need to be shown in your respsonse.

Examples of User Input:
"Teegarden Park in Berwyn, PA"
"Marsh Creek State Park in Pennsylvania"
"Tiger Mountain West, WA"

Examples of AI Output:
Park Name: Teegarden Park
Location: Berwyn, PA
Description: Teegarden Park is a beautiful neighborhood park offering a peaceful and serene escape from the hustle and bustle of city life. With its lush green spaces and mature trees, visitors can enjoy a variety of outdoor activities at this park.
Activities: Walking, playgrounds, picnicking
Facilities: Restrooms, parking, picnic tables
Tips: Best visited in the morning for a peaceful walk or picnic with family or friends.

Another Example:
Discovering Tiger Mountain West, WA
Tiger Mountain West, nestled just 35 miles east of Seattle, Washington, is a verdant escape into nature known as part of the "Issaquah Alps." This area, rich in wildlife and forest landscapes, is a hiker's paradise with over 34 miles of trails, including the renowned West Tiger #3 trail. Whether you're up for a challenging hike or interested in paragliding from Poo Poo Point, Tiger Mountain offers breathtaking views and a variety of activities for all ages.
Location and Directions:
1. Drive east on I-90 past Bellevue.
2. Take exit 20 just past Issaquah.
3. Turn right onto 270th Ave SE, then right onto SE 79th Street.
4. Proceed through the gate onto a gravel road leading to the parking lot.

Real-time Information: {real_time_info}
chat_history: {chat_history}
Human: {question}
AI:
"""

INIT_PROMPT = '''
Hello there! This is your personalized park trail advisor. 
Please enter the name of the park you are interested in. 
I am happy to provide detailed information.
'''

NPS_BASE_URL = "https://developer.nps.gov/api/v1/alerts?parkCode=acad,dena"
API_BASE_URL = "https://api.gptsapi.net/v1"

NPS_API_KEY = config('NPS_API_KEY')
CHAT_INPUT_PROMPT = "Enter your question about a park or trail..."

MAX_TOKEN = 800

def fetch_park_info(query):
    params = {'api_key': NPS_API_KEY}
    response = requests.get(NPS_BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and len(data['data']) > 0:
            alerts_info = ""
            for alert in data['data']:
                alerts_info += f'''
                                Title: {alert['title']}\n
                                Description: {alert['description']}\n\n
                                '''
            return alerts_info.strip()
    
    return "No real-time information available."

if __name__ == "__main__":
    test_query = "Teegarden Park in Berwyn, PA"
    print(fetch_park_info(test_query))
