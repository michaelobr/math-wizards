import random

# Set both players' scores to 0 at the beginning 
p1_score = 0
p2_score = 0

# Game introduction 
print("This is a math game. Two players pick two numbers each, any number they want. Then a random operation is performed on these two numbers. Whichever player is closest to the target number wins the round. \n")

num_rounds = int(input("How many rounds would you like to play? "))
max_range = int(input("At which magnitude would you like to set the possible target number range? (begins at 0) "))

# Game Loop 
for x in range(1, num_rounds + 1):
	print("Round #", x, " out of 10", sep="")
	
	# Create a target number
	target_number = random.randint(0, max_range)
	
	# Get the users' numbers
	p1fn = int(input("Player 1, enter your first number: "))
	p1sn = int(input("Player 1, enter your second number: "))
	p2fn = int(input("Player 2, enter your first number: "))
	p2sn = int(input("Player 2, enter your second number: "))

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
	if target_number >= p1_result:
		p1_distance = target_number - p1_result
	elif target_number <= p1_result:
		p1_distance = p1_result - target_number

	# Calculate the score for player 2
	if target_number >= p2_result:
		p2_distance = target_number - p2_result
	elif target_number <= p2_result:
		p2_distance = p2_result - target_number

	if p1_distance == 0:
		print("Exact guess, 10x point multiplier.")
		p1_score += 10
	if p2_distance == 0:
		print("Exact guess, 10x point multiplier.")
		p2_score += 10
	elif p1_distance < p2_distance:
		p1_score += 1
	elif p2_distance < p1_distance:
		p2_score += 1
	else:
		p1_score += 1
		p2_score += 1
		print("Tie: Each player receives 1 point.")

	print("The score is...", "\n", "Player 1: ", p1_score, "\n", "Player 2: ", p2_score)