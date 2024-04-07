import sys

type = sys.argv[1]

if type == "t2.micro":
    print("This will cost $2 per day")
elif type == "t2.medium":
    print("This will cost $4 per day")
else:
    print("Please provide a valid instance type")