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

print '<html> <head> <title> Welcome </title>';

print "<script type=\"text/JavaScript\">\n";
print "<!--\n";

print "function myfunc(){\n";
print "var objForm=document.forms[\"user\"];";
print "objForm.submit();";
print "}\n";

print "//--></SCRIPT>\n";

print '<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>';
print '<link rel="stylesheet" type="text/css" href="APO_style.css" />';

#! variables to store the user name and password to access the database
open (IN, "database") || die "Error: Cannot open file";  #Open the story file, otherwise print error msg

$username = <IN>;
$password = <IN>;
chop($username);
chop($password);

close(IN);

#! $dbh is a variable that will be used to connect to the database Amanda_Jamin_Vote
my $dbh = DBI->connect('DBI:mysql:APOOI;mysql.wpi.edu', $username, $password, { RaiseError => 1, AutoCommit => 1}) or die("No Connect");

#! Get variables from url
$query=CGI->new;
@params = $query->param;

$index = 0;
foreach my $paramKey (@params) {
	$inputdata = $query->param($paramKey);
	$formList[$index] = $inputdata;
	$index = $index + 1;
	}
	
#! get username and password for the current login
my $loginQuery = $dbh -> prepare("SELECT password FROM BROTHERS WHERE user = '$formList[0]'");
$loginQuery -> execute;

$i = 0;

if(@checkPSWD = $loginQuery -> fetchrow_array())
{
	$i = $i + 1;
}

#!If the query did not return anything --> print error message
if ($i == 0)
{
	print "<meta http-equiv=\"refresh\" content=\"5; URL=./login.cgi\"> </head><body>
	<div class = \"inhalt\">
	<p> User does not exist.  If you are trying to register for $formList[0] then <a href=\"./Register.cgi\" title = \"Register for a Brother Account\" tabstop = \"1\">Register here.</a> 
	</p></div>";
        
}
#!If the query returned results
else 
{

#!Check the password 
#!If they dont match print error message and return to login

	if ($formList[1] ne @checkPSWD[0])
	{
		print '<meta http-equiv="refresh" content="1; URL=./login.cgi"></head><body>
		<div class = "inhalt">
		<p>User Name and Password do not match.  Please Try again.</p></div>';
	}
#!If the password and login match
	else 
	{
	
		if ($formList[0] eq "admin")
		{
		print '<meta http-equiv="refresh" content="0; URL=./adminMenu.cgi"></head><body>';
		}
		
		#!otherwise print user options
		else
		{
			my $approveQuery = $dbh -> prepare("SELECT approval FROM BROTHERS WHERE user = '$formList[0]'");
			$approveQuery -> execute;
			
			$i = 0;
			
			if(@approvePSWD = $approveQuery -> fetchrow_array())
			{
				$i = $i + 1;
			}


			if (@approvePSWD[0] eq "0")
			{
			print '</head><body><div class = "inhalt"><p>Sorry, but your user account has not yet been approved by the Webmaster.  Please try again later.</p>';
			print '<p><meta http-equiv="refresh" content="2"; URL="./login.cgi"></p></div>';
						
			}
			elsif(@approvePSWD[0] eq "1")
			{
				print '<body OnLoad="myfunc()">';
				print '<form name = "user" method="POST" action = "./brotherLogin.cgi">'; 
				print "<p><input type = \"hidden\" name = \"user\" value=\"$formList[0]\">
				<input type = \"hidden\" name = \"id\" value=1></p> </form>";
			
			}
			else
			{
				print '<body OnLoad="myfunc()">';
				print '<form name = "user" method="POST" action = "./brotherLogin.cgi">'; 
				print "<p><input type = \"hidden\" name = \"user\" value=\"$formList[0]\">
				<input type = \"hidden\" name = \"id\" value=2></p> </form>";
			}
		}

	}

}


print '</body></html>';
 
