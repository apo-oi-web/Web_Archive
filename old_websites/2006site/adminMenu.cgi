#!/usr/bin/perl
#!

use CGI;
use CGI::Carp qw( fatalsToBrowser );
use DBI;
$query = new CGI;
$| = 1;

#!Print basic XHTML information 
print "Content-type:text/html\n\n";

print "<?xml version='1.0' encoding='UTF-8' standalone='no' ?>\n";

print '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">';

print '<html> <head> <title> Administrator: Change Admin Password </title>';

print '<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>';
print '<link rel="stylesheet" type="text/css" href="myStyle.css" />';

print '<style type = "text/css">';
print 'h1 {';
print 'text-align: center;';
print 'font-weight: bold;';
print '}';
print '</style>';

print "</head><body>";

print '<p><img src="./DesignPics/goss.gif" id="Goss" align = top /><img src="./DesignPics/apo2.gif" id="AlphaPhiOmega" align = topalt = "Alpha Phi Omega" /></p>';
print '<table align = left align = top width = 1200 border = 0 >
  	<tr>
  	  	<td width=200 align = top >
  	  		<p> <a href="http://users.wpi.edu/~ajamin/APO/rush.cgi"><img src="./DesignPics/Rush.gif" align = top border="0" /></a></p>
			<p><a href="http://users.wpi.edu/~ajamin/APO/service.cgi"><img src="./DesignPics/Link2.gif" align = top border="0" /></a></p>
			<p><a href="http://users.wpi.edu/~ajamin/APO/fellowship.cgi"><img src="./DesignPics/Fellow.gif" align = top border="0" /></a></p>
			<p><a href="http://users.wpi.edu/~ajamin/APO/login.cgi"><img src="./DesignPics/Brothers.gif" align = top border="0" /></a></p>
  	  		<a href="http://users.wpi.edu/~ajamin/APO/pledgeLogin.cgi"><p><img src="./DesignPics/Pledges.gif" align = top border="0" /></a></p>';
		
		print '<td width = 800 align = top>
			<table align = top width = 800>
				<tr>
					<td width = 10>
					<td width = 300>
						<h1><br/>Administrator Maintenance Page</h1>
					<td width = 490>
				</tr>
				
				<tr>
					<td width = 10>
					<td width = 300>
						<p><a href="http://users.wpi.edu/~ajamin/APO/unregister.cgi">Delete User Account</a></p>
					<td width = 490>
				</tr>
				
				<tr>
					<td width = 10>
					<td width = 300>
						<p><a href="http://users.wpi.edu/~ajamin/APO/cUserPswd.cgi">Change User Password</a></p>
					<td width = 490>
				</tr>
				
				<tr>
					<td width = 10>
					<td width = 300>
						<p><a href="http://users.wpi.edu/~ajamin/APO/cAdminPswd.cgi">Change Administrator Password</a></p>
					<td width = 490>
				</tr>
				
				<tr>
					<td width = 10>
					<td width = 300>
					<p><a href="http://users.wpi.edu/~ajamin/APO/approve.cgi">Approve User Account</a></p>
					<td width = 490>
				</tr>
				
				<tr>
					<td width = 10>
					<td width = 300>
						<p><a href="http://users.wpi.edu/~ajamin/APO/">Logout </a></p>
					<td width = 490>
				</tr>';

#!End of Body and HTML
print "</body> </html>";
