urlParams = new URLSearchParams(window.location.search);
usr = urlParams.get('username');
pwd = urlParams.get('password');
if (!(usr == null && pwd == null))
{
	if (usr == "cantgetme" && pwd == "thistime")
	{
		window.location.href = "admin.html";
	}
	else
	{
		window.location.href = "nosuccess.html";
	}
}