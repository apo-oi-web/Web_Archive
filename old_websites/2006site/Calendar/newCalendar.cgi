#! /usr/bin/perl
######################################################################
# Basic Calendar                          Version 1.01               #
# Copyright 1999 Frederic TYNDIUK (FTLS)  All Rights Reserved.       #
# E-Mail: tyndiuk@ftls.org                Script License: GPL        #
# Created  05/30/99                       Last Modified 07/15/99     #
# Scripts Archive at:                     http://www.ftls.org/cgi/   #
######################################################################
# Function :                                                         #
# calentar.cgi : print calendar of current month...                  #
# calendar.cgi?MM-YYYY : print calendar of the MM-YYYY (01-2000)     #
# You can use this Script as SSI (Server Side Include) or Not, whith #
# $SSI var.                                                          #
# Your can chose size of tabe border with $Border = Size             #
######################################################################
##################### license & copyright header #####################
#                                                                    #
#                 Copyright (c) 1999 TYNDIUK Frederic                #
#                                                                    #
#  This program is free software; you can redistribute it and/or     #
#  modify it under the terms of the GNU General Public License as    #
#  published by the Free Software Foundation; either version 2 of    #
#  the License, or (at your option) any later version.               #
#                                                                    #
#  This program is distributed in the hope that it will be useful,   #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of    #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the     #
#  GNU General Public License for more details.                      #
#                                                                    #
#  You should have received a copy of the GNU General Public License #
#  along with this program in the file 'COPYING'; if not, write to   #
#  the Free Software Foundation, Inc., 59 Temple Place - Suite 330,  #
#  Boston, MA 02111-1307, USA, or contact the author:                #
#                                                                    #
#                              TYNDIUK Frederic <tyndiuk@ftls.org>   #
#                                       <http://www.ftls.org/>       #
#                                                                    #
################### end license & copyright header ###################
######################################################################

use CGI;
use CGI::Carp qw( fatalsToBrowser );
use DBI;
use Switch;

$query = new CGI;
$| = 1;

# Necessary Variables:                                               #
# The following variables should be set to define the locations      #
# and URLs of various files, as explained in the documentation.      #

	$CalCMD = "/usr/bin/cal";  # En: PATH of cal.
	                           # Fr: Chemin de cal.

	$Days = "Su Mo Tu We Th Fr Sa";  # En: Days
	#$Days = "Di Lu Ma Me Je Ve Sa"; # Fr: Jours en Francais


#!Print basic XHTML information
print "Content-type:text/html\n\n";

print "<?xml version='1.0' encoding='UTF-8' standalone='no' ?>\n";

print '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">';


#! Connect to apo database
open (IN, "../database") || die "Error: Cannot open file";  

$username = <IN>;
$password = <IN>;
chop($username);
chop($password);

close(IN);

#! $dbh is the varible used to connect to the database
my $dbh = DBI->connect('DBI:mysql:APOOI;mysql.wpi.edu', $username, $password, { RaiseError => 1, AutoCommit => 1}) or die("No Connect");

#! Basic html meta data
print '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" >
        <head>
        <link rel="stylesheet" type="text/css" href="APO_style.css" />
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
        <meta name="author" content="Amanda Jamin" />
        <meta name="keywords" content="service community faternity alpha phi omega" />
        <meta name="description" content="Website for the WPI chapter of Alpha Phi Omega" />
        <title>Alpha Phi Omega</title>';

#! Javascript to determine event information
print '<script language = "javascript" type = "text/javascript">';
print   "<!--
        var newwindow;
        function popup(url)
        {
                newwindow=window.open(url,'name','height=400,width=200');
                if (window.focus) {newwindow.focus()}
        }

        //--></script>";

#!Start html body
print '</head><body class="wpi-apo">';

print '<div class = "container">';
print '<div class = "navigation">
       <ul>
       <li><a href="../index.cgi">Home</a></li>
       <li><a href="../rush.cgi">Rush</a></li>
       <li><a href="../service.cgi">Service</a></li>
       <li><a href="../fellowship.cgi">Fellowship</a></li>
       <li><a href="../login.cgi">Login</a></li>
       <li><a href="./newCalendar.cgi">Calendar</a></li>
       <li><a href="../history.html">History</a></li>
       </ul></div>';

print '<div class = "inhalt">';

######################################################################

$Query_String = $ENV{QUERY_STRING};
$Query_String =~ s/%([0-9A-F][0-9A-F])/pack("C",oct("0x$1"))/ge;
$Query_String =~ tr/+/ /;

print &RetCal($CalCMD, $Query_String);
print "</div></body></html>";

# En: Sub routine return calendar.
sub RetCal {
	my($CalCMD, $Args, $Border) = @_;
	my($ret, @Result, $Month, $dy, $line, $no);
	
	if ( -x "$CalCMD" ) {

		if (($Args !~ /^\d\d?-\d\d\d\d$/) || ($Args eq "")) {
			$Args = "";
			@date = localtime(time); 
			$Today = $date[3];
		} else {
			$Args =~ s/-/ /g;
		}

		$numYear = $date[5] + 1900;	

		open(CAL, "$CalCMD $Args|");
		@Result = <CAL>;
		close(CAL);

		$Month = $Result[0]; shift(@Result);
                $Month =~ s/\s\s\s*//g;

		@stringMonth = split(/ /, $Month);
                $stringMonth = @stringMonth[0];
		
		$numMonth = '00';
		$previousMonth = "";
		$nextMonth = "";
		switch($stringMonth){
                        case "January" {$numMonth = '01'}
                        case "February" {$numMonth = '02'}
                        case "March" {$numMonth = '03'}
                        case "April" {$numMonth = '04'}
                        case "May" {$numMonth = '05'}
                        case "June" {$numMonth = '06'}
                        case "July" {$numMonth = '07'}
                        case "August" {$numMonth = '08'}
                        case "September" {$numMonth = '09'}
                        case "October" {$numMonth = '10'}
                        case "November" {$numMonth = '11'}
                        case "December" {$numMonth = '12'}
                }

		switch($stringMonth){
                        case "January"{$previousMonth = "December"}
                        case "February" {$previousMonth = "January"}
                        case "March" {$previousMonth = "February"}
                        case "April" {$previousMonth = "March"}
                        case "May" {$previousMonth = "April"}
                        case "June" {$previousMonth = "May"}
                        case "July" {$previousMonth = "June"}
                        case "August" {$previousMonth = "July"}
                        case "September" {$previousMonth = "August"}
                        case "October" {$previousMonth = "September"}
                        case "November" {$previousMonth = "October"}
                        case "December" {$previousMonth = "November"}
                }

		switch($stringMonth){
                        case "January" {$nextMonth = "February"}
                        case "February" {$nextMonth = "March"}
                        case "March" {$nextMonth = "April"}
                        case "April" {$nextMonth = "May"}
                        case "May" {$nextMonth = "June"}
                        case "June" {$nextMonth = "July"}
                        case "July" {$nextMonth = "August"}
                        case "August" {$nextMonth = "September"}
                        case "September" {$nextMonth = "October"}
                        case "October" {$nextMonth = "November"}
                        case "November" {$nextMonth = "December"}
                        case "December" {$nextMonth = "January"}
                }

		$ret = "<TABLE><CAPTION ALIGN=\"CENTER\">$previousMonth <font size = 12pt;><B>$Month</B></font> $nextMonth</CAPTION>\n<TR>";
		
		shift(@Result);

		#! Prints Sunday Monday....Saturday
		foreach $dy (split(/ /, $Days)) {
			$ret .= "<TH WIDTH = 100>$dy</TH>";
		}
		$ret .= "</TR>\n";

		foreach $line (@Result) {
			$line =~ s/\n//;
			$line =~ s/   /ccs/g;
			$line =~ s/  /sc/g;
			$line =~ s/ /s/g;
			$line =~ s/^s//g;
			$line =~ s/ss/s/g;
			$line =~ s/c//g;
			$ret .= "<TR>";
			
			foreach $no (split(/s/, $line)){
				if($no)
				{
					$tomorrow = $no+1;
					$startTime = $numYear."-".$numMonth."-".$no." 00:00:00.0";
                			$endTime = $numYear."-".$numMonth."-".$tomorrow." 00:00:00.0";
				}
				if ($no == $Today) {
					$ret .= "<TD HEIGHT = 150 VALIGN = TOP><BLINK><B>$no</B></BLINK><br/>";
				} else {
					$ret .= "<TD HEIGHT = 150 VALIGN = TOP>$no<br/>";
				}
				
				if($no)
				{
					my $todaysEvents = $dbh->prepare("SELECT * FROM EVENTS WHERE Start > '$startTime' AND Start < '$endTime' ORDER BY Start");
                		
					$todaysEvents -> execute();
					
	
					while(@event = $todaysEvents ->fetchrow_array())
                			{

			                   if ($event[5] eq "Rush")
        	        		   {
			                     $ret .= '<div class = "rushEvent">';
                			   }
		                	   if ($event[5] eq "Service")
                		   	   {
		                     		$ret .= '<div class = "serviceEvent">';
                		   	   }
		                   	   if ($event[5] eq "Fellowship")
                		   	   {
		                     		$ret .= '<div class = "fellowshipEvent">';
                		   	   }

		                   	   #!Print the title, description and date with time
                		   	   $ret .= "<a  href = \"javascript:popup('detailedInfo.cgi?=$event[4]')\"> 
					   $event[0]</a></div><br/>";   

					}
				}
				$ret .= "</TD>";
			}
			
			$ret .= "</TR>\n";
		}
		$ret .= "</TABLE></div>\n";
	} else {
		$ret = "Cannot find cal on this system.";
	}
	return $ret;
}

