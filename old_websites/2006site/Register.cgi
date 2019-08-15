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

print '<html> <head> <title> Alpha Phi Omega </title> <script type="text/JavaScript">';

#! JAVASCRIPT

print "<!--\n";
print "function validate(theform){\n";

#! go through each item in the form
print 	"for (var i=0; i<theform.elements.length; i++){\n";
#!store the current item in the variable field
print 		"var field = theform.elements[i];\n";
#! If the item is a radio buddon
print 		"if (field.type == \"radio\"){\n";

#! Store the current index in Sindex and initialize the variable checked to 0 and rlength to 1
print 			"var Sindex = i;\n";
print 			"var checked = 0;\n";
print 			"var rLength=1;\n";

#! Find out the length of the radio button by checking if the next elemet on the form shares the same name as the current element
print 			"while(field.type == theform.elements[i+1].type && field.name == theform.elements[i+1].name){\n";
print 				"rLength++;\n";
print 				"i++;\n";
print 			"}\n";

#! For each element of the radio button see if it was checked.  If it was increment the checked variable. 				
print 			"for(var g = Sindex; g < rLength+Sindex; g++){\n";
print 				"if(theform.elements[g].checked){\n";
print 					"checked++;\n";
print 					"break;\n";
print 				"}\n";
print 			"}\n";		

#! IF check is still equal to 0 the button was not checked.  Alert the user and return false 				
print 			"if(checked == 0){\n";
print 				"i=Sindex;\n";
print 				"alert(\"Please select a value for the \"+field.name+ \"\");\n";				
print 				"setTimeout(\"theform.elements[\"+i+\"].focus()\", 10);\n";
print 				"return false;\n";
print 			"}\n";		
print		"}\n";

#! If the form item is not a radio button, it must be a scroll down menu
print 		"else{\n";

#! Check if the value of the selected field is null.  If it is, prompt the user to enter a value.
print 			"if (field.value == \"\"){";
print				"alert(\"You must enter a value for the \"+field.name+ \"\");\n";
print				"setTimeout(\"theform.elements[\"+i+\"].focus()\", 10);\n";
print				"return false;\n";
print			"}\n";
print		"}\n";

print	"}\n";

print  "if (theform.password.value != theform.password2.value)";
print   "{\n";
print	     "alert(\"The two password fields do no match\");\n";
print        "return false;\n";
print    "}\n"; 

#! If the form reaches here without returning false, the form is valid return true.

print   "return true;";
print 	"}//-->\n";
print '</script>';

#!Start form
print '</head><body>';

	print '<div class = "container">';
	print '<div class = "navigation">
	       <ul>       
	       <li><a href="./index.cgi">Home</a></li>
	       <li><a href="./rush.cgi">Rush</a></li>
	       <li><a href="./service.cgi">Service</a></li>
	       <li><a href="./fellowship.cgi">Fellowship</a></li>
	       <li><a href="./login.cgi">Login</a></li>
	       <li><a href="./Calendar/newCalendar.cgi">Calendar</a></li>
	       <li><a href="./history.cgi">History</a></li>
	       </ul></div>';				  	  			
		
	print '<div class = "about" >
			
		<p class = "bp1">Alpha Phi Omega (APO) is a national co-ed community service fraternity whose mission is to promote service, fellowship, and leadership.  
		</p>
		</div>';
		
	print "<div class = \"inhalt\">";
		print'<form onsubmit="return validate(this)" action = "register2.cgi" method = "post">';
		print 'First Name <input type = "text" font-size = 18 size = 20 maxlength = 30 name = "first name"></input><br/>
		       Last Name  <input type = "text" font-size = 18 size = 20 maxlength = 30 name = "last name"></input><br/>
		       Email Address <input type = "text" font-size = 18 size = 20 maxlength = 50 name = "email"></input><br/>
		       Apartment/Dorm <input type = "text" font-size = 18 size = 20 maxlength = 40 name = "apartment"></input><br/>
		       Phone	  <input type = "text" font-size = 18 size = 20 maxlength = 12 name = "phone"></input><br/>
		       Aim Name	  <input type = "text" font-size = 18 size = 20 maxlength = 30 name = "aim"></input><br/>
		       User Name  <input type = "text" font-size = 18 size = 20 maxlength = 20 name = "login"></input><br/>
		       Password	  <input type = "password" font-size = 18 size = 20 maxlength = 20 name = "password"></input><br/>
		       Confirm Password <input type = "password" font-size = 18 size = 20 maxlength = 20 name = "password2"></input><br/>
  		                  <td width = 200><input size = 100 type = "submit" value = "Register" /> </form>
	</div>';
		
	#!End of Body and HTML
	print "</div></body> </html>";
 

#!END OF FORM

#!End of Body and HTML
print "<br/>";
print "</p>";
print "</body> </html>";
