# Check-Processor-Temperature

Check the processor temperature. If it is high, the script send an e-mail to the sys-admin.

This is based on the script form https://gist.github.com/LeonardoGentile/7a5330e6bc55860feee5d0dd79e7965d with the same aim. The difference is that this script works for servers.

This script requires the lm-sensors package installed.

To make this as a cronjob running every 30 min do this

mkdir -p ~/scripts

vi ~/scripts/temp.py

paste the code from the script above.

**Edit the variables At lines 7 to 11 as you desire:**

  * mail_from -> a gmail account
  * password -> password for the account
  * mail_to -> python list to whom the email should be send
  * high -> First warning temperature
  * too_high -> Critical warning temperature

It is the user responsability to check the correct temperatures interval (high and too_high).

Then in the terminal type: 

crontab -e 

A text editor will open a text file (if you never use crontab, you will need to choose a text editor).

Add the following line to the end of the file:

\*/30 * * * * python3 ~/scripts/temp.py

close crontab editor (ctrl-x if nano or esc, then :wq if vim)

That should do the work. If you want to edit the cronjobs just type crontab -e again. 

