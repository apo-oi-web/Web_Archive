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
	
	

#! JAVASCRIPT

print '<script type="text/JavaScript">';

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


$query=CGI->new;
@params = $query->param;

$index = 0;
foreach my $paramKey (@params) {
	$inputdata = $query->param($paramKey);
	$formList[$index] = $inputdata;
	$index = $index + 1;
	}

if($formList[0])
{
	print '<div class = "container">';
	print '<div class = "navigation">
       		<ul>       
       		<li><a href="./index.cgi">Home</a></li>
       		<li><a href="./rush.cgi">Rush</a></li>
       		<li><a href="./service.cgi">Service</a></li>
       		<li><a href="./fellowship.cgi">Fellowship</a></li>
       		<li><a href="./login.cgi">Login</a></li>	 
       		<li><a href="./Calendar/newCalendar.cgi">Calendar</a></li>
       		<li><a href="./history.html">History</a></li>
       		</ul>
       
       		<br/>
       		<div align = center>
       		<form action="https://www.paypal.com/cgi-bin/webscr" method="post">
       		<input type="hidden" name="cmd" value="_s-xclick">
       		<input type="image" src="https://www.paypal.com/en_US/i/btn/x-click-but21.gif" border="0" name="submit" alt="Make payments with PayPal">
       		<input type="hidden" name="encrypted" value="-----BEGIN PKCS7-----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-----END PKCS7-----">
       		</form>
       		</div>
       		</div>';
       		
	print '<div class = "about" >
	
       <p class = "bp1">Alpha Phi Omega (APO) is a national co-ed community service fraternity whose mission is to promote service, fellowship, and leadership.  
       </p>
	</div>';

	print '<div class = "inhalt">
	<form onsubmit="return validate(this)" action = "updateUser.cgi" method = "post">
	
	<p>Update Information </p>
	
	<ul>';       
	    print "<input type = \"hidden\" name = \"user\" value=$formList[0]></input>";
	    print '
	    <p> First Name <input type = "text" font-size = 18 size = 20 maxlength = 30 name = "first name"></input></p>
	    <p> Last Name <input type = "text" font-size = 18 size = 20 maxlength = 30 name = "last name"></input></p>
	    <p> Email <input type = "text" font-size = 18 size = 20 maxlength = 50 name = "email"> </p>
	    <p> Apartment <input type = "text" font-size = 18 size = 20 maxlength = 40 name = "apartment"></input> </p>
	    <p> Phone <input type = "text" font-size = 18 size = 20 maxlength = 12 name = "phone"></input> </p>
	    <p> AIM <input type = "text" font-size = 18 size = 20 maxlength = 30 name = "aim"></input> </p>';
	    print "<input type = \"hidden\" name = \"id\" value=$formList[1]></input>";
	    print '<p> <input size = 100 type = "submit" value = "Update" /></input> </p>
   	    
   	    </ul></div></div>';
 

#!END OF FORM
}

#!End of Body and HTML

print "</body> </html>";
