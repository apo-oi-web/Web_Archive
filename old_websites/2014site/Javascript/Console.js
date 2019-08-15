/**
 * @author Colin Ogren
 */

// CONSOLE FUNCTIONS

// Initialization code: clear console, add event listeners
function init(){
	clearConsole();
	try{
		document.addEventListener('keydown', keyDownHandler, true);
		document.addEventListener('keyup', keyUpHandler, true);
	}
	catch(error){
		document.attachEvent('onkeydown', keyDownHandler);
		document.attachEvent('onkeyup', keyUpHandler);
	}
	return false;
}

// Press CTRL + ALT + C to open console
var ctrlDown = false;  // true when pressed
function keyDownHandler(event){
	var e = event || window.event;
	var code = e.charCode || e.keyCode;
	if(code == 17)
		ctrlDown = true; // technically, there is a e.ctrlKey, but Chrome is buggy
	if(code == 67 && ctrlDown && e.altKey) // CTRL + ALT + C
		window.document.getElementById('consoleWindow').style.visibility = 'visible';
}

// Release CTRL and the key will unregister
function keyUpHandler(event){
	var e = event || window.event;
	var code = e.charCode || e.keyCode;
	if(code == 17)
		ctrlDown = false;
}

// Hides the console
function closeConsole(){
	window.document.getElementById('consoleWindow').style.visibility = 'hidden';
	return false;
}

// Clears all text from the console
function clearConsole(){
	window.document.getElementById('console').value = '';
	return false;
}

/* Print a message to the console
 * code is any number the can associate with a message
 * message is the content text
 * newline specifies if each line should end with a \n (on by default)
 */
function printf(code, message, noNewline){
	var lbracket = '[';
	var rbracket = '] ';
	var new_line = '\n';
	
	if(code == '')
		lbracket = rbracket = '';
	if(noNewline)
		new_line = '';
	
	window.document.getElementById('console').value += lbracket + code + rbracket + message + new_line;
	return window.document.getElementById('console').value.length;
}

// END CONSOLE CODE