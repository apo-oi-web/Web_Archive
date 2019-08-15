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

my $dbh = DBI->connect('DBI:mysql:APOOI;mysql.wpi.edu', $username, $password, { RaiseError => 1, AutoCommit => 1}) or die("No Connect");

print "Content-type:text/html\n\n";

print "<?xml version='1.0' encoding='UTF-8' standalone='no' ?>\n";

print "<script type=\"text/JavaScript\">\n";
print "<!--\n";

print "function myfunc(){\n";
print "var objForm=document.forms[\"user\"];";
print "objForm.submit();";
print "}\n";

print "//--></SCRIPT>\n";

print '</head>';

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
  my $InCan = $dbh-> prepare("UPDATE BROTHERS SET password = '$formList[2]' WHERE user = '$formList[0]'");
  
  $InCan -> execute;
    
  print '<body OnLoad="myfunc()">';
  print '<form name = "user" method="POST" action = "brotherLogin.cgi">'; 
  print "<p><input type = \"hidden\" name = \"user\" value=\"$formList[0]\" /> 
  <input type = \"hidden\" name = \"id\" value=\"$formList[1]\" />
  </form></p>";
}

#!End of Body and HTML
print "</body> </html>";
