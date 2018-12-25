from hashlib import sha256

def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()

#Taking from https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py

Comments = []
Passwords = []


index = 0
password_index = 0
password_found = False

while True:
	print("Menu:")
	print("1) Please enter \"register\" to be registered")
	print("2) Please enter \"comment\" to write comment")
	print("3) Please enter \"exit\" to exit the program")
	choise = input("Your choise: ")
	
	if (choise.lower() == "register"):
		pw1 = input('Please enter your password:')
		hsh1 = create_hash(pw1)
		Passwords.append(hsh1)	
#Taking from https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py
		
	elif (choise.lower() == "comment"):	
		your_comment =  input("Enter your comment: ")
		your_password = input("Enter your password: ")
		hsh2 = create_hash(your_password)
#Taking from https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py		
		
		while password_index < len(Passwords):
			if(Passwords[password_index] == hsh2):
				Comments.append(your_comment)
				password_found = True
				break
			else:
				password_index = password_index + 1
			
		if (password_found == False):
			print("I am sorry I cannot let you do that.")
			
		elif (password_found == True):
			print("Previously entered comments:")
			while index < len(Comments):
				message = str(index+1) + ". " + Comments[index] 
				print(message)
				index = index + 1
			index = 0
		password_index = 0
		password_found = False		
			
	elif (choise.lower() == "exit"):
		break
