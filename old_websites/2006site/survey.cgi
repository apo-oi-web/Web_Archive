#!/usr/local/bin/perl -w

# survey.cgi
# A simple cgi script that will e-mail the results of a survey to 
# apo

use CGI ":standard";

print header();
print "<html>\n";
print " <head>\n";
print "  <title>APO Game Tournament Survey</title>\n";
print "  <meta name=\"author\" content=\"Tim Walsh\" />\n";
print "  <meta name=\"created\" content=\"2/9/06\" />\n";
print "  <meta name=\"modified\" content=\"2/9/06\" />\n";
print " </head>\n";
print " <body>\n";
print "  <p>|<a href = \"./index.cgi\">Alpha Phi Omega</a>| is considering running a video game tournament to help raise money for our service program. Please fill out the survey to help us bring a fun and successful event to campus.</p>";

print "  <form method=\"post\" action=\"http://www.wpi.edu/cgi-bin/webform.pl\">";
print "  <input type=\"hidden\" name=\"email-recipients\" value=\"twalsh\@wpi.edu\" />";
print "  <input type=\"hidden\" name=\"required-fields\" value=\"particapate, pay\" />";
print "  <input type=\"hidden\" name=\"form-dependency1\" value=\"particapate=yes, Madden\" />";
print "  <input type=\"hidden\" name=\"form-dependency2\" value=\"Madden=no, other\" />";
print "  <input type=\"hidden\" name\"form-dependency3\" value=\"Madden=maybe, other\" />";
print "<input type=\"hidden\" name=\"success-redirect\" value=\"http://users.wpi.edu/~apo/index.cgi\">";



print "  <p>Would you participate in a game tournament?\n<br>";
print "  <input type=\"radio\" name=\"particapate\" value=\"no\" /> No\n";
print "  <br />";
print "  <input type=\"radio\" name=\"particapate\" value=\"yes\" /> Yes\n";
print "  <br />";
print "  <input type=\"radio\" name=\"particapate\" value=\"maybe\" /> Maybe\n";
print "  </p>\n";

print "  <p>Would you be interested in playing Madden 06?\n<br />";
print "  <input type=\"radio\" name=\"Madden\" value=\"no\" /> No\n";
print "  <br />";
print "  <input type=\"radio\" name=\"Madden\" value=\"yes\" /> Yes\n";
print "  <br />";
print "  <input type=\"radio\" name=\"Madden\" value=\"maybe\" /> Maybe\n";
print "  </p>\n";

print " <p>How much would you be willing to pay as an enterance fee?<br/>";
print " <input type =\"text\" value = \"\$\" name = \"pay\" />";
print " </p>";

print "  <p>If no, list what games you would perfer to play?<br />";
print "  <textarea name=\"other\" rows=\"5\" cols=\"50\" wrap=\"on\" ></textarea>";
print "  </p>";

print "  <p><input type=\"submit\" /></p>";

print " </body>\n";
print "</html>\n";
