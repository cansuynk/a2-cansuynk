Comments = []

index = 0

while True:
	your_comment =  input("Enter your comment (To exit the program write \"exit\"): ")
	if(your_comment.lower() == "exit"):
		break
	Comments.append(your_comment)
	print("Previously entered comments:")
	while index < len(Comments):
		message = str(index+1) + ". " + Comments[index] 
		print(message)
		index = index + 1
	index = 0
