# Check-Processor-Temperature

Check the processor temperature. If it is too high, the script send an e-mail to the sys-admin.

This is based on the script form https://gist.github.com/LeonardoGentile/7a5330e6bc55860feee5d0dd79e7965d with the same aim. The difference is that this script works for servers.

To make this as a cronjob running every 30 min do this

mkdir -p ~/scripts

vi ~/scripts/temp.py

paste the code from the script above.

**Edit the variables At lines 7 to 11 as you desire: **

  *mail_from -> a gmail account
  *password -> password fo the account
  *mail_to -> python list to whom the email should be send
  *high -> First warning temperature
  *too_high -> Critical warning temperature

Then in the terminal: 

crontab -e 

and add this:

/30 * * * * python3 ~/scripts/temp.py

(if you never use contrab, you will need to choose a text editor)

close crontab editor (ctrl-x if nano or esc, then :wq if vim)

That should do the work.

