import smtplib
import email
import datetime
from wordOTD import createMessage

# This function sends an email with the specified body to the specified recipient
def email_alert(body,to):
    # Create an EmailMessage object
    msg = email.message.EmailMessage()
    
    # Set the content of the email to the specified body
    msg.set_content(body)
    
    # Set the recipient of the email to the specified email address
    msg['to'] = to
    
    # Set the email and password of the sender
    user = "example@gmail.com"
    password = "generated app-password for example gmail"
    
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
# then sends the message to the specified phone number via email to text (MMS)
def sendWord(number):
    # Create the message
    message = createMessage()
    
    # Capitalize the first letter of the message
    message = message[0].upper() + message[1:]
    
    # Send the message
    email_alert(message, number)
    print('Message Sent')

def main():
    # This variable is used to prevent multiple emails from being sent at the same time
    safe = True

    # Run the loop indefinitely
    while True:
        # Get the current minute and hour
        minute = datetime.datetime.now().minute
        hour = datetime.datetime.now().hour

        # Set safe to True at 7:31 to allow for the next email to be sent
        if hour == 7 and minute == 31:
            safe = True
        
        # Send an email at 7:30 if it is safe to do so (i.e., an email was not already sent at 7:30)
        if (hour == 7 and minute == 30) and safe:
            sendWord('examplenumber@mmsaddress')
            safe = False

# Run the main function
main()
