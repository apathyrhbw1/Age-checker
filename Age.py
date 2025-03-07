import time
print("Hello user, may I know your name?")

name = input("Enter your name: ")
time.sleep(1)
print("Hello," + name, "how are you?")
time.sleep(1)

while True:
	try:
		classify_age = float(input("How old are you?: "))
		if classify_age <=12:
			print("you're a child")
		
		elif classify_age <=19:
			print("you're a teen")
		
		elif classify_age <=64:
			print("you're an adult")
		
		elif classify_age >=65:
			print("you're a senior")
		
		else:
			print("please inpur your age in no.")
			break
			
	except ValueError:
			print("please input your age in no.")