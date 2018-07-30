import random

# Game introduction 
print("This is a math game. Two players pick two numbers each, any number they want. Then a random operation is performed on these two numbers.", 
	"Both players earn points each round, but the closest player to the target number earns more points. \n")

# Set both players' scores to 0 at the beginning 
p1_score = 0
p2_score = 0

# Game Loop 
for x in range(1, 11):
	print("Round #", x, " out of 10", sep="")
	# Get the users' numbers
	p1fn = int(input("Player 1, enter your first number: "))
	p1sn = int(input("Player 1, enter your second number: "))
	p2fn = int(input("Player 2, enter your first number: "))
	p2sn = int(input("Player 2, enter your second number: "))

	# Create a target number
	target_number = random.randint(0, 100)

	# Figure out which operator to use 
	choice = random.choice(["addition", "subtraction", "multiplication", "division"])
	if choice == "addition":
		p1_result = p1fn + p1sn
		p2_result = p2fn + p2sn
		print("Player 1: ", p1fn, " + ", p1sn, " = ", p1_result)
		print("Player 2: ", p2fn, " + ", p2sn, " = ", p2_result)
	elif choice == "subtraction":
		p1_result = p1fn - p1sn
		p2_result = p2fn - p2sn
		print("Player 1: ", p1fn, " - ", p1sn, " = ", p1_result)
		print("Player 2: ", p2fn, " - ", p2sn, " = ", p2_result)
	elif choice == "multiplication":
		p1_result = p1fn * p1sn
		p2_result = p2fn * p2sn
		print("Player 1: ", p1fn, " x ", p1sn, " = ", p1_result)
		print("Player 2: ", p2fn, " x ", p2sn, " = ", p2_result)
	elif choice == "division":
		p1_result = p1fn / p1sn
		p2_result = p2fn / p2sn
		print("Player 1: ", p1fn, " / ", p1sn, " = ", p1_result)
		print("Player 2: ", p2fn, " / ", p2sn, " = ", p2_result)
	
	print("The target number was ", target_number, ".", sep="")

	# Calculate the score for player 1
	if target_number > p1_result:
		p1_distance = target_number - p1_result
	elif target_number < p1_result:
		p1_distance = p1_result - target_number

	# Calculate the score for player 2
	if target_number > p2_result:
		p2_distance = target_number - p2_result
	if target_number < p2_result:
		p2_distance = p1_result - target_number

	if p1_distance < p2_distance:
		p1_score += 1
	if p2_distance < p1_distance:
		p2_score += 1
	if p1_distance == p2_distance:
		p1_score += 1
		p2_score += 1
		print("Tie: Each player receives 1 point.")

	print("The score is...", "\n", "Player 1: ", p1_score, "\n", "Player 2: ", p2_score)