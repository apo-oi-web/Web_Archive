/**
 * @author Colin Ogren
 * Retrieves the photos with the access token
 * If the structure is empty, an error writes to the console and the old slideshow is used instead.
 * The console has a facebook login button to access permissions. Upon receiving an access token, it prints to console.
 * 
 */
/*
 * Bug Report:
 * 1. App seems to pull only 25 photos from Facebook, ever. 
 */


// MAJOR GLOBALS

var fbPhotos = [];
var bannedPhotos = []; // true = banned for that position/index
var resultsPerPage = 20;
var pi = 0; // index of first photo; this will = resultsPerPage * page#
var currentID = 0; // index of currently viewed photo
var TableProps = function(){
	this.tableWidth = 640;
	this.tableBorder = 0;
	this.cellBorder = 0;
	this.borderSpacing = 0;
	this.padding = 5;
	this.imageWidth = 180; // photos.data[0].images[x].width; x varies depending on original size
	this.cellsPerRow = (this.tableWidth - (2 * this.tableBorder + this.borderSpacing))/(2 * (this.cellBorder + this.borderSpacing + this.imageWidth + this.padding));
};
var tableProperties = new TableProps();

// END MAJOR GLOBALS

// BANNED PHOTOS
// !!!index is one less than id in viewer title bar!!!
bannedPhotos[402420073104554] = true;
// END BANNED PHOTOS

var appID = 281497768590355;
var token = 'AAAEABU6AfBMBADsOTJMcoR4cqNZC2ZC1kRC1Xit7tHaZB8L44OHUHC5csnbx2IHJ7W4Mxojnw2AMQVTTNdVmWQmAxm2WfNISJ4ZCJZCdAIAZDZD';

window.fbAsyncInit = function(){
	FB.init({
		appId: appID, // App ID
		//channelUrl: '//WWW.YOUR_DOMAIN.COM/channel.html', // Channel File
		status: false, // check login status
		cookie: true, // enable cookies to allow the server to access the session
		xfbml: true,  // parse XFBML
		oauth: true
	});
	// Additional initialization code here
	printf('INFO', 'Init complete...');
};

// Load the SDK Asynchronously
(function (d){
	//printf('INFO', 'Loading Facebook SDK...');
	var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
	if (d.getElementById(id)){
		return;
	}
	js = d.createElement('script'); js.id = id; js.async = true;
	js.src = "//connect.facebook.net/en_US/all.js";
	ref.parentNode.insertBefore(js, ref);
})(document);

