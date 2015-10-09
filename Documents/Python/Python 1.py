byte = "school";
instructors = ["Greg", "Ken", "Billy"];
students = ("Adolfo", "Benny", "Devin", "Brendan");
# The difference main between a tuple and a list is that a tuple cannot be changed after its creation but a list can be edited. 
# A tuple should be used for constants and values that will not change during the execution of the program. 
# A list should be used if a collection of values is needed and the values will be changed by the end of the program.
dictionary = {'byteAcademy':byte, 'instructors':instructors, 'students':students};
test = {0:'byteAcademy', 1:'instructors', 2:'students'}; # Needed to output keys and values in print statement
for i in range(0,len(test),1):
	print("{0} - {1}".format(test[i], str(dictionary[test[i]]).strip("[]()").replace("'","")));