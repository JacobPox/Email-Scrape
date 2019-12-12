import re

def load_data():
	print("""Enter file name you wish to scape for emails.
An example would be my_file.txt
If you wish to exit, just press enter.
		""")
	file_to_scrape = input(">>>")
	if file_to_scrape == "":
		exit()
	try:	
		with open(file_to_scrape) as f:
			return f.read()
	except FileNotFoundError:
		print("No such file found. Try again.")
		load_data()

def find_emails(text_to_read):
	emailRegex = re.compile(r'(\w+@\w+.(com|net|org|gov))')
	mo = emailRegex.findall(text_to_read)
	print("Here are the emails found: {}".format(mo))

data_source = load_data()
find_emails(data_source)
print("Exiting program...")
