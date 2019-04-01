#!/usr/bin/python
print("Content-type: text/html\n\n")

titleMessage = "My Python Webpage"
bodyMessage = "Hello World"

pythonURLs = {
    "Real Python":"https://realpython.com/courses/python-requests/",
    "The Hitchhiker's Guide to Python!":"https://docs.python-guide.org/"

}

goURLs = {
    "Go by example":"https://gobyexample.com/channels",
    "A Tour of Go":"https://tour.golang.org/"
}

ansibleURLs = {
    "Using Ansible Through WSL":"https://www.jeffgeerling.com/blog/2017/using-ansible-through-windows-10s-subsystem-linux"
}

selfHostedURLs = {
    "BookStack":"https://www.bookstackapp.com/",
	"Graylog":"https://www.graylog.org/"
}

miscBlogsURLS = {
	"No Lab No Party":"https://nolabnoparty.com/",
	"Derek Seaman's IT Blog":"https://www.derekseaman.com/",
	"VCDX56":"http://vcdx56.com/",
	"Yellow Bricks":"http://www.yellow-bricks.com/",
	"virtuallyGhetto":"https://www.virtuallyghetto.com/",
	"VMGuru":"https://vmguru.com/",
	"Nutanix Community Blog":"https://next.nutanix.com/blog-40",
	"The Deployment Bunny":"https://deploymentbunny.com/",
	"SCConfigMgr":"https://www.scconfigmgr.com/",
	"Demployment Research":"https://deploymentresearch.com/Research",
	"Petri":"https://www.petri.com/"
	
	
}

devOpsURLs = {
	"Google SRE Books":"https://landing.google.com/sre/books/",
	"Hashicorp":"https://www.hashicorp.com/"
	
}

miscURLs = {
	"ZeroTier (VPN)":"https://www.zerotier.com/",
	
}


head = (
f"<html>"
    f"\n\t<head>"
        f"\n\t\t<title>{titleMessage}</title>"
    f"\n\t</head>"
)

lists = "<ul>"

for k,v in pythonURLs.items():
    lists += f"\n\t\t\t<il><a href=\"{v}\">{k}</a>"

lists += "\n\t\t</ul>"

body = (
    f"\t<body>"
        f"\n\t\t<p>{bodyMessage}</p>"
        f"\n\t\t{lists}"
    f"\n\t</body>"
f"\n</html>"
)


#head.format(titleMessage)
#body.format(bodyMessage)

#print(head.format(titleMessage))
print(head)
print(body)