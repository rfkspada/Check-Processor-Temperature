# Check-Processor-Temperature

Check the processor temperature. If it is too high, the script send an e-mail to the sys-admin.

This is based on the script form https://gist.github.com/LeonardoGentile/7a5330e6bc55860feee5d0dd79e7965d with the same aim. The difference is that this script works for servers.

To make this as a cronjob running every 30 min do this

mkdir -p ~/scripts
vi ~/scripts/temp.py
paste the code from the script above.

Then crontab -e and add this:

30 * * * * python ~/scripts/temp.py
close crontab editor (ctrl-x if nano or esc, then :wq if vim)

That's it

I need to check how to remove it from crontab!!!!

