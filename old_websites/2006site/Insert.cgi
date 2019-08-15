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

print '<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>';
print '<link rel="stylesheet" type="text/css" href="myStyle.css" />';

print '<style type = "text/css">';
print 'h1 {';
print 'text-align: center;';
print 'font-weight: bold;';
print 'font-size: 18 pt;';
print '}';
print '</style>';

$query = ($ENV{"QUERY_STRING"});

@pairs = split(/&/, $query);

$i = 0;
foreach $pair(@pairs){
    ($name, $value) = split(/=/, $pair);

    $value =~ tr/+/ /;
    $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
    $name =~ tr/+/ /;
    $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

    $formHash{$name} = $value;
    $formList[$i] = $value;
	
    $i = $i + 1;    

    }

$username = "ajamin5";
$password = "3dmoTu";

my $dbh = DBI->connect('DBI:mysql:Amanda_Jamin_BSMS;mysql.wpi.edu', $username, $password, { RaiseError => 1, AutoCommit => 1}) or die("No Connect");

my $isUser = $dbh -> prepare("SELECT userLogin FROM user WHERE userLogin = '$formList[0]'");
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
	print "<p><a href=\"http://validator.w3.org/check?uri=referer\"><img src=\"http://www.w3.org/Icons/valid-xhtml10\" alt=\"Valid XHTML 1.0!\" height=\"31\" width=\"88\" /></a>";
}
else
{
	my $InCan = $dbh-> do("INSERT INTO user values ('$formList[0]','$formList[1]', '$formList[2]', '$formList[3]', '$formList[4]')") or die("ERROR 2");
	print '<meta http-equiv="refresh" content="0; URL=http://users.wpi.edu/~ajamin/Webware/BSMS/login.cgi"/></head><body>';
	print "<p><a href=\"http://validator.w3.org/check?uri=referer\"><img src=\"http://www.w3.org/Icons/valid-xhtml10\" alt=\"Valid XHTML 1.0!\" height=\"31\" width=\"88\" /></a>";
}

print "<a href=\"http://jigsaw.w3.org/css-validator/check/referer\"><img src=\"h
ttp://www.w3.org/Icons/valid-css\" alt =\"Valid CSS\" height=\"31\" width=\"88\"
 /></a></p>";	

$dbh -> disconnect();

print '</body></html>';
