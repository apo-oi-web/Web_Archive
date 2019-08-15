#!/usr/bin/perl
#!

use CGI;
use CGI::Carp qw( fatalsToBrowser );
use DBI;
$query = new CGI;
$| = 1;


#! variables to store the user name and password to access the database
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

	#! Store year month day hour and minute submitted by user into the #!corresponding variables
	$year = $formList[4];
	$month = $formList[2];
	$day = $formList[3];
	$index2 = 0;

	$hour = 0;
	if($formList[7] eq 'PM')
	{
	  $hour = 12 + $formList[5];
	}
	else
	{
	  $hour = $formList[5];
	}
	$min = $formList[6];
	$AM = $formList[7];
	$hour2 = $formList[8];
	$min2 = $formList[9];
	$AM2 = $formList[10];

	#!using the above variables create a date string
	$start = $year."-".$month."-".$day." ".$hour.":".$min.":00";
	$end = $year."-".$month."-".$day." ".$hour2.":".$min2.":00";

	#!print "$year $month $day $hour $min $hour2 $min2";


	print "$start is start $end is end";

	#!Insert values submitted by the user into the events table
	my $addEvent = $dbh-> prepare("INSERT INTO EVENTS (Title, Start, End, Description, Type) VALUES ('$formList[1]', '$start', '$end', '$formList[11]', '$formList[12]')");
	$addEvent ->execute();

#!	print "<p><meta http-equiv=\"refresh\" content=\"0; URL=./success.cgi?login=$formList[8]&password=$formList[9]\"></p>";

	#!End of Body and HTML
	print "</body> </html>";
