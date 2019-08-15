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
print '<script language = "javascript" type = "text/javascript">';
print	"<!--
	var newwindow;
	function popup(url)
	{
		newwindow=window.open(url,'name','height=400,width=200');
		if (window.focus) {newwindow.focus()}
	}

	//--></script>";

print '<div class = "container">';
print '<div class = "navigation">
       <ul>       
       <li><a href="../index.cgi">Home</a></li>
       <li><a href="../rush.cgi">Rush</a></li>
       <li><a href="../service.cgi">Service</a></li>
       <li><a href="../fellowship.cgi">Fellowship</a></li>
       <li><a href="../login.cgi">Login</a></li>	  			
       <li><a href="./January2006.cgi">Calendar</a></li>
       <li><a href="../history.html">History</a></li>
       </ul></div>';				  	  			

print '<div class = "inhalt">';

	#!get the list of events that belong to the current user and match the date entered 
	
	my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006:01:01 00:00:00.0' AND Start < '2006:02:01 00:00:00.0' ORDER BY Start");
	$thisMon -> execute();
	
	print' <TABLE WIDTH = 800 BORDER=1>
	  	<CAPTION><a href="./April2006.cgi">April</a><font size = 12pt;>May</font></CAPTION>
	  	
	  	<TR><TH WIDTH = 100>Sunday</TH>
	  	<TH WIDTH = 100>Monday</TH>
	  	<TH WIDTH = 100>Tuesday</TH>
	  	<TH WIDTH = 100>Wednesday</TH>
	  	<TH WIDTH = 100>Thursday</TH>
	  	<TH WIDTH = 100>Friday</TH>
		<TH WIDTH = 100>Saturday</TH></TR>
		
		<TR ><TD VALIGN = TOP></TD>
		<TD HEIGHT = 150 VALIGN = TOP>1<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-01 00:00:00.0' AND Start < '2006-05-02 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
		   print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";	         
	        }
	           
		print '</TD>
		<TD VALIGN = TOP>2<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-02 00:00:00.0' AND Start < '2006-05-03 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD VALIGN = TOP>3<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-03 00:00:00.0' AND Start < '2006-05-04 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD VALIGN = TOP>4<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-04 00:00:00.0' AND Start < '2006-05-05 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD VALIGN = TOP>5<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-05 00:00:00.0' AND Start < '2006-05-06 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD VALIGN = TOP>6<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-06 00:00:00.0' AND Start < '2006-05-07 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD></TR>
		<TR><TD HEIGHT = 150  VALIGN = TOP>7<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-07 00:00:00.0' AND Start < '2006-05-08 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		
		<TD HEIGHT = 150  VALIGN = TOP>8<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-08 00:00:00.0' AND Start < '2006-05-09 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD HEIGHT = 150  VALIGN = TOP>9<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-09 00:00:00.0' AND Start < '2006-05-10 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD VALIGN = TOP>10<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-10 00:00:00.0' AND Start < '2006-05-11 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD VALIGN = TOP>11<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-11 00:00:00.0' AND Start < '2006-05-12 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD VALIGN = TOP>12<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-12 00:00:00.0' AND Start < '2006-05-13 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD VALIGN = TOP>13<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-13 00:00:00.0' AND Start < '2006-05-14 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD></TR>
		<TR><TD HEIGHT = 150  VALIGN = TOP>14<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-14 00:00:00.0' AND Start < '2006-05-15 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		
		<TD  VALIGN = TOP HEIGHT = 150>15<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-15 00:00:00.0' AND Start < '2006-05-16 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD HEIGHT = 150  VALIGN = TOP>16<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-16 00:00:00.0' AND Start < '2006-05-17 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD VALIGN = TOP>17<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-17 00:00:00.0' AND Start < '2006-05-18 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD VALIGN = TOP>18<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-18 00:00:00.0' AND Start < '2006-05-19 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD VALIGN = TOP>19<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-19 00:00:00.0' AND Start < '2006-05-20 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD VALIGN = TOP>20<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-20 00:00:00.0' AND Start < '2006-05-21 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "$month[0]</div><br/>";
	         }
	           
		print '</TD></TR>
		<TR><TD HEIGHT = 150  VALIGN = TOP>21<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-21 00:00:00.0' AND Start < '2006-05-22 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		
		<TD HEIGHT = 150  VALIGN = TOP>22<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-22 00:00:00.0' AND Start < '2006-05-23 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD VALIGN = TOP>23<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-23 00:00:00.0' AND Start < '2006-05-24 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD VALIGN = TOP>24<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-24 00:00:00.0' AND Start < '2006-05-25 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD VALIGN = TOP>25<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-25 00:00:00.0' AND Start < '2006-05-26 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD VALIGN = TOP>26<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-26 00:00:00.0' AND Start < '2006-05-27 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD VALIGN = TOP>27<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-27 00:00:00.0' AND Start < '2006-05-28 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD></TR>
		<TR><TD HEIGHT = 150  VALIGN = TOP>28<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-28 00:00:00.0' AND Start < '2006-05-29 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		
		<TD VALIGN = TOP HEIGHT = 150>29<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-29 00:00:00.0' AND Start < '2006-05-30 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD VALIGN = TOP>30<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-30 00:00:00.0' AND Start < '2006-05-31 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD VALIGN = TOP>31<br/>';
		my $thisMon = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '2006-05-31 00:00:00.0' AND Start < '2006-02-01 00:00:00.0' ORDER BY Start");
		$thisMon -> execute();
		while(@month = $thisMon ->fetchrow_array())
		{
				
		   if ($month[5] eq "Rush")
		   {
		     print'<div class = "rushEvent">';
		   } 
		   if ($month[5] eq "Service")
		   {
   		     print'<div class = "serviceEvent">';   
		   }
		   if ($month[5] eq "Fellowship")
		   {
  		     print'<div class = "fellowshipEvent">'; 
		   }
				    
		   #!Print the title, description and date with time
	           print "<a  href = \"javascript:popup('detailedInfo.cgi?=$month[4]')\">
	           $month[0]</a></div><br/>";
	         }
	           
		print '</TD>
		<TD VALIGN = TOP></TD>
		<TD VALIGN = TOP></TD>
		<TD VALIGN = TOP></TD></TR>


	  	
	</TABLE>';
	
  	print '</div>';

#!End of Body and HTML
print "</div></body> </html>";
