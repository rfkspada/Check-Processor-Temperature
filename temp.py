# coding=utf-8
import os, sys
import smtplib
from email.mime.text import MIMEText
import socket

mail_from = 'server_mail'
password = 'account_pass'
mail_to = ['user_address']
high = 60
too_high = 70

# At First we have to get the current CPU-Temperature with this defined function
# I need to modify this function to use sensors -j and read the resulting json!!
# If possible I need to count the number of cpus also!
def getCPUtemperature():
    temp = []
    os.system('sensors -u -A > temp.out')
    with open ('temp.out', 'r') as out:
        for line in out:
            if 'temp' in line and 'input' in line:
                temp.append(line.split(':')[1].strip())
    os.system('rm temp.out')
    return temp
# Now we convert our value into a float number

# temp must be a list with the temperature for each core.
tempstr = getCPUtemperature()

temp=[]
for i in tempstr:
    temp.append(float(i))

subject = "Alta temperatura no servidor"
body = ""
critical = False
send = False
# Check if the temperature is abouve 60°C (you can change this value, but it shouldn't be above 70)

for i in temp:
    if (i > high):
        send = True
        if i > too_high:
            critical = True
            body = body + "Critical warning! The actual temperature is: {}!!!!  Please shut down!!!!\n".format(i)
        else:
            body = body + "Warning! The actual temperature is: {}\n".format(i)

if send:
    host = socket.gethostname()
    body = "Message from {}\n".format(host) + body
    # Enter your smtp Server-Connection
    server = smtplib.SMTP_SSL('smtp.gmail.com') # if your using gmail: smtp.gmail.com
    # Login
    server.login(mail_from, password)

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = mail_from 
    msg['To'] = ", ".join(mail_to)

    # Finally send the mail
    # The email should be sent only if the temperature is too high!
    server.sendmail(mail_from, mail_to, msg.as_string())
    server.quit()

# Critical, shut down the pi
# Need to shutdown ?????
#    if critical:
#        os.popen('sudo halt')

# Don't print anything otherwise. 
# Cron will send you an email for any command that returns "any" output (so you would get another  email)
# else:
#   print "Everything is working fine!"