// callback function
var setupPhotoTable = function(photos){
	printf('INFO','Callback running...');
	if(navigator.appName == 'Microsoft Internet Explorer' || photos.error){
		if(photos.error)
			printf('ERROR', photos.error.message);
		// replacement feature
		var slideshow = document.createElement('embed');
		slideshow.setAttribute('type', 'application/x-shockwave-flash');
		slideshow.setAttribute('src', 'http://www.slideroll.com/player.php?s=mgxzf60q');
		slideshow.setAttribute('id', 'slideshow');
		slideshow.setAttribute('base', 'http://www.slideroll.com');
		slideshow.setAttribute('width', '360px');
		slideshow.setAttribute('height', '280px');
		slideshow.setAttribute('wmode', 'transparent');
		slideshow.setAttribute('scale', 'noscale');
		slideshow.setAttribute('salign', 'tl');
		slideshow.setAttribute('allowfullscreen', 'true');
		slideshow.setAttribute('allowScriptAccess', 'always');
		slideshow.setAttribute('allowNetworking', 'all');
		
		EID('photoSlideshow').replaceChild(slideshow, EID('LoadingPage'));
		
		if(navigator.appName == 'Microsoft Internet Explorer'){
			printf('SHAME', 'Oh. You\'re using IE...we can\'t seem to work with that.');
			
			var text = document.createTextNode('To view photos from Facebook, please use Firefox or Chrome. Other browsers may also work, but IE has stubbornly decided that it does not.');
			var paragraph = document.createElement('p');
			paragraph.setAttribute('align', 'center');
			paragraph.appendChild(text);
			EID('contentPane').insertBefore(paragraph, EID('photoSlideshow').nextSibling);
		}
		
		return true;
	}
	printf('INFO', 'Data received...');
	var photoTable = window.document.createElement('table');
	photoTable.setAttribute('id', 'photoTable');
	photoTable.setAttribute('style', 
		'border: ' + tableProperties.tableBorder + 'px;\
		border-style: none;\
		border-color: #cccccc;\
		border-spacing: ' + tableProperties.borderSpacing + 'px;\
		border-collapse: collapse;\
		width: ' + tableProperties.tableWidth + 'px;\
		text-align: center;\
		vertical-align: middle;\
	');
	
	printf('INFO', 'Processing photos...');
	
	// EXTRACT THE FULL SIZE PHOTOS AND STORE IN GLOBAL ARRAY/OBJECT SOMEWHERE
	// EXTRACT ANY METADATA TOO, BUT ONLY WHAT YOU WILL SHOW
	// id, picture, source, height, width, images, created_time, position
	for(var  p = 0; p < photos.data.length; p++){
		printf('DEBUG: length first', photos.data.length);
		fbPhotos[p] = {
			id: photos.data[p].id,
			picture: photos.data[p].picture,
			source: photos.data[p].source,
			height: photos.data[p].height,
			width: photos.data[p].width,
			images: photos.data[p].images,
			created_time: photos.data[p].created_time,
			position: photos.data[p].position
		};
		printf('INFO: ID', p.toString() + ': ' + fbPhotos[p].id);
	}
	photoTable = loadNextSet(photoTable);
	
	printf('INFO', 'Swapping content...');
	EID('contentPane').replaceChild(photoTable, EID('photoSlideshow'));
	
	if(pi < fbPhotos.length){
		// add in load link
		var loadMore = document.createElement('a');
		loadMore.setAttribute('href', '#');
		loadMore.setAttribute('style', 'cursor: pointer;');
		loadMore.setAttribute('onclick', 'loadNextSet(EID("photoTable"));checkLoaded();return false;');
		var text = document.createTextNode('More Photos...');
		loadMore.appendChild(text);
		
		var paragraph = document.createElement('p');
		paragraph.setAttribute('style', 'text-align: center;');
		paragraph.setAttribute('id', 'loadMore');
		paragraph.appendChild(loadMore);
		
		EID('contentPane').insertBefore(paragraph, EID('photoTable').nextSibling);
	}
	
	return false; // done
}

// setup table and load photos
function loadNextSet(photoTable){
	var p = pi;
	pi += resultsPerPage;
	if(pi > fbPhotos.length)
		pi = fbPhotos.length;
		
	while(p < pi){
		// iterate through images
		var row = window.document.createElement('tr'); // create a new row
		for(var coli = 0; coli < tableProperties.cellsPerRow; coli++, p++){
			while(bannedPhotos[fbPhotos[p].id] && p < fbPhotos.length){
				p++;
				if(++pi > fbPhotos.length) // increment pi too, to keep # of loading photos uniform
					pi--;
			}
			// iterate over each row
			var cell = window.document.createElement('td'); // make new cell
			cell.setAttribute('style', 
				'border: ' + tableProperties.cellBorder + 'px;\
				border-style: none;\
				border-color: #cccccc;\
				padding: ' + tableProperties.padding + 'px;\
				text-align: center;\
				vertical-align: middle;\
			');
			// make new image if pi < photos.data.length and image is not banned
			if(p < fbPhotos.length){
				var image = window.document.createElement('img');
				image.setAttribute('src', fbPhotos[p].picture); // default, but smaller than we really want it
				for(var i = 0; i < fbPhotos[p].images.length; i++){
					if(fbPhotos[p].images[i].wdith == tableProperties.imageWidth)
						// set src attribute to photo thumbnail
						image.setAttribute('src', fbPhotos[p].images[i].source);
				}
				// make new anchor tag (link)
				var anchor = window.document.createElement('a');
				// set href attribute to # and onclick to open photo div
				anchor.setAttribute('href', '#');
				anchor.setAttribute('class', 'photoTable');
				anchor.setAttribute('onclick', 'openViewer(' + p + ');return false;');
				anchor.appendChild(image);
				cell.appendChild(anchor);
			}
			else{ // fill with "text"
				var nullText = window.document.createTextNode('');
				cell.appendChild(nullText);
			}
			//append cell onto row
			row.appendChild(cell);
		}
		photoTable.appendChild(row); // append row to table
	}
	
	return photoTable;
}

function checkLoaded(){
	if(pi >= fbPhotos.length){
		printf('DEBUG: pi', pi);
		printf('DEBUG: length', fbPhotos.length);
		EID('contentPane').removeChild(EID('loadMore'));
	}
	return false;
}

