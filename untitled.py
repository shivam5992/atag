import subprocess, sys

def execute(cmd, message):
	try:
		print (message)
		cmdlist = cmd.split()
		process = subprocess.Popen(cmdlist, stdout=subprocess.PIPE)
		output = process.communicate()[0]
		return (output)
	except:
		print "Error"


def automate_tagging(bname = None, tagname = None, tagmessage = None):
	command = "git checkout " + bname
	execute(command, "Checking out to branch " + bname)

	command = "git rev-parse " + bname
	execute(command, "Obtaining the commit id")

	command = "git tag -a '" + tagname + "' -m '" + tagmessage + "'"
	execute(command, "Creating the tag")

	command = "git show '" + tagname + "'"
	execute(command, "Show Tag: ")

	command = "git rev-parse " + bname
	execute(command, "")
	command = "git rev-parse tags/" + tagname + "^{commit}"
	execute(command, "Validating the tag")

args = sys.argv
bname = args[1]
tname = args[2]
tmsg = args[3]
automate_tagging(bname, tname, tmsg)





