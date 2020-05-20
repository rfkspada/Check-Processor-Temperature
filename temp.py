# coding=utf-8
import os, sys
import smtplib
from email.mime.text import MIMEText

critical = False
high = 20
too_high = 80

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

print(temp)

subject = "Alta temperatura no servidor"
body = " "
# Check if the temperature is abouve 60°C (you can change this value, but it shouldn't be above 70)

for i in temp:
    if (i > high):
        if i > too_high:
            critical = True
            body = body + "Critical warning! The actual temperature is: {}!!!!  Shutting down!!!! \n\n".format(i)
        else:
            body = "Warning! The actual temperature is: {} \n\n".format(i)

    print(body)

sys.exit(' ')

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
#    if critical:
#        os.popen('sudo halt')

# Don't print anything otherwise. 
# Cron will send you an email for any command that returns "any" output (so you would get another  email)
# else:
#   print "Everything is working fine!"
