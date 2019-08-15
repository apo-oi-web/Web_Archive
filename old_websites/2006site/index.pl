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

print '<div class = "container">';
print '<div class = "navigation">
       <ul>       
       <li><a href="./index.cgi" title = "The home page of APO-OI" tabindex="1">Home</a></li>
       <li><a href="./rush.cgi" title = "Access information regarding rushing the faternity" tabindex="2">Rush</a></li>
       <li><a href="./service.cgi" title = "Information regarding our service program" tabindex="3">Service</a></li>
       <li><a href="./fellowship.cgi" title = "Information regarding our fellowship events" tabindex="4">Fellowship</a></li>
       <li><a href="./login.cgi" tile = "Brothers and Pledges log in for more information" tabindex="5">Login</a></li>	 
       <li><a href="./Calendar/February2006.cgi" title = "A Calendar of our events" tabindex="6">Calendar</a></li>
       <li><a href="./history.html" tile = "A history of our faternity" tabindex="7">History</a></li>
       </ul>
       <br/>
       <div align = center>
       <form action="https://www.paypal.com/cgi-bin/webscr" method="post">
       <input type="hidden" name="cmd" value="_s-xclick">
       <input type="image" src="https://www.paypal.com/en_US/i/btn/x-click-but21.gif" border="0" name="submit" alt="Make payments with PayPal" tabindex="8">
       <input type="hidden" name="encrypted" value="-----BEGIN PKCS7-----MIIHNwYJKoZIhvcNAQcEoIIHKDCCByQCAQExggEwMIIBLAIBADCBlDCBjjELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAkNBMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtQYXlQYWwgSW5jLjETMBEGA1UECxQKbGl2ZV9jZXJ0czERMA8GA1UEAxQIbGl2ZV9hcGkxHDAaBgkqhkiG9w0BCQEWDXJlQHBheXBhbC5jb20CAQAwDQYJKoZIhvcNAQEBBQAEgYBIZzaDc4Vi/ikqz7MxqswSbJ8zt4vGSDsOPtl2cY7QIvoFh1QdwrxE+dNLlzT9H93vOB40tu9QmaGCBVESCpucHH+M5VPV1c7uiQ69dlV4fQWax2g7zOwm/2h+CcjvdqgArVd0qnA3yW6EWWShh1ktJOd/qoUBIaFCROjC8D8dWTELMAkGBSsOAwIaBQAwgbQGCSqGSIb3DQEHATAUBggqhkiG9w0DBwQIb/iPNIMQQXuAgZA7njpNcGvfpbfa3W56OA1+H5dQGIMEaXFnty4vVIRF55VcR7DH9nsRELD7H2QFFGL/GsnQ48gF+TsOL0JLAeyInBgRVI8HNmkJ82sliH/M1qJT/ukB2urdiG4eXGaIfcrGOQ6OYAkXUE5FtOu4YYQb6g3tZrZ15z/z+urmx+yotv2VSRXO5R94DaKF84bk6WOgggOHMIIDgzCCAuygAwIBAgIBADANBgkqhkiG9w0BAQUFADCBjjELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAkNBMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtQYXlQYWwgSW5jLjETMBEGA1UECxQKbGl2ZV9jZXJ0czERMA8GA1UEAxQIbGl2ZV9hcGkxHDAaBgkqhkiG9w0BCQEWDXJlQHBheXBhbC5jb20wHhcNMDQwMjEzMTAxMzE1WhcNMzUwMjEzMTAxMzE1WjCBjjELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAkNBMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtQYXlQYWwgSW5jLjETMBEGA1UECxQKbGl2ZV9jZXJ0czERMA8GA1UEAxQIbGl2ZV9hcGkxHDAaBgkqhkiG9w0BCQEWDXJlQHBheXBhbC5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMFHTt38RMxLXJyO2SmS+Ndl72T7oKJ4u4uw+6awntALWh03PewmIJuzbALScsTS4sZoS1fKciBGoh11gIfHzylvkdNe/hJl66/RGqrj5rFb08sAABNTzDTiqqNpJeBsYs/c2aiGozptX2RlnBktH+SUNpAajW724Nv2Wvhif6sFAgMBAAGjge4wgeswHQYDVR0OBBYEFJaffLvGbxe9WT9S1wob7BDWZJRrMIG7BgNVHSMEgbMwgbCAFJaffLvGbxe9WT9S1wob7BDWZJRroYGUpIGRMIGOMQswCQYDVQQGEwJVUzELMAkGA1UECBMCQ0ExFjAUBgNVBAcTDU1vdW50YWluIFZpZXcxFDASBgNVBAoTC1BheVBhbCBJbmMuMRMwEQYDVQQLFApsaXZlX2NlcnRzMREwDwYDVQQDFAhsaXZlX2FwaTEcMBoGCSqGSIb3DQEJARYNcmVAcGF5cGFsLmNvbYIBADAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBBQUAA4GBAIFfOlaagFrl71+jq6OKidbWFSE+Q4FqROvdgIONth+8kSK//Y/4ihuE4Ymvzn5ceE3S/iBSQQMjyvb+s2TWbQYDwcp129OPIbD9epdr4tJOUNiSojw7BHwYRiPh58S1xGlFgHFXwrEBb3dgNbMUa+u4qectsMAXpVHnD9wIyfmHMYIBmjCCAZYCAQEwgZQwgY4xCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJDQTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEUMBIGA1UEChMLUGF5UGFsIEluYy4xEzARBgNVBAsUCmxpdmVfY2VydHMxETAPBgNVBAMUCGxpdmVfYXBpMRwwGgYJKoZIhvcNAQkBFg1yZUBwYXlwYWwuY29tAgEAMAkGBSsOAwIaBQCgXTAYBgkqhkiG9w0BCQMxCwYJKoZIhvcNAQcBMBwGCSqGSIb3DQEJBTEPFw0wNjAyMDIwNTMwNDlaMCMGCSqGSIb3DQEJBDEWBBRkZ/lLkjxY4t3HioRIfhWqgaD4LTANBgkqhkiG9w0BAQEFAASBgEsKrW9Siz4qrQySUxCl3VRA/eh+Dky8+rpepLnCvSPvlrYfqEdmfx+7NinMoFnu98mbTOLEDZ11H9j0Z0g4mYrnoxDKMVu4QWKEFWe5hU59NKP+P2EM0Cb5PgNGGlrX9Pj70ljq5G+eWAdiO3/nOH8xDsUSHJcmM2Va45b28KGD-----END PKCS7-----">
       </form>
       </div>
       </div>';				  	  			

