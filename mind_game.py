print "Now let's prepare for the game take a BREATH !!!"

answer = "YES"
toBegin = "Are you ready ?"

while True:
 
    start = str(raw_input(toBegin))

    if start == answer:
	print ("You are not ready. Try again !!!")
    else: # start == answer
	print ("Go !!!")
	break

print ("Now let's play the guessing game!")

answer = 23
question = "What number am I thinking of? "
while True:
    guess = int(input(question))

    if guess < answer:
        print ("Little higher")
    elif guess > answer:
        print ("Little lower")
    else: # guess == answerOne
        print ("MINDREADER!!!")
        break

