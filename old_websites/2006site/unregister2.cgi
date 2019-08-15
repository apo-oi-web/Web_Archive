#!/usr/bin/perl
#!

use CGI;
use CGI::Carp qw( fatalsToBrowser );
use DBI;
$query = new CGI;
$| = 1;

#!Print basic XHTML information 
print "Content-type:\n\n";

print "<?xml version='1.0' encoding='UTF-8' standalone='no' ?>\n";

print '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">';

print "\n";

print '<html> <head> <title> Administrator: Delete Account </title>';

print "\n";


print '<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>';
print '<link rel="stylesheet" type="text/css" href="myStyle.css" />';

print "\n";

print '<style type = "text/css">';
print 'h1 {';
print 'font-weight: bold;';
print '}';
print '</style>';

print "\n";

print "</head><body>";

print "\n";


print '<table width = 1200 border = 0>
  	<tr>
  	
  		<td width=200 align = top>
	
		<td width = 1000 align = top>
			<form  action = "deleteUser.cgi" method = "post">
			<table width = 800>
			  <tr>  <td width = 50>
				<td width = 300>
					<h1>Delete User Account</h1>
				<td width = 640>
			  </tr>
			  
			  <tr>  <td width = 50>
			  	<td width = 300>
			  		Enter User Name to Delete 
			  	<td width = 640>
			  		<input type = "text" name = "toDelete"></input></p>
			  </tr>
			  
			  <tr>  <td width = 50>
			  	<td width = 300>
			  		<p> <input type = "submit\" value = "DeleteUser"> </p>
			  	<td width = 640>
			  </tr>
			  
			</table>
	</tr>
	</table>';


#!End of Form
print '</form>';

#!End of Body and HTML
print "</body> </html>";