print '<div class = "about" >
	
       <p class = "bp1">
       <div align = "center">
       Omicorn Iota <br/>
       |<a href = "http://www.apor1.org/" title = "APO Region 1 Website" tabindex="9">Region I</a>| <br/> |<a href = "http://www.apo96.org/" title = "APO Section 96 Website" tabindex="10">Section 96</a>|
       </div>
       <br/>
       Alpha Phi Omega (APO) is a national co-ed community service fraternity whose mission is to promote service, fellowship, and leadership.
       </p></div>';


print '<div class = "inhalt" style = "overflow: auto;">

	<h2><span class = "indexTitle">Who Are We?</span></h2>
		
		<p class = "bp2">
		Alpha Phi Omega Omicorn Iota is the chapter of [<a href ="http://www.apo.org" title = "APO National Website" tabindex="11">Alpha Phi Omega</a>] on the campus of [<a href = "http://www.wpi.edu" title = "WPI Website" tabindex="12">Worcester Polytechnic Institute.</a>]  We have been continueously active at <ACRONYM title="Worcester Polytechnic Institute" tabindex="13">WPI</ACRONYM> since 1964.  
		</p>
		
		<p class = "bp3">  Primarily <ACRONYM title="Alpha Phi Omega">APO</ACRONYM> is a service faternity.  Each brother is required to complete several hours of community service a term.  Past projects have included visiting the [<a href="http://www.cancer.org/docroot/COM/content/div_NE/COM_5_1x_Worcester_MA_Hope_Lodge_Provides_Home_Away_from_Home_for_Those_Facing_Cancer.asp" title = "Hope Lodge Worcester" tabindex="14">Hope Lodge</a>], cooking at the [<a href="http://www.massveterans.org/index.htm" title = "Worcester Veterns Shelter" tabindex="15">Worcester Veterans Shelter</a>], entertaining the residents of the [<a href="http://www.whyme.org/" title = "Why Me Website" tabindex="16">Sherrys House</a>], as well as several events at the People in Peril Shelter.  In addition, APO puts on five annual service projects;  Freshman Move-in day, the APO Service Auction, the APO Homeless Sleepout, the Ugly Man on  Campus competition, and the Service to Students Award.</p>
	
		<p class = "bp4">
	 	However, APO is not solely about service.  APO strongly believes in fostering fellowship between its members.  Weekly after meetings brothers visit the Bean Counter.  In addition, [<a href="http://www.foodnetwork.com/food/show_ic" title = "Iron Chef Website" tabindex="17">Iron Chef</a>] competitions  are held yearly as are Assassins games.   
	  	</p>
	
	  	<p class = "bp5">
	  	Our meetings are held in Higgins Labs 218 Thurdays, starting at 6:30 pm.  Our office is located on the third floor of Olin.
		To contact our chapter through email, please email apo-exec at wpi.edu.  We can also be reached via the US postal service at 
	  	<div align = "center"> Alpha Phi Omega c/o SAO Office <br/> 
	  	100 Institute Road <br/>
	  	Worcester, MA 01609 <br/></div>
	  	</p>
	  	
	  	<div class = "Foot">
	  	<br/>
		National Disclaimer: This electronic document is intended for public viewing and is solely for personal reference. It should not be considered an authoritative source nor an official publication of Alpha Phi Omega. Inquiries regarding Alpha Phi Omega and its official publications may be directed to: Alpha Phi Omega, 14901 E. 42nd Street, Independence, MO, 64055 - USA. "Alpha Phi Omega" is copyrighted, registered trademark in the USA. All rights reserved.
		</div>
		
		<p align = "center">|<a href = "http://www.apo.org" title = "APO National Website" tabindex="18">APO National Site</a>|</p>
	</div>';
       
#!End of Body and HTML
print "</div></body> </html>";
