print "Lets know your info"
name = raw_input("What is your name?") #almost like to alert function and take the variable assign it from my input 
quest = raw_input("What is your quest?") #almost like to alert function and take the variable assign it from my input 
color = raw_input("What is your favorite color?") #almost like to alert function and take the variable assign it from my input 
age = raw_input("How old are you ?")

while True:

	if age.isdigit():
		print "Ah, so your name is %s, your quest is %s, printing out"
	"and your favorite color is %s ." % (name, quest, color,int(age)) #%s's to replace the inputs by also using a modulo-% then to result in a full sentence

elif:
	print "%s, \"%s\" is not an age!" % (name,age)
