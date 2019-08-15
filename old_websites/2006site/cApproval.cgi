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

open (IN, "database") || die "Error: Cannot open file";  #Open the story file, otherwise print error msg

$username = <IN>;
$password = <IN>;
chop($username);
chop($password);

close(IN);

#! $dbh is a variable that will be used to connect to the database Amanda_Jamin_Vote
my $dbh = DBI->connect('DBI:mysql:APOOI;mysql.wpi.edu', $username, $password, { RaiseError => 1, AutoCommit => 1}) or die("No Connect");

print "Content-type:text/html\n\n";

print "<?xml version='1.0' encoding='UTF-8' standalone='no' ?>\n";

print '<html> <head> <title> Welcome </title>';

print "<body>";

my $InCan = $dbh-> do("UPDATE BROTHERS SET approval = 1 WHERE user = '$formList[0]'");

print "<p><meta http-equiv=\"refresh\" content=\"0; URL=http://users.wpi.edu/~ajamin/APO/adminMenu.cgi\"></p>";

#!End of Body and HTML
print "</body> </html>";
