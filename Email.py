import smtplib
from email.messages import EmailMessages
email=EmailMessages()
email["from"]="Enteraemail@gamil.com"
email["to"]="Enteranotheremail@gmail.com"
email["subjet"]="Now you have got 20 mmillion $"

email.set.content("You have got a gift")

with smtplib.SMTP(host="smtp.gmail.com",port=587)as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("Your emailadress","Password of email")

    smtp.send_message(email)
    print("All have been done")
