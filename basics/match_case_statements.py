# Match-Case Statements
# An alternative to using multiple 'elif' statements.
#
# Benefits:
# - Cleaner and more readable syntax
# - Easier to maintain when handling many conditions
#
# Notes:
# - case _ acts as the default/else case
# - | acts as a logical OR between multiple patterns

# -------- Numeric Match-Case Example --------

def day_of_week(day):

    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:
            return "Invalid day."

print(day_of_week(1))

# -------- Weekend Checker (Basic Version) --------

def is_weekend(day):

    match day:
        case "Sunday":
            return True
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wednesday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case "Saturday":
            return True
        case _:
            return False


print(is_weekend("Saturday"))

# -------- Weekend Checker (Using OR Patterns) --------

def is_weekend(day):

    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False

print(is_weekend("Friday"))