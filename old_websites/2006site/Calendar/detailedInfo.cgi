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

	open (IN, "../database") || die "Error: Cannot open file";  #Open the story file, otherwise print error msg

	$username = <IN>;
	$password = <IN>;
	chop($username);
	chop($password);

	close(IN);

	#! $dbh is a variable that will be used to connect to the database Amanda_Jamin_Vote
	my $dbh = DBI->connect('DBI:mysql:APOOI;mysql.wpi.edu', $username, $password, { RaiseError => 1, AutoCommit => 1}) or die("No Connect");


print '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" >
	<head>
	<link rel="stylesheet" type="text/css" href="APO_style.css" />
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
	<meta name="author" content="Amanda Jamin" />
	<meta name="keywords" content="service community faternity alpha phi omega" />
	<meta name="description" content="Website for the WPI chapter of Alpha Phi Omega" />
	<title>Alpha Phi Omega</title>';

#!Start form
print '</head><body class="wpi-apo">';

#!JAVASCRIPT
print "<script language = \"javascript\" type = \"text/javascript\">
	<!--
	function popup(url){
	window.open(url, 'Event Information', 'height = 300, width = 300,resizable=yes');
	if(window.focus){newwindow.focus()}
	return false;
	}
	//--></script>";
	
#! Get variables from url

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

my $thisEvent = $dbh->prepare("SELECT * FROM EVENTS WHERE id = $formList[0]");
$thisEvent -> execute();

while(@events = $thisEvent ->fetchrow_array())
{
 	print "<b>$events[0]</b><br/>";
  	  	@date = split(/-/, $events[1]);
  	  	@day = split(/ /, @date[2]);
  	  	@time = split(/:/, @day[1]);		
		
		@date2 = split(/-/, $events[2]);
		@day2 = split(/ /, @date2[2]);
		@time2 = split(/:/, @day2[1]);

     	        $AMPM = "AM";
     	        $AMPM2 = "AM";

		if(@time[0] > 12)
		{
		   @time[0] = @time[0] - 12;
		   $AMPM = "PM";
		}
		if(@time2[0] > 12)
		{
		   @time2[0] = @time2[0] - 12;
		   $AMPM2 = "PM";
		}

  	  	print " Start: @date[1]/@day[0]/@date[0] @time[0]:@time[1] $AMPM<br/>
  	  	End: @date2[1]/@day2[0]/@date2[0] @time2[0]:@time2[1] $AMPM2<br/>
  	  	$events[3]</li><br/>";   
 }


#!End of Body and HTML
print "</div></body> </html>";
