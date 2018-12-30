
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, request, static_file, get, post
from hashlib import sha256

def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()

#Taking from https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py

Passwords = {}

#Checks the user information for registration
def Register(username, pw1):
	global Passwords
	hsh1 = create_hash(pw1)
	  
	if(username not in Passwords):
		Passwords[username]=hsh1
		#Saves new record to the file
		with open('./userdata.txt', 'a') as f:
			username=username+"\n"
			hsh1=hsh1+"\n"
			f.write(username)
			f.write(hsh1)
		return True
	else:
		return False

#Checks the user information for comment	
def Comment(username, pw1):
	global Passwords
	
	hsh2 = create_hash(pw1)
	
	if(username in Passwords):
		if(Passwords[username]==hsh2):
			return True
		else:
			return False

#Prints the page
def htmlify(text):
    page = """
        <!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>CONTACT</title>
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.4.1/css/all.css" integrity="sha384-5sAR7xN1Nv6T6+dT2mhtzEpVJvfS3NScPQTrOxhwjIuvcA67KV2R5Jz6kr4abQsz" crossorigin="anonymous"/>
<link rel='stylesheet' id='googlefonts-css'  href='http://fonts.googleapis.com/css?family=Open+Sans:300,300italic,400,400italic,600,600italic,700,700italic,800,800italic&subset=latin,latin-ext' type='text/css' media='all' />
<link href='https://fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext' rel='stylesheet' type='text/css' media='all' />
<link rel="stylesheet" href="/static/contact.css" type="text/css"/>
<link rel="shortcut icon" type="image/png" href="/static/images/logo.png" />
</head>

<body style="background-color:#F5B7B1;">

<div class="topmain">
	<div class="sides">
		<img src="/static/images/side.png" width="150" alt="Sidepicture" />
	
	</div>
	
<div class="main">
	<div class="header">
		<div class="logo">
			<a href="/index.html"><img src="/static/images/logo.png" width="300" height="300" alt="LOGO" /></a>
		</div>

		<div class="header-right">
			<div class="slogan"><span class="slogan-item">ISAAC ASIMOV</span></div>
		</div>
	</div>

	<div class="navbar">
		<div id="menu">
			<ul>
				<li><a href="/index.html">HOME</a></li>
				<li><a href="/about.html">ABOUT ISAAC ASIMOV</a></li>
				<li class="dropdown">
					<a href="javascript:void(0)" class="dropbtn">BOOKS<i class="fas fa-caret-down"></i></a>
					<div class="books-content">
						<div id="menu2">
						<a href="/hisbooks.html">HIS BOOKS</a>
						<a href="/booksiread.html">BOOKS I READ</a>
						</div>
					</div>
				</li>
				<li style="float:right"><a class="active" href="/contact">CONTACT</a></li>
			</ul>				
		</div>
	</div>
	
	

	<div class="content">
		<p class="title"><strong>CONTACT INFORMATION</strong></p>
		<div class="container">
		
			<p class="text"> 
				<img src="/static/images/star.png" width="20" height="20" alt="Staricon" />
				You can contact with me via these addresses.
				<img src="/static/images/star.png" width="20" height="20" alt="Staricon" />
			</p>
			
			<table id="contact">
				<tr>
					<td colspan="4">
						<img  src="/static/images/hi.png" width="300" height="300" alt="Mylogo" class="centerimage">
					</td>
				</tr>
				
				<tr>
					<td colspan="2"  class="titlee"><p>My E-mail Addresses</p></td>
					<td class="titlee"><p>My Linkedin Profile</p></td>
					<td class="titlee"><p>My Location</p></td>
				</tr>
				
				<tr>
					<td class="pagination">
						<a href="mailto:yanikc17@itu.edu.tr">
							<img src="/static/images/mail.png" width="60" height="60" alt="Mail" class="centerimage">
						</a>
											
					</td>
										
					<td class="pagination">
						<a href="mailto:cansuyanik96@gmail.com">
								<img src="/static/images/google.png" width="60" height="60" alt="Mail" class="centerimage">
						</a>
					</td>
					
					<td class="pagination">
						<a href="https://www.linkedin.com/in/cansuyanik/" target="_blank">
							<img src="/static/images/linkedin.png" width="60" height="60" alt="Linkedin" class="centerimage">
						</a>
					</td>
					
					<td class="pagination">
						<details>
							<summary>
								<img src="/static/images/location.png" width="60" height="60" alt="Adress" class="centerimage">
							</summary>
							
							<address><p>İTÜ International Office 
										Ayazaga Campus 
										Registrator's Office Building
										Maslak 34469 Sarıyer/Istanbul Tel:+902122856600 
										Fax:+902122857139</p>
							</address>
							
						</details>
					</td>
				</tr>
			</table>
			
			<div class="commentarea">
				<p class="text"> 
					<img src="/static/images/star.png" width="20" height="20" alt="Staricon" />
					Leave me a comment 
					<img src="/static/images/star.png" width="20" height="20" alt="Staricon" />
				</p>
				<p><strong><i>Note: If you are new here, please register before adding a comment :)</i></strong> </p>
				<details>
					<summary>
						<strong>Open for steps</strong>
					</summary>
					<ol>
						<li>
							<strong>Enter your name and password</strong>
						</li>
						<li>
							<strong>Select "Register" option for registration or select "Comment" for adding comment</strong>
						</li>
						<li>
							<strong>Submit your changes</strong>
						</li>
					</ol>
					
				</details>
					
				%s
				
			</div>
			
			<p class="thanks">THANK YOU SO MUCH!</p>

		</div>
	  
	</div>

	<div class="footer"><p>&copy; 2018, By Cansu YANIK</p></div>

</div>

	<div class="sides2">
		<img src="/static/images/side.png" width="150" alt="Sidepicture" />
	
	</div>

</div>

<script>
	window.onscroll = function() {myFunction()};

	var menu = document.getElementById("menu");
	var sticky = menu.offsetTop;
	
	var menu2 = document.getElementById("menu2");
	var sticky2 = menu2.offsetTop;

	function myFunction() {
	  if (window.pageYOffset >= sticky) {
		menu.classList.add("sticky")
	  } else{
		menu.classList.remove("sticky");
	  }
	  if (window.pageYOffset >= sticky) {
		menu2.classList.add("books-content2")
	  } else{
		menu2.classList.remove("books-content2");
	  }
	}
</script>

</body>
</html>

    """ % (text)
    return page

