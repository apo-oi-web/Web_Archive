#!/usr/bin/perl
#!

use CGI;
use CGI::Carp qw( fatalsToBrowser );
use DBI;
$query = new CGI;
$| = 1;


#! variables to store the user name and password to access the database
	open (IN, "../database") || die "Error: Cannot open file";  #Open the story file, otherwise print error msg

	$username = <IN>;
	$password = <IN>;
	chop($username);
	chop($password);

	close(IN);

	#! $dbh is a variable that will be used to connect to the database Amanda_Jamin_Vote
	my $dbh = DBI->connect('DBI:mysql:APOOI;mysql.wpi.edu', $username, $password, { RaiseError => 1, AutoCommit => 1}) or die("No Connect");

	
	print "Content-type:text/html\n\n";

	print "<?xml version='1.0' encoding='UTF-8' standalone='no' ?>\n";

	print '<LINK rel="stylesheet" type="text/css" href="AuctionStyle.css" />';
	
	print '<html> <head> <title> Welcome </title> </head>';

	print "<body>";

	$query=CGI->new;
	@params = $query->param;
	
	$index = 0;
	foreach my $paramKey (@params) {
		$inputdata = $query->param($paramKey);
		$formList[$index] = $inputdata;
		$index = $index + 1;
	}

	$fname = $formList[0];
	$lname = $formList[1];
	$email = $formList[2];
	$box =  $formList[3];
	$phone = $formList[4];
	$serviceName = $formList[5];
	$serviceHours = $formList[6];
	$desc = $formList[7];
	$notes = $formList[8];

	#!Insert values submitted by the user into the events table
	my $addService = $dbh-> prepare("INSERT INTO ServiceAuction (FirstName, LastName, Box, Phone, Email, ServiceName, Hours, Description, Notes) VALUES ('$fname', '$lname', '$box', '$phone', '$email', '$serviceName', '$serviceHours', '$desc', '$notes')");
	$addService ->execute();

	$reply_to = "apo-service@wpi.edu";
	$subject  = "Confirmation of your service donation";
	$content  = "You have donated the following service to the Alpha Phi Omega service auction: \n 
			$serviceName \n
			Number of Hours: $serviceHours \n
			$desc \n
			$notes \n
			Thank you for your donation.  If you have any questions please email apo-service@wpi.edu";



#! DISPLAYED PAGE

	print  '<div class = "header">
   		<img src="images/logorightblank.gif" width = "238" height = "74" align = right>
   		<div class = "logo" align=middle> <h1>Alpha Phi Omega</h1> </div>
		<div class = "auction"> Service Auction  </div>
		</div>

		<div class = "content">
		<p> 
		  <h3> Thank you for participating in the Alpha Phi Omega Service Auction. </br> 
		       For more information on our faternity visit http://users.wpi.edu/~apo/ </br>
		       and please attend the auction on November 21st. 
		  </h3>';

	print	  '<form method="Post" action="/cgi-bin/webform.pl" id="emailUser">';
	print		"<input type=\"hidden\" name=\"email-recipients\" value=\"$email\">
			<input type=\"hidden\" name=\"email-subject\" value=\"$subject\">
			<input type=\"hidden\" name=\"form-name\" value=\"$content\">
			<input type=\"hidden\" name=\"success-redirect\" value=\"index.html\">
			<input type=\"hidden\" name=\"failure-redirect\" value=\"index.html\">
		  </form>";
		  
	print	  '<script language="JavaScript" type="text/javascript">
		  <!--
			document.getElementById(\'emailUser\').submit();
		  //-->
		  </script>
		
		</p>
		</div>';

	print	'<div class = "navigationTop">
		</div>
	
		<div class = "navigation">
		</div>
	
		<div class = "footer">
		</div>';

	print '</body> </html>';
