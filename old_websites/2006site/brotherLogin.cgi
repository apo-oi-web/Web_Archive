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

#! JAVASCRIPT
print '<script type="text/JavaScript">';

print "<!--\n";
print "function validate(url){\n";
print "var objForm=document.forms[\"user\"];";
print "objForm.action=url;";
print "objForm.submit();";
print 	"}//-->\n";
print '</script>';;

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
	my $loginQuery = $dbh -> prepare("SELECT office FROM BROTHERS WHERE user = '$formList[0]'");
	$loginQuery -> execute;

	$i = 0;

	$office = $loginQuery -> fetchrow_array();

	print '</head><body class="wpi-apo">';
	
	
	print '<div class = "container">';
	print '<div class = "navigation">
        	<ul>       
       		<li><a href="./index.cgi">Home</a></li>
       		<li><a href="./rush.cgi">Rush</a></li>
       		<li><a href="./service.cgi">Service</a></li>
       		<li><a href="./fellowship.cgi">Fellowship</a></li>
       		<li><a href="./login.cgi">Login</a></li>	 
       		<li><a href="./Calendar/newCalendar.cgi">Calendar</a></li>
       		<li><a href="./history.html">History</a></li>
       		</ul>
       		<br/>
       		<div align = center>
       		<form action="https://www.paypal.com/cgi-bin/webscr" method="post">
       		<input type="hidden" name="cmd" value="_s-xclick">
       		<input type="image" src="https://www.paypal.com/en_US/i/btn/x-click-but21.gif" border="0" name="submit" alt="Make payments with PayPal">
       		<input type="hidden" name="encrypted" value="-----BEGIN PKCS7-----MIIHNwYJKoZIhvcNAQcEoIIHKDCCByQCAQExggEwMIIBLAIBADCBlDCBjjELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAkNBMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtQYXlQYWwgSW5jLjETMBEGA1UECxQKbGl2ZV9jZXJ0czERMA8GA1UEAxQIbGl2ZV9hcGkxHDAaBgkqhkiG9w0BCQEWDXJlQHBheXBhbC5jb20CAQAwDQYJKoZIhvcNAQEBBQAEgYBIZzaDc4Vi/ikqz7MxqswSbJ8zt4vGSDsOPtl2cY7QIvoFh1QdwrxE+dNLlzT9H93vOB40tu9QmaGCBVESCpucHH+M5VPV1c7uiQ69dlV4fQWax2g7zOwm/2h+CcjvdqgArVd0qnA3yW6EWWShh1ktJOd/qoUBIaFCROjC8D8dWTELMAkGBSsOAwIaBQAwgbQGCSqGSIb3DQEHATAUBggqhkiG9w0DBwQIb/iPNIMQQXuAgZA7njpNcGvfpbfa3W56OA1+H5dQGIMEaXFnty4vVIRF55VcR7DH9nsRELD7H2QFFGL/GsnQ48gF+TsOL0JLAeyInBgRVI8HNmkJ82sliH/M1qJT/ukB2urdiG4eXGaIfcrGOQ6OYAkXUE5FtOu4YYQb6g3tZrZ15z/z+urmx+yotv2VSRXO5R94DaKF84bk6WOgggOHMIIDgzCCAuygAwIBAgIBADANBgkqhkiG9w0BAQUFADCBjjELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAkNBMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtQYXlQYWwgSW5jLjETMBEGA1UECxQKbGl2ZV9jZXJ0czERMA8GA1UEAxQIbGl2ZV9hcGkxHDAaBgkqhkiG9w0BCQEWDXJlQHBheXBhbC5jb20wHhcNMDQwMjEzMTAxMzE1WhcNMzUwMjEzMTAxMzE1WjCBjjELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAkNBMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtQYXlQYWwgSW5jLjETMBEGA1UECxQKbGl2ZV9jZXJ0czERMA8GA1UEAxQIbGl2ZV9hcGkxHDAaBgkqhkiG9w0BCQEWDXJlQHBheXBhbC5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMFHTt38RMxLXJyO2SmS+Ndl72T7oKJ4u4uw+6awntALWh03PewmIJuzbALScsTS4sZoS1fKciBGoh11gIfHzylvkdNe/hJl66/RGqrj5rFb08sAABNTzDTiqqNpJeBsYs/c2aiGozptX2RlnBktH+SUNpAajW724Nv2Wvhif6sFAgMBAAGjge4wgeswHQYDVR0OBBYEFJaffLvGbxe9WT9S1wob7BDWZJRrMIG7BgNVHSMEgbMwgbCAFJaffLvGbxe9WT9S1wob7BDWZJRroYGUpIGRMIGOMQswCQYDVQQGEwJVUzELMAkGA1UECBMCQ0ExFjAUBgNVBAcTDU1vdW50YWluIFZpZXcxFDASBgNVBAoTC1BheVBhbCBJbmMuMRMwEQYDVQQLFApsaXZlX2NlcnRzMREwDwYDVQQDFAhsaXZlX2FwaTEcMBoGCSqGSIb3DQEJARYNcmVAcGF5cGFsLmNvbYIBADAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBBQUAA4GBAIFfOlaagFrl71+jq6OKidbWFSE+Q4FqROvdgIONth+8kSK//Y/4ihuE4Ymvzn5ceE3S/iBSQQMjyvb+s2TWbQYDwcp129OPIbD9epdr4tJOUNiSojw7BHwYRiPh58S1xGlFgHFXwrEBb3dgNbMUa+u4qectsMAXpVHnD9wIyfmHMYIBmjCCAZYCAQEwgZQwgY4xCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJDQTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEUMBIGA1UEChMLUGF5UGFsIEluYy4xEzARBgNVBAsUCmxpdmVfY2VydHMxETAPBgNVBAMUCGxpdmVfYXBpMRwwGgYJKoZIhvcNAQkBFg1yZUBwYXlwYWwuY29tAgEAMAkGBSsOAwIaBQCgXTAYBgkqhkiG9w0BCQMxCwYJKoZIhvcNAQcBMBwGCSqGSIb3DQEJBTEPFw0wNjAyMDIwNTMwNDlaMCMGCSqGSIb3DQEJBDEWBBRkZ/lLkjxY4t3HioRIfhWqgaD4LTANBgkqhkiG9w0BAQEFAASBgEsKrW9Siz4qrQySUxCl3VRA/eh+Dky8+rpepLnCvSPvlrYfqEdmfx+7NinMoFnu98mbTOLEDZ11H9j0Z0g4mYrnoxDKMVu4QWKEFWe5hU59NKP+P2EM0Cb5PgNGGlrX9Pj70ljq5G+eWAdiO3/nOH8xDsUSHJcmM2Va45b28KGD-----END PKCS7-----">
       		</form>
       		</div>
       		</div>';					  	  			
	
	print '<div class = "about" >
		
	       <p class = "bp1">Alpha Phi Omega (APO) is a national co-ed community service fraternity whose mission is to promote service, fellowship, and leadership.  
	       </p>
		</div>';
			
	if($formList[1] eq "1")
	{
		print "<div class = \"inhalt\">
		<form name = \"user\" method=\"POST\">
		<input type = \"hidden\" name = \"user\" value=$formList[0]>
		<input type = \"hidden\" name = \"id\" value=$formList[1]>";
		print '<a href="./Documents/Bylaws.doc"> Bylaws (Word Doc)</a> <br/>
		&nbsp;<br/>
		<input type="Submit" name="findBrother" value="Find a Brother" onclick="validate(\'findBro.cgi\')" /> <br/>
		&nbsp;<br/>
		<input type="Submit" name="changePswd" value="Change Password" onclick="validate(\'cUserPswd.cgi\')" /><br/>
		&nbsp;<br/>
		<input type="Submit" name="changeInfo" value="Update Information" onclick="validate(\'cUserInfo.cgi\')"/><br/>
		&nbsp;<br/>
		<input type="Submit" name="signUp" value="Sign Up for Service" onclick="validate(\'serviceSignUp.cgi\')"/><br/>
		&nbsp;<br/>
		<a href = "http://new.apo.org/show/Supporting_APO/Life_Memberships">Obtain a Lifetime Membership</a><br/>
		&nbsp;<br/>
		Pictures **Page Coming Soon** <br/>
		&nbsp;<br/>
		Pledge Class **Page Coming Soon** <br/>
		&nbsp;<br/>';

		if(($office eq "SVP") || ($office eq "Webmaster") ||($office eq "President") || ($office eq "FVP"))
		{
		print'<input type="Submit" name="addEvent" value="Add an Event" onclick="validate(\'addEvent.cgi\')"> <br/>';
		}
		print '</form>';
		print '</div>';

	 }
	 
	 if($formList[1] eq "2")
	 {
		print "<div class = \"inhalt\">
		<form name = \"user\" method=\"POST\">
		<input type = \"hidden\" name = \"user\" value=$formList[0]>
		<input type = \"hidden\" name = \"id\" value=$formList[1]>";
		print '<input type="Submit" name="findBrother" value="Find a Brother" onclick="validate(\'findBro.cgi\')"> <br/>
		&nbsp;<br/>
		<input type="Submit" name="changePswd" value="Change Password" onclick="validate(\'cUserPswd.cgi\')"><br/>
		&nbsp;<br/>
		<input type="Submit" name="changeInfo" value="Update Information" onclick="validate(\'cUserInfo.cgi\')"><br/>
		&nbsp;<br/>
		<input type="Submit" name="signUp" value="Sign Up for Service" onclick="validate(\'serviceSignUp.cgi\')"><br/>
		&nbsp;<br/>
		<input type="Submit" name="requirements" value="Pledge Requirements" onclick="validate(\'requirements.cgi\')"><br/>
		&nbsp;<br/>
		<a href = "./Documents/pledgemanuel.pdf">Pledge Manuel</a><br/>
		&nbsp;<br/>
		Pictures **Page Coming Soon** <br/>
		&nbsp;<br/>
		</form>';
		print '</div>
		<div class = "pledgePin">
		<img src = "./DesignPics/pinPledge.gif"/>
		</div>';
		

	 }
	 	
	#!End of Body and HTML
	print "</div></body> </html>";
	
				 

}else{
	print "<p><meta http-equiv=\"refresh\" content=\"0; URL=http://users.wpi.edu/~ajamin/APO/login.cgi\"></p>";
}


#!End of Body and HTML
print "<br/>";
print "</p>";
print "</body> </html>";
