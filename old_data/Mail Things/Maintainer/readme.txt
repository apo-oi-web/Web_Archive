Hello, if you are reading this, then you must be the APO account
maintainer.  I received some instruction from my predecessor (John Grossi)
so I figured it would be helpful for those who follow me (Brian Pothier).
	Where to begin..  

---CRONJOBS: 
	Well, to start the cron job file is in this directory.  If you
ever need to change this, edit the text file in this directory and then
install the new file with "crontab crontab.bigwpi".  Currently, it just
moves the apo-l and aposoc-l lists to *.yesterday at 5:00am.  It is VERY
helpful to ONLY install cronjobs via this method, i.e.  create a file here
with the name of the host it will be installed on.  Otherwise, it is easy
to forget which host has the cronjob. 

---Procmail:
	This is run vie the .procmailrc file.  First off, edit it and
change the OWNER= line to contain your e-mail address.  This will send all
important e-mail, i.e. from Root/AEJ/Postmaster to you rather than the APO
account.  This way it is more likely to get fixed quickly.  (I logged into
APO account once a week or so..)  PLEASE be careful what you change, as if
you are not careful all e-mail could get trashed and never received.  If
possible read about procmail ("man procmail", "man procmailex").  It takes
some practice and experimenting.  After changing anything, send a test
message to the APO account to make sure mail still gets through.

---Mailing lists:
	All WPI mailing lists are contained in '/shared/aliases/*' where *
is the name of the list.  To create a new alias, send e-mail to
questions@wpi.edu  When you create a new one, place a link in
~/Mailing-Lists pointing to the file.  To do this for a list called
"blah@wpi.edu", do: 
	cd ~/Mailing-Lists
	ln -s /shared/aliases/blah
	This will create a symbolic link to the file in Mailing-Lists
called blah.  To add/remove people from mailing lists (apo's :), i.e.
aponews, just edit the file in Mailing-Lists called aponews.  The symbolic
link will tell it to go edit the file in /shared/aliases.  Addresses are
entered either as:

bdp
bdp@wpi.edu
Brian Pothier <bdp@wpi.edu>
#This is a comment

	All 3 of these are valid lines.  I prefer the 3rd, as it also
tells you who it is.  Comments can be added to the file with lines
starting with a #.  I usually throw the apo account in, and add a section
to the .procmailrc to archive the lists.
	Periodically, I go through and split up the archive of aponews.
Look in ~/FTPSite/mailinglists/ for the files.  We only have a 1meg quota
on the FTP site, so it sometimes gets necessary to condense things.

---Ownership
	Most files are owned by the apo account and group "officers".
Important files should be group "apo".  I had only myself and the current
president in the "apo" group.  The mailing lists have to be owned by
someone, usually YOU.  You need to have the current owner (do a "ls -l
/shared/aliases/aponews" or whatever to see who owns it) send e-mail to
"questions@wpi.edu" to get ownership changed.  MAKE SURE TO DO THIS BEFORE
THEIR ACCOUNT GETS DELETED!!!  Do the same for the owner of the APO
account.  You only need to login to the APO account and send e-mail to
questions asking them to change ownership.  To change members of the
groups, type "gred".  It is a little weird, but "/officers" will select
the "officers" group, 'p' will print out the current members, '?' will
give additional help.

---WWW Pages
	I created a script to make new members pages.  It is in
~/bin/make.brotherhtml.scr  It will create 2 files that you move into the
~/public_html directory.  Check the files it creates before moving them,
just in case..  Feel free to edit the script it shouldn't be too bad to
figure out.  It sure beats changing it by hand!!
	Also, the comments.html file sends e-mail to the apo account and
to the person specified in the .procmailrc file as WEBMASTER.  Change the
WEBMASTER line to point to whoever it is (I was both maintainer and web
guy).

---Misc
	Not sure what else you might need to know, but if you think of
something, please add it to this file for those who follow you.  I might
be able to be reached at the following addresses:
bdp@mindport.net bdp@kluge.net bdp@bigfoot.com bdp@poboxes.com bdp@wpi.edu
Good luck,
Brian Pothier - Class of 97, RecSec/Maintainer 12/94-12/96
