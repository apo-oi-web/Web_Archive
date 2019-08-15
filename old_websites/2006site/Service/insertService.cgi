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

	$serviceName =~ s/'/ /g;
	$serviceName =~ s/"/ /g;
	$desc =~ s/'/ /g;
	$desc =~ s/"/ /g;
	$notes =~ s/'/ /g;
	$notes =~ s/"/ /g;

	# Insert values submitted by the user into the events table
	my $addService = $dbh-> prepare("INSERT INTO ServiceAuction (FirstName, LastName, Box, Phone, Email, ServiceName, Hours, Description, Notes) VALUES ('$fname', '$lname', '$box', '$phone', '$email', '$serviceName', '$serviceHours', '$desc', '$notes')");
	$addService ->execute();


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
		       and please attend the auction on November 27st. 
		  </h3>
		</p>
		</div>

		<div class = "navigationTop">
		</div>
	
		<div class = "navigation">
		</div>
	
		<div class = "footer">
		</div>';

	print '<META HTTP-EQUIV="Refresh" CONTENT="10; URL=index.html">';
	print "</body> </html>";
