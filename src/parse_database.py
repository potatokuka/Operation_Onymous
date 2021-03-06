import json

def getTarget(line):
	jsonLine = json.loads(line)
	try:
		username = jsonLine['payment']['target']['user']['username']
	except:
		username = "NULL"
	try:
		display_name = jsonLine['payment']['target']['user']['display_name']
	except:
		display_name = "NULL"
	return username, display_name

def getActor(line):
	jsonLine = json.loads(line)
	try:
		username = jsonLine['payment']['actor']['username']
	except:
		username = "NULL"
	try:
		display_name = jsonLine['payment']['actor']['display_name']
	except:
		display_name = "NULL"
	return username, display_name

def getNote(line):
	try:
		note = json.loads(line)['payment']['note']
	except:
		note = "NULL"
	return note

print("What database would you like to parse?")
print("database/", end="")
database_file = input().split()[0]
if database_file[-5:] == ".json":
	database_file = database_file[:-5]
try:
	fields = open("../database/" + database_file + ".json", "r").read().split("\n")
except:
	print("Invalid file")
	quit()
print("{:<50} {:<50} {:<16}".format("BUYER", "SELLER", "NOTE"), end="\n\n")
for i in fields:
	jsonLine = json.loads(i)
	targetUser, targetName = getTarget(i)
	actorUser, actorName = getActor(i)
	note = getNote(i)
	if jsonLine['payment']['action'] == "pay":
		print("{:<50} {:<50} {:<16}".format((actorUser + " (" + actorName + ")"), (targetUser + " (" + targetName + ")"), note))
	else:
		print("{:<50} {:<50} {:<16}".format((targetUser + " (" + targetName + ")"), (actorUser + " (" + actorName + ")"), note))