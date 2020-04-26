urlParams = new URLSearchParams(window.location.search);
usr = urlParams.get('username');
pwd = urlParams.get('password');

var xmlhttp = new XMLHttpRequest();
var credentials = "";
xmlhttp.open("GET", "data/users.txt", false);
xmlhttp.send();
if (xmlhttp.status==200) {
	credentials = xmlhttp.responseText.split(' ');
}

if (!(usr == null && pwd == null))
{
	if (usr == credentials[0] && pwd == credentials[1])
	{
		window.location.href = "admin.html";
	}
	else
	{
		window.location.href = "nosuccess.html";
	}
}