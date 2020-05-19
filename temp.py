# coding=utf-8
import os
import smtplib
from email.mime.text import MIMEText

critical = False
high = 60
too_high = 80

# At First we have to get the current CPU-Temperature with this defined function
# I need to modify this function to use sensors -j and read the resulting json!!
# If possible I need to count the number of cpus also!
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

# Now we convert our value into a float number

# temp must be a list with the temperature for each core.
temp = float(getCPUtemperature())

# Check if the temperature is abouve 60°C (you can change this value, but it shouldn't be above 70)
if (temp > high):
    if temp > too_high:
        critical = True
        subject = "Critical warning! The temperature is: {} shutting down!!".format(temp)
        body = "Critical warning! The actual temperature is: {} \n\n Shutting down the pi!".format(temp)
    else:
        subject = "Warning! The temperature is: {} ".format(temp)
        body = "Warning! The actual temperature is: {} ".format(temp)

    # Enter your smtp Server-Connection
    server = smtplib.SMTP('localhost', 25) # if your using gmail: smtp.gmail.com
    server.ehlo()
    server.starttls()
    server.ehlo
    # Login
    # server.login("your email or username", "your Password")
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "Root"
    msg['To'] = "root"

    # Finally send the mail
    # The email should be sent only if the temperature is too high!
    server.sendmail("root", "root", msg.as_string())
    server.quit()
    
    # Critical, shut down the pi
    # Need to shutdown ?????
    if critical:
        os.popen('sudo halt')

# Don't print anything otherwise. 
# Cron will send you an email for any command that returns "any" output (so you would get another  email)
# else:
#   print "Everything is working fine!"
