#!/usr/bin/perl
#!

use CGI;
use CGI::Carp qw( fatalsToBrowser );
use DBI;
$query = new CGI;
$| = 1;

print "Content-type:text/html\n\n";

print "<?xml version='1.0' encoding='UTF-8' standalone='no' ?>\n";

print '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">';

print '<html> <head> <title> Administrator: Change User Password </title>';

print '<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>';
print '<link rel="stylesheet" type="text/css" href="myStyle.css" />';

print '<style type = "text/css">';
print 'h1 {';
print 'font-weight: bold;';
print '}';
print '</style>';

print "</head><body>";

print '<table align = top align = center width = 1200 border = 0>
  	<tr>
  	
  		<td width=200 align = top>
	
		<td width = 1000 align = top>
			<form  action = "cAPswd.cgi" method = "post">
			<table align = top align = center width = 800>
			  <tr>  <td width = 50>
				<td width = 300>
					<h1>Change Administrator Password</h1>
				<td width = 640>
			  </tr>
			  
			  <tr>  <td width = 50>
			  	<td width = 300>
			  		Enter New Password 
			  	<td width = 640>
			  		<input type = "password" name = "password"></input></p>
			  </tr>
			  
			  <tr>  <td width = 50>
			  	<td width = 300>
			  		<p> <input type = "submit" value = "ChangePassword"> </p>
			  	<td width = 640>
			  </tr>
			  
			</table>
	</tr>
	</table>';

#!End of Body and HTML
print "</body> </html>";
