#!/usr/bin/perl
#!

use CGI;
use CGI::Carp qw( fatalsToBrowser );
use DBI;
$query = new CGI;
$| = 1;

$query=CGI->new;
@params = $query->param;

$index = 0;
foreach my $paramKey (@params) {
	$inputdata = $query->param($paramKey);
	$formList[$index] = $inputdata;
	$index = $index + 1;
	} 
	
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
	       <li><a href="./history.html">History</a></li>
	       </ul></div>';				  	  			
		
	print '<div class = "about" >
			
		<p class = "bp1">Alpha Phi Omega (APO) is a national co-ed community service fraternity whose mission is to promote service, fellowship, and leadership.  
		</p>
		</div>';
		
	print "<div class = \"inhalt\">";
		print'<form action = "aEvent.cgi" method = "post">';
		print "<input type = \"hidden\" name = \"user\" value=\"$formList[0]\">";
		print "Event Name <input type = \"text\" font-size = 18 size = 20 maxlength = 50 name = \"EventName\"></input><br/>
		       Date  <select name = \"EventMonth\">
 				<option value = \"01\"> Jan</option>
        			<option value = \"02\"> Feb</option>
        			<option value = \"03\"> Mar</option>
			        <option value = \"04\"> Apr</option>
        			<option value = \"05\"> May</option>
        			<option value = \"06\"> June</option>
        			<option value = \"07\"> July</option>
        			<option value = \"08\"> Aug</option>
        			<option value = \"09\"> Sep</option>
        			<option value = \"10\"> Oct</option>
        			<option value = \"11\"> Nov</option>
        			<option value = \"12\"> Dec</option></select>
        			
        		     <select name = \"EventDay\">
				<option value = \"01\"> 01</option>
				<option value = \"02\"> 02</option>
				<option value = \"03\"> 03</option>
				<option value = \"04\"> 04</option>
				<option value = \"05\"> 05</option>
				<option value = \"06\"> 06</option>
				<option value = \"07\"> 07</option>
				<option value = \"08\"> 08</option>
				<option value = \"09\"> 09</option>
				<option value = \"10\"> 10</option>
				<option value = \"11\"> 11</option
				<option value = \"12\"> 12</option>
				<option value = \"13\"> 13</option>
				<option value = \"14\"> 14</option>
				<option value = \"15\"> 15</option>
				<option value = \"16\"> 16</option>
				<option value = \"17\"> 17</option>
				<option value = \"18\"> 18</option>
				<option value = \"19\"> 19</option>
				<option value = \"20\"> 20</option>
				<option value = \"21\"> 21</option>
				<option value = \"22\"> 22</option>
				<option value = \"23\"> 23</option>
				<option value = \"24\"> 24</option>
				<option value = \"25\"> 25</option>
				<option value = \"26\"> 26</option>
				<option value = \"27\"> 27</option>
				<option value = \"28\"> 28</option>
				<option value = \"29\"> 29</option>
				<option value = \"30\"> 30</option>
				<option value = \"31\"> 31</option></select>
				
			     <select name = \"EventYear\">
				<option value = \"2006\"> 2006</option>
				<option value = \"2007\"> 2007</option>
				<option value = \"2008\"> 2008</option>
				<option value = \"2009\"> 2009</option></select>
        			<br/>
		       Start <select name = \"EventHour\">
       		 		<option value = \"01\"> 1</option>
        			<option value = \"02\"> 2</option>
				<option value = \"03\"> 3</option>
				<option value = \"04\"> 4</option>
				<option value = \"05\"> 5</option>
				<option value = \"06\"> 6</option>
        			<option value = \"07\"> 7</option>
				<option value = \"08\"> 8</option>
				<option value = \"09\"> 9</option>
				<option value = \"10\">10</option>
				<option value = \"11\">11</option>
				<option value = \"12\">12</option></select>
			:
			     <select name = \"EventMinute\">
			       	<option value = \"00\"> 00</option>
			        <option value = \"15\"> 15</option>
				<option value = \"30\"> 30</option>
				<option value = \"45\"> 45</option></select>
			
			     <select name = \"AmPm\">
			      	<option value = \"AM\"> AM</option>
			        <option value = \"PM\"> PM</option></select>
        			<br/>
        	       End <select name = \"EventHour2\">
		              	<option value = \"01\"> 1</option>
		               	<option value = \"02\"> 2</option>
		       		<option value = \"03\"> 3</option>
		       		<option value = \"04\"> 4</option>
		       		<option value = \"05\"> 5</option>
		       		<option value = \"06\"> 6</option>
		         	<option value = \"07\"> 7</option>
		       		<option value = \"08\"> 8</option>
		       		<option value = \"09\"> 9</option>
		       		<option value = \"10\">10</option>
		       		<option value = \"11\">11</option>
		       		<option value = \"12\">12</option></select>
		       	:
		            <select name = \"EventMinute2\">
		       	       	<option value = \"00\"> 00</option>
		       	        <option value = \"15\"> 15</option>
		       		<option value = \"30\"> 30</option>
		       		<option value = \"45\"> 45</option></select>
		       			
		       	    <select name = \"AmPm2\">
		       	      	<option value = \"AM\"> AM</option>
		       	        <option value = \"PM\"> PM</option></select>
        			<br/>
		       Description <textarea name = \"apartment\" rows=\"5\" cols = \"50\"></textarea><br/>
		       Type  <select name = \"Event Type\">
		       		<option value = \"Fellowship\"> Fellowship</option>
			        <option value = \"Rush\"> Rush</option>
				<option value = \"Service\"> Service</option></select><br/>
  		       <td width = 200><input size = 100 type = \"submit\" value = \"Add Event\" /> </form>
	</div>";
		
	#!End of Body and HTML
	print "</div></body> </html>";
 

#!END OF FORM

#!End of Body and HTML
print "<br/>";
print "</p>";
print "</body> </html>";
