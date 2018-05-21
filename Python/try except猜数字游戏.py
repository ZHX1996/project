import random

num = random.randint(0,100)
print num

while True:
	try:
		guess = int(raw_input("Enter 1~100: "))
	except ValueError, e:
		print "Please enter 1~100", e
		continue
	if guess > num:
		print "less than", guess
	elif guess < num:
		print "greater than", guess
	else:
		print "Bingo, Game Over"
		break
	print "\n"
