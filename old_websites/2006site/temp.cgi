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



print '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" >
	<head>
	<link rel="stylesheet" type="text/css" href="APO_style.css" />
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
	<meta name="author" content="Amanda Jamin" />
	<meta name="keywords" content="service community faternity alpha phi omega" />
	<meta name="description" content="Website for the WPI chapter of Alpha Phi Omega" />
	<title>Alpha Phi Omega</title>';

#!Start form
print '</head><body class="wpi-apo>';

#!BEGIN FORM

print '<div class = "container">';
print '<div class = "navigation">
       <ul>
       <li><a href="./index.cgi">Home</a></li>
       <li><a href="./rush.cgi">Rush</a></li>
       <li><a href="./service.cgi">Service</a></li>
       <li><a href="./fellowship.cgi">Fellowship</a></li>
       <li><a href="./login.cgi">Brothers</a></li>	  			
       <li><a href="./pLogin.cgi">Pledges</a></li>
       <li><a href="./history.cgi">History</a></li>
       </ul></div>';				  	  			

print '<div class = "about" >
	
       <p class = "rp1">"People rarely succeed unless they have fun in what they are doing."
	-Dale Carnegie
       </p>
	</div>';

print '<div class = "inhalt">

  	<form onsubmit="return validate(this)" action = "success.cgi" method = "post">
				
		<h2><span class = indexTitle> Please Log in </span></h2>
							
		<p>User Name
		<input type = "text" font-size = 18 size = 20 maxlength = 20 name = "userName"></input></p>
		<p> Password
		<input type = "password" font-size = 18 size = 20 maxlength = 30 name = "password"></input></p>
		<p> <input type = "submit" value = "Login" /> </p>
		<p> Not Registered? <a href="http://users.wpi.edu/~ajamin/APO/Register.cgi"> Register Now.</a></p>
	</form>';
       
#!End of Body and HTML
print "</div></body> </html>";
