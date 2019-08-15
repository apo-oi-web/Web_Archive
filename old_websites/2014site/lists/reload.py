#!/usr/bin/python
import subprocess

def main():
    print "Content-type: text/html\n\n"
    subprocess.call("/home/apo/public_html/lists/apoLists.sh")
    print "<html><head><title>APO ALIASES</title></head>"
    print "<body><center><hr><table align='center'>"
    print "<tr><th>APO ALIASES NOW RELOADED.</th></tr>"
    #print "<tr><td>Click MAIN LIST to return.</td></tr>"
    print "</table><hr></center></body></html>"

main()
