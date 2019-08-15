#!/usr/bin/python
import subprocess

def main():
    print "Content-type: text/html\n\n"
    #subprocess.call("/home/apo/public_html/lists/apoLists.sh")
    print "<html><head><title>APO ALIASES</title></head><body>"
    #print "<center><a href="reload.py">RELOAD VALUES</a></center><br>"
    print "<table align='center'><tr><th><u>ALIAS</u></th><th><u>OWNER</u></th><th><u>LAST UPDATED</u></th></tr><tr><td>"
    lists = ['apo-alpha','apo-bids','apo-chairs','apo-conclave','apo-exec','apo-fellowship','apo-historian','apo-membership','apo-omegas','apo-phi','apo-pledgetrainer','apo-pledges','apo-pr','apo-president','apo-prospective','apo-recruitment','apo-secretary','apo-sergeantatarms','apo-service','apo-slides','apo-social','apo-treasurer','apo-underclassmen','apoheadsofhouse','execsnogeorge','ift','apo-oi-alumni','freefood','apo-brothers']
    for list in lists:
        link = "links/" + list
        print '<a href="data/%s" target="frame">%s</a><br>' % (list, list)
    print "</td><td>"
    for list in lists:
        owner = "owners/" + list
        print " | "
        print open(owner,"r").read()
        print "<br>"
    print "</td><td>"
    for list in lists:
        time = "times/" + list
        print " | "
        print open(time,"r").read()
        print "<br>"
    print "</td></tr></table></body></html>"

main()