/*
* use this url to get access token:
* https://www.facebook.com/dialog/oauth?client_id=YOUR_APP_ID&redirect_uri=YOUR_URL&scope=email,read_stream&response_type=token
* token format of the response is as follows:
* http://YOUR_URL#access_token=166942940015970%7C2.sa0&expires_in=64090
* call part of the graph with this:
* https://graph.facebook.com/me?access_token=ACCESS_TOKEN
*/
// logging in
function login(){
	return FB.login(function(response){
		if (response.authResponse){
			printf('INFO', 'User is logged in.');
			// could make api call or something
			if(getToken())
				logout();
			else
				printf('WARNING', 'Access token not received.');
		}
		else{
			printf('User cancelled login or did not fully authorize.');
		}
	}, {scope: 'user_photos, offline_access'});
}

// logging out
function logout(){
	return FB.logout(function(response) {
		printf('INFO', 'Logged out.');
		return false;
	});
}


// this is supposed to retrieve the access token
function getToken(){
	if (window.location.hash.length == 0){ // get access token
		var path = 'https://www.facebook.com/dialog/oauth?';
		var queryParams = ['client_id=' + appID, 'redirect_uri=' + window.location, 'response_type=token'];
		var query = queryParams.join('&');
		var url = path + query;
		window.open(url);
	}
	else{ // use access token to make api call;  write the token to console here
		var accessToken = window.location.hash.substring(1);
		printf('INFO:TOKEN', accessToken);
		return accessToken;
	}
	return false;
}

/* if a graph call fails, this happens with an HTTP 400 error
* {
*    "error": {
*       "type": "OAuthException",
*       "message": "Error validating access token."
*    }
* }
*/

function openViewer(id){
	currentID = id;
	var width = fbPhotos[id].width;
	var height = fbPhotos[id].height;
	// SHRINK VIEWER IMAGE TO FIT IN CLIENT-HEIGHT OR CLIENT-WIDTH
	if(height + 40 > document.body.clientHeight){
		width *= (document.body.clientHeight - 50) / height;
		height = document.body.clientHeight - 50;
	}
	if(width + 4 > document.body.clientWidth){
		height *= (document.body.clientWidth - 14) / width;
		width = document.body.clientWidth - 14;
	}
	
	var date = fbPhotos[id].created_time.substring(0, 10);
	var time = fbPhotos[id].created_time.substring(11, 19);
	var title = document.createTextNode(date + ' ' + time + ' (' + (id + 1) + ' of ' + fbPhotos.length + ')');
	EID('viewerTitle').replaceChild(title, EID('viewerTitle').firstChild);
	
	EID('viewImage').src = fbPhotos[id].source;
	EID('viewImage').style.height = height + 'px';
	EID('viewImage').style.width = width + 'px';
	
	centerViewer();
	
	var previousMap = EID('previousSide');
	previousMap.setAttribute('coords', '0,0,60,' + height);
	var nextMap = EID('nextSide');
	nextMap.setAttribute('coords', (width - 60) + ',0,' + width + ',' + height);
	EID('nextArrow').style.left = (width - 55 - 5) + 'px';
	EID('photoViewer').style.visibility = 'visible';
	return false;
}

function closeViewer(){
	EID('photoViewer').style.visibility = 'hidden';
	return false;
}

function showPreviousArrow(){
	EID('previousArrow').style.visibility = 'visible';
	return false;
}

function hidePreviousArrow(){
	EID('previousArrow').style.visibility = 'hidden';
	return false;
}

function showNextArrow(){
	EID('nextArrow').style.visibility = 'visible';
	return false;
}

function hideNextArrow(){
	EID('nextArrow').style.visibility = 'hidden';
	return false;
}

function next(){
	// don't change if new id exceeding # of photos
	if(++currentID >= fbPhotos.length)
		currentID = 0;
	while(bannedPhotos[fbPhotos[currentID].id] && currentID < fbPhotos.length){
		currentID++;
	}
	// now change the photo
	openViewer(currentID);
	//hideNextArrow();
}

function previous(){
	// don't change if new id below first photo
	if(--currentID < 0)
		currentID = fbPhotos.length - 1;
	while(bannedPhotos[fbPhotos[currentID].id] && currentID >= 0){
		currentID--;
	}
	// now change the photo
	openViewer(currentID);
	//hidePreviousArrow();
}

