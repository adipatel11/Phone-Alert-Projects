import requests
import smtplib
import email
import datetime
import calendar

# This script sends a text message to a specified recipient with the current weather at 7:30 a.m. local time
# information for a specified location. The weather data is retrieved from the OpenWeatherMap API.
# https://home.openweathermap.org/

def email_alert(body,to):
    """
    Send an email with the specified body to the specified recipient.
    
    Parameters:
        body (str): The content of the email.
        to (str): The email address of the recipient.
    """
    msg = email.message.EmailMessage()
    msg.set_content(body)
    msg['to'] = to
    
    # Hard-coded login information for the email account to send the message from.
    user = "example@gmail.com"
    password = "given generated app-password"

    # Connect to the SMTP server and start a secure TLS connection
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    
    # Login to the email account using the specified email and password
    server.login(user,password)
    
    # Send the email
    server.send_message(msg)
    
    # Disconnect from the SMTP server
    server.quit()

# This function creates a message using the createMessage function from the wordOTD module,
# then sends the message to the specified phone number via email

def sendWeather(town, key, recipient):
    """
    Send a text message with the current weather information for the specified location to the specified recipient.
    
    Parameters:
        town (str): The name of the location to get the weather for.
        key (str): The API key for the OpenWeatherMap API.
        recipient (str): The phone number or email address of the recipient to send the text message to.
    """

    # A dictionary of example locations in Mississippi and their latitude/longitude coordinates.
    locations = {'clinton':[32.31276409667422,-90.3572500313335], 'columbus':[33.48972597386832, -88.41865176426754],
                 'jackson':[32.282081890663534, -90.20997290438726], "oxford":[34.368884610924674, -89.53028698892851],
                 'madison':[32.48121224475622, -90.12341908897285]}

    # Get the current month, day, and year.
    month = calendar.month_name[datetime.date.today().month]
    day = datetime.date.today().day
    year = datetime.date.today().year

    # Retrieve the current weather data from the OpenWeatherMap API.
    weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={locations[town][0]}&lon={locations[town][1]}&appid={key}").json()

    clouds = weather['weather'][0]['description']
    currentTemp = toF(weather['main']['temp'])
    feelsLike = toF(weather['main']['feels_like'])
    city = weather['name']



    time = datetime.datetime.today().strftime("%I:%M %p")
    weather_statement = f'Hello! It is currently {time} {month} {day}, {year}. The temperature right now in {city} is about {currentTemp}°F. It currently feels like {feelsLike}°F outside with {clouds}.' 
    email_alert(weather_statement, recipient)
    print(f"Weather Text sent at {time} {month} {day} to {recipient}")

def toF(x):
    """
    Convert the temperature from Kelvin to Fahrenheit.
    
    Parameters:
        x (float): The temperature in Kelvin
"""

    return round((9/5)*(x-273.15) + 32, 1)


def main():

    # Store the API key in a variable
    APIkey = 'given API key from OpenWeather'

    # Initialize a flag to prevent multiple messages being sent during the same minute (7:30)
    safe = True

    # Run the loop indefinitely
    while True:
        # Get the current minute and hour
        minute = datetime.datetime.now().minute
        hour = datetime.datetime.now().hour

        # Once the minute has passed, set the flag to true
        if hour == 7 and minute == 31:
            safe = True

        # If it is exactly 7:30 (7:30 PM) and the safe flag is True,
        # send the weather information for Columbus to the specified phone number
        # using the sendWeather function and the API key, and set the safe flag to False
        if (hour == 7 and minute == 30) and safe:
            sendWeather('columbus', APIkey, 'examplenumber@mmsaddress')
            safe = False




main()


