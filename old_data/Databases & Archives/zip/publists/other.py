#!/usr/bin/python
import subprocess
import cgi

def main():
    print "Content-type: text/html\n\n"
    print "<html><head><title>OTHER ALIASES</title></head><body>"
    print "<hr><table align='center'><tr><th>ALIAS</th><th>OWNER</th><th>LAST UPDATED</th></tr><tr><td>"
    form = cgi.FieldStorage()
    alias = form["alias"].value
    subprocess.call("other.sh '%s'" % alias)
    list = "other/list/" + alias
    owner = "other/owner/" + alias
    time = "other/time/" + alias
    data = "other/data/" + alias
    print alias
    print "</td><td>"
    print " | "
    print open(owner,"r").read()
    print "</td><td>"
    print " | "
    print open(time,"r").read()
    print "</td></tr><tr><td colspan="3">"
    print "<iframe src="other/data/$alias></iframe>"
    
    print "</td></tr></table><hr></body></html>"

main()
