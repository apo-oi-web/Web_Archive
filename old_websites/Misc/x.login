## Set up shell
stty dec new
umask 0027
mesg y

## Execute busy_signal if logged on via modem
#removed 12/3/97 
#set source=`CCC_source`
#if ((! $?BUSY_SIGNAL) && ($source == "ccc-modems")) then
#  echo -n "Do you wish to execute busy signal (y/n)? "
#  if ($< == "y") then
#   exec busy_signal
#  endif
#endif

## Set up TERM correctly
if (! $?DISPLAY) then
 if ($TERM == "xterm") then
   if ($source == $HOSTNAME) then
     setenv DISPLAY :0.0
   else
     setenv DISPLAY "$source":0.0
     set term=vt100
   endif
 endif
endif

## What to do once logged in
#removed 12/3/97
#if (($HOSTNAME == "bigwpi") || ($HOSTNAME == "wpi") || ($source == "banach")) then
#   clear
#   date +'[1m---------- %A, %B %d %Y ---------------- %r ----------[m'
#   echo ""
#   echo " "
#   frm -s new
#   echo " "
#endif

#echo -n "Please enter your name:"
#echo === $< >> ~/.account.log
if ($OSTYPE == "ultrix") then
  who am i >> ~/.account.log
else
  echo -n "$HOST" >> ~/.account.log
  echo -n '!' >> ~/.account.log
  who -M am i >> ~/.account.log
endif

#cat ~/President/.pres
source .aliases
