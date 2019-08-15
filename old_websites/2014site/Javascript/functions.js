/*
* n	Your email username (ex. johnsmith)
* dn	Your domain name (ex. wpi)
* d	Your domain (ex. edu)
* id	The tag id to assign the address to
*/
function mailScrambler(dn, n, id, d){
	var part1 = n + '@' + dn;
	var part2 = part1 + '.' + d;
	window.document.getElementById(id).href = "mailto:" + part2;
	
	return false;
}

function ieFix(){
	if(navigator.appName == "Microsoft Internet Explorer"){
		window.document.getElementById('contentPane').style.width = '685px';	
	}

	return false;
}

// Calls all functions needed to complete web page.
function setupRun(){
	ieFix(); // DON'T EVER TOUCH THIS LINE!!
	
	/* 
	** This line is for creating mailto links. Use it as a template.
	** Arguments are: server, username, link ID, domain 
	** link ID links this email address to the link location in HTML
	** Make sure the web chair explains this to new web chairs!
	*/
	mailScrambler('wpi', 'apo-w', 'webchairMail', 'edu');
	return false;
}