print("Please enter the following information:")
print()
first = input("First name: ")
last = input("Last name: ")
email = input("Email address: ")
phone = input("Phone number: ")
job = input("Job title: ")
id = input("ID Number: ")
hair = input("Hair: ")
eyes = input("Eyes: ")
month = input("Month Started: ")
train = input("Completed Training(yes/no): ")
print()
print("The ID Card is: ")
print("----------------------------------------------")
print(f"{last.upper()}, {first}")
print(job.title())
print(f"ID: {id}")
print()
print(email.lower())
print(phone)
print()
print(f"Hair: {hair.capitalize()}              Eyes: {eyes.capitalize()}")
print(f"Month: {month.capitalize()}         Traning: {train.capitalize()}")
print("----------------------------------------------")