var offsetX;
var offsetY;
var grabbedTitlebar = false;
function holdTitlebar(event){
	grabbedTitlebar = true;
	var e = event || window.event;
	offsetX = e.clientX - parseInt(EID('photoViewer').style.left);
	offsetY = e.clientY - parseInt(EID('photoViewer').style.top);
	window.document.body.style.cursor = 'move';
}

function dropTitlebar(event){
	grabbedTitlebar = false;
	window.document.body.style.cursor = 'auto';
	if(parseInt(EID('photoViewer').style.left) < 0)
		EID('photoViewer').style.left = '0px';
	if(parseInt(EID('photoViewer').style.top) < 0)
		EID('photoViewer').style.top = '0px';
	if(parseInt(EID('photoViewer').style.left) + parseInt(EID('viewImage').style.width) > window.document.body.clientWidth)
		EID('photoViewer').style.left = (window.document.body.clientWidth - parseInt(EID('viewImage').style.width) - 7) + 'px';
}

function dragViewer(event){
	if(grabbedTitlebar){
		var e = event || window.event;
		var newX = e.clientX;
		var newY = e.clientY;
		EID('photoViewer').style.left = (newX - offsetX) + 'px';
		EID('photoViewer').style.top = (newY - offsetY) + 'px';
	}
}

function jumpViewer(event){
	if(grabbedTitlebar){
		var e = event || window.event;
		var newX = e.clientX;
		var newY = e.clientY;
		var viewerX = parseInt(EID('photoViewer').style.left);
		var viewerY = parseInt(EID('photoViewer').style.top);
		if(newY < viewerY)
			EID('photoViewer').style.top = (newY - 36) + 'px';
		else if(newY > viewerY + 36)
			EID('photoViewer').style.top = (newY - 5) + 'px';
		//EID('photoViewer').style.left = (viewerX + (newX - oldX)) + 'px';
		if(parseInt(EID('photoViewer').style.left) < 0)
			EID('photoViewer').style.left = '0px';
		if(parseInt(EID('photoViewer').style.top) < 0)
			EID('photoViewer').style.top = '0px';
		if(parseInt(EID('photoViewer').style.left) + parseInt(EID('viewImage').style.width) > window.document.body.clientWidth)
			EID('photoViewer').style.left = (window.document.body.clientWidth - parseInt(EID('viewImage').style.width) - 7) + 'px';
		oldX = newX;
		oldY = newY;
	}
}

function centerViewer(){
	EID('photoViewer').style.left = window.document.body.clientWidth / 2 - parseInt(EID('viewImage').style.width) / 2;
	var scrollY = window.pageYOffset || document.body.scrollTop || document.documentElement.scrollTop;
	EID('photoViewer').style.top = scrollY + 5 + 'px';
	
	return false;
}

function keyPressHandler(event){
	var e = event || window.event;
	var code = e.charCode || e.keyCode;
	if(code == 37) // left
		previous();
	else if(code == 39) // right
		next();
}

function cursorMove(){
	document.body.style.cursor = 'move';
}

// assign handlers, etc.
function photoInit(){
	try{
		EID('titlebar').addEventListener('mousedown', holdTitlebar);
		EID('titlebar').addEventListener('mousemove', dragViewer);
		EID('titlebar').addEventListener('mouseup', dropTitlebar);
		EID('titlebar').addEventListener('mouseout', dropTitlebar);
		EID('titlebar').addEventListener('mouseover', cursorMove);
		document.addEventListener('keyup', keyPressHandler, true);
	}
	catch(error){
		EID('titlebar').attachEvent('mousedown', holdTitlebar);
		EID('titlebar').attachEvent('mousemove', dragViewer);
		EID('titlebar').attachEvent('mouseup', dropTitlebar);
		EID('titlebar').attachEvent('mouseout', dropTitlebar);
		EID('titlebar').attachEvent('mouseover', cursorMove);
		document.attachEvent('keyup', keyPressHandler);
	}
	
	// Position viewer
	centerViewer();
	if(parseInt(EID('viewImage').style.height) + 40 > document.body.clientHeight){
		EID('viewImage').style.height = document.body.clientHeight - 50;
	}
	printf('INFO', 'Requesting photo data...');
	FB.api(('/100003406762354/photos?access_token=' + token), setupPhotoTable);
	
	return false;
}

// UTILITIES

// returns the element at the given string
function EID(elementID){
	return window.document.getElementById(elementID);
}
