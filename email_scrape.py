import re #regular expressions library being used

def load_data():
	"""Tries to find a file in the given directory. Defaults to the current one
	If no file exists by that name, the program will run again and handle
	the conflict.
	"""

	print("""Enter file name you wish to scape for emails.
An example would be my_file.txt
If you wish to exit, just press enter.
		""")
	file_to_scrape = input(">>>")
	# take input until an existing file is given or exit when input is blank 
	if file_to_scrape == "":
		exit()
	try:
		with open(file_to_scrape) as f:
			return f.read()
	except FileNotFoundError:
		print("No such file found. Try again.")
		load_data()

def find_emails(text_to_read):
	""" Looks for emails with domain of com, net, org, or gov. Some
	formats which are probably not real emails can be discovered such as:
	9702@3123.com. This is unlikely to be a real email with all numbers, but
	nonetheless it will be found.
	"""
	emailRegex = re.compile(r'(\w+@\w+.(com|net|org|gov))')
	mo = emailRegex.findall(text_to_read)
	if not mo: #if mo is empty a.k.a nothing found
		print("No emails found.")
		return 0
	emails = []
	for email in mo: #removes unnecessary repeat of domain name
		emails.append(email[0])
	print("Here are the emails found:")
	for email in emails:
		print(email)
#main program
data_source = load_data()
find_emails(data_source)
print("\nExiting program...")