#Prints content of comment section
def print_forum(text):
	global html
	html= '''<form action="/contact" method="post">
				<br/><br/>			
				Your Username:
				<input type="text" name="name" placeholder="Name">
					  
				Your Password:
				<input type="password" name="password" placeholder="Password">
					  
				<input type="submit" value="Submit"><br/><br/>
				
				<input type="radio" name="option" value="Register" checked>Register
				<input type="radio" name="option" value="Comment">Comment
				
				<br/><br/><p>%s</p>
				<div class="comment">
					<input type="text" name="comment" placeholder="Write your comment here"/>
				</div>
				
			</form> 
				
				'''%(text)
	#Reads the comments from file and keeps them into a list
	Comments_file=[]
	data_file = open ("./datafile.txt", "r")
	while True:
		username = data_file.readline()
		
		if not username:
			break;
		comment = data_file.readline()
		User=[]
		User.append(username.strip()+":")
		User.append(comment.strip())
		Comments_file.append(User)
	data_file.close()  
	
	#Reads the user information from file and keeps them into a list
	global Passwords
	Passwords = {}
	data_file = open("./userdata.txt", "r")
	while True:
		usernames = data_file.readline()
		
		if not usernames:
			break;
		password = data_file.readline()
		Passwords[usernames.strip()]=password.strip()	
	data_file.close() 
	
	#Prints user and admin comments			
	for item in Comments_file:
		if(item[0]=="Admin:"):
			html+= '''
				<div class="Admincomments">
					<p><strong>%s </strong></p>
					<p>%s</p>
				</div>
				''' %(item[0],item[1])
			continue
		html+= '''
			<div class="usercomments">
				<p><strong>%s </strong></p>
				<p>%s</p>
			</div>
				''' %(item[0],item[1])			
	return html
    
option=""
html=""

#Gets option
def get_option():
	global option
	option=request.POST["option"]
	global html
	
	name=request.POST["name"]
	password=request.POST["password"]
	comment=request.POST["comment"] 
	
	if(option=="Register"):
		registration=Register(name,password)
		option=""
		if(registration==True):
			html=print_forum("Your registration is successful")
		else:
			html=print_forum("This username has been already taken")	
			
	elif(option=="Comment"):
		member=Comment(name,password)
		if(member==True):
			if "</" not in comment:
				if "<" not in comment:
			#Saves new comment to the file
					with open('./datafile.txt', 'a') as f:
						name=name+"\n"
						comment=comment+"\n"
						f.write(name)
						f.write(comment)	
					option=""
					member=False
					index()
		else:
			html=""
			html=print_forum("Your username or password is not correct")
				
	return htmlify(html)
		
		
def index():
	global html
	html=""
	html= print_forum("")			
					
	return htmlify(html)
	
def homepage():
	return server_static('/index.html')
	

def server_static(fname):
   txt = static_file(fname, root='./static_files')
   return txt

	
route('/static/<fname:path>','GET',server_static)
route('/<fname:path>','GET',server_static)
route('/contact', 'GET', index)
route('/contact','POST',get_option)
route('/','GET',homepage)


#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()

