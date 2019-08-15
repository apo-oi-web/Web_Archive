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

print '<html> <head> <title> Welcome </title>';

print '<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>';
print '<link rel="stylesheet" type="text/css" href="myStyle.css" />';

print '<style type = "text/css">';
print 'h1 {';
print 'text-align: center;';
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

open (IN, "database") || die "Error: Cannot open file";  #Open the story file, otherwise print error msg

$username = <IN>;
$password = <IN>;
chop($username);
chop($password);

close(IN);

my $dbh = DBI->connect('DBI:mysql:APOOI;mysql.wpi.edu', $username, $password, { RaiseError => 1, AutoCommit => 1}) or die("No Connect");

my $delRes = $dbh-> prepare ("DELETE FROM BROTHERS WHERE user = '$formList[0]'");
$delRes -> execute;

print "<p><meta http-equiv=\"refresh\" content=\"0; URL=http://users.wpi.edu/~ajamin/APO/adminMenu.cgi\"></p>";

#!End of Body and HTML
print "</body> </html>";
