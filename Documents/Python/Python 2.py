name = {0:"Michaela", 1:"Steve"};
gender = {0:"Female", 1:"Male"};
height = {0:178, 1:160};
jobs = {0:["Visual Artist"], 1:["Graphic Designer at Acme Corp", "Bartender at Banter"]};
parents = {0:["Aimee", "Louis"], 1:None};
pets = {0:["Fezzy","Rufus"], 1:None};
nick = {0:None, 1:"The Cow"};
friend = {0:None, 1:["Stephen","Stephanie","Stefan"]};

for i in range(0, len(name), 1):
	if name[i] != None:
		print("Name: {0}".format(name[i]));
	if gender[i] != None:
		print("Gender: {0}".format(gender[i]));
	if height[i] != None:
		print("Height in cm: {0}".format(height[i]));
	if jobs[i] != None:
		print("Jobs: {0}".format(str(jobs[i]).strip("[]").replace("'","")));
	if parents[i] != None:
		print("Parents: {0}".format(str(parents[i]).strip("[]").replace("'","")));
	if pets[i] != None:
		print("Pets: {0}".format(str(pets[i]).strip("[]").replace("'","")));
	if nick[i] != None:
		print("Nickname: {0}".format(nick[i]));
	if friend[i] != None:
		print("Friends: {0}".format(str(friend[i]).strip("[]").replace("'","")));
	print("\n");
