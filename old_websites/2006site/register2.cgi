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

print '<html> <head> <title> Vote NOW!! </title>';

#!print '<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>';
print '<link rel="stylesheet" type="text/css" href="myStyle.css" />';

print '<style type = "text/css">';
print 'h1 {';
print 'text-align: center;';
print 'font-weight: bold;';
print 'font-size: 18 pt;';
print '}';
print '</style>';


open (IN, "database") || die "Error: Cannot open file";  #Open the story file, otherwise print error msg

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


my $isUser = $dbh -> prepare("SELECT user FROM BROTHERS WHERE user = '$formList[6]'");

$isUser -> execute;
$i = 0;

if (@exist = $isUser -> fetchrow_array())
{
	$i = $i + 1;
}

if ($i != 0)
{
	print '<meta http-equiv="refresh" content="5; URL=http://users.wpi.edu/~ajamin/Webware/BSMS/register.cgi"/></head><body>';
	print "<h1><br/>User login already exists.  Please try again.</h1>";
	print '<meta http-equiv="refresh" content="5; URL=http://users.wpi.edu/~ajamin/APO/Register.cgi"/></head><body>';
}
else
{
	my $InCan = $dbh-> do("INSERT INTO BROTHERS (fname, lname, email, apart, phone, aim, user, password) values ('$formList[0]', '$formList[1]', '$formList[2]', '$formList[3]', '$formList[4]', '$formList[5]', '$formList[6]', '$formList[7]')") or die("ERROR 2");
	print '<meta http-equiv="refresh" content="0; URL=http://users.wpi.edu/~ajamin/APO/"/></head><body>';
}


$dbh -> disconnect();

print '</body></html>';
