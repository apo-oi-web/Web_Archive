$savStr = "";

while(<>) {
 if ( /,/ ) {
  chomp;
  $savStr = $savStr . $_;
 } else {
  print $savStr . "\n";
  $savStr = "";
}

}
