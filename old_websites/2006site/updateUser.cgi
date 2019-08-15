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

print '<html> <head> <title> </title>';

print "<script type=\"text/JavaScript\">\n";
print "<!--\n";

print "function myfunc(){\n";
print "var objForm=document.forms[\"user\"];";
print "objForm.submit();";
print "}\n";

print "//--></SCRIPT>\n";

print "</head>";

#!print '<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>';
print '<link rel="stylesheet" type="text/css" href="myStyle.css" />';

print '<style type = "text/css">';
print 'h1 {';
print 'text-align: center;';
print 'font-weight: bold;';
print 'font-size: 18 pt;';
print '}';
print '</style>';


open (IN, "database") || die "Error: Cannot open file"; 

$username = <IN>;
$password = <IN>;
chop($username);
chop($password);

close(IN);

my $dbh = DBI->connect('DBI:mysql:APOOI;mysql.wpi.edu', $username, $password, { RaiseError => 1, AutoCommit => 1}) or die("No Connect");


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
	my $InCan = $dbh-> do("UPDATE BROTHERS SET fname = '$formList[1]', lname = '$formList[2]', 
		email = '$formList[3]', apart = '$formList[4]', phone = '$formList[5]', aim = '$formList[6]' WHERE user = '$formList[0]'") or die("ERROR 2");
	print '<body OnLoad="myfunc()">';
	print '<form name = "user" method="POST" action = "brotherLogin.cgi">'; 
	print "<p><input type = \"hidden\" name = \"user\" value=\"$formList[0]\" /></input>
	<input type = \"hidden\" name = \"id\" value=\"$formList[7]\" /> </p>
	</form>";
}


$dbh -> disconnect();

print '</body></html>';
