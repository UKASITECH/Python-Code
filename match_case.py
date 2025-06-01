# Get input from the user
day = input("Enter a day of the week (e.g., Monday, Tuesday): ")

# Use match-case to print a message based on the day
match day:
    case "Monday":
        print("It's the start of the work week!")
    case "Tuesday":
        print("It's Tuesday, keep going!")
    case "Wednesday":
        print("It's the middle of the week, halfway there!")
    case "Thursday":
        print("It's Thursday, almost the weekend!")
    case "Friday":
        print("It's Friday, the weekend is near!")
    case "Saturday":
        print("It's Saturday, enjoy your weekend!")
    case "Sunday":
        print("It's Sunday, time to relax before the week starts again!")
    case _:
        print("That's not a valid day of the week.")
