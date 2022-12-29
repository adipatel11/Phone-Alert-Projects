# Phone-Alert-Projects
Applications that Utilize the Email and SMTP Python Libraries to Send Phone Alerts

## Example:

![iPhonePic3](https://user-images.githubusercontent.com/120439586/209910686-1de173bf-a27e-4d35-a674-f1939d858a6c.png)

## Understanding this Repository

These projects are general templates for users to run. For example, certain variables such as "username", "password", and API keys need
to be filled in by the user. SMTP is used to log in to a certain Gmail and send an MMS text message. This way, the message will show up
on any phone as a text message even though it was sent as an email. The "email" module formats the message that needs to be sent. In order
to log in to a Gmail, an app password needs to be created so that the user is able to log in with the program without two-factor authentication.

## Information on Specific Projects

### Word of the Day Project

The main.py file in this folder needs to be run in the same directory as the wordOTD.py file. This project simply creates a "word of the day"
message and sends it as a text message using the process described above.
