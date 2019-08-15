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

print '<table align = top align = center width = 1200 border = 0>
  	<tr>
  	
  		<td width=200 align = top>
	
		<td width = 1000 align = top>
			  <form  action = "findBrother.cgi" method = "POST">
<form method="post" action="/cgi-bin/webform.pl">
<input type="hidden" name="email-recipients" value="apo-membership@wpi.edu">
<input type="hidden" name="email-subject" value="APO little">
<input type="hidden" name="email-template" value="/www/docs/Alex/emailExample.tmpl">
<input type="hidden" name="success-page" value="/success.tmpl">
<input type="hidden" name="required-fields" value="form-email,Dept">
<input type="hidden" name="form-dependency1" value="form-fname,form-lname">
<input type="hidden" name="form-record-file" value="./record.txt">

First Name :<input type="text" size="30" name="form-fname">
Last Name: <input type="text" size="30" name="form-lname">
E-mail :<input type="text" size="30" name="form-email">
Phone :<input type="text" size="15" name="Phone">
Department :<input type="text" size="30" name="Dept">
Mailing Address: <textarea name="Address" rows="3" cols="50" wrap="on"></textarea>
<input type="submit">
</form>			 
			 <table align = top align = center width = 800>
				  <tr>  <td width = 50>
					<td width = 300>
						<h1>Find a Brother</h1>
					<td width = 640>
				  </tr>
			  
				  <tr>  <td width = 50>
				  	<td width = 300>
				  		Enter Brother\'s First Name        (Required)
				  	<td width = 640>
				  		<input type = "text" name = "fname"></input></p>
				  </tr>
			  
				  <tr>  <td width = 50>
				  	<td width = 300>
				  		Enter Brother\'s Last Name         (optional)
				  	<td width = 640>
				  	<input type = "text" name = "lname"></input></p>
				  </tr>
			  
				  <tr>';
					print "<p><input type = \"hidden\" name = \"user\" value=$formList[0]> </p>";									 			
	  	 		  print '</tr>
				  
				  <tr>  <td width = 50>
				  	<td width = 300>
			  		<p> <input type = "submit" value = "Find Brother"> </p>
				  	<td width = 640>
				  </tr>
			  
			</table>
			</form>
	</tr>
	</table>';
}
else 
{
	print '<meta http-equiv="refresh" content="0; URL=http://users.wpi.edu/~ajamin/APO/"/>';
}

#!End of Body and HTML
print "</body> </html>";
