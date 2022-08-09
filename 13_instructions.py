# Checks to see the users valid responses to the questions that are asked
# if not valid , shows error message
def string_check(choice, options):

    for var_list in options:

        # if the snack is in one of the lists, return the full item
        if choice in var_list:

            # Get full name of snack 

            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # If the options are not valid - set not_valid to no 
        else:
            is_valid = "no"

    # if the snack os not Ok - ask question again 

    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"

def instructions(options):
    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = input("Would you like to read the instructions?")
        show_help = string_check(show_help, options)

    if show_help == "Yes":
        print()
        print("** Mega Movie Fundraiser Instructions **")
        print()
        print("Instructions go here, they are brief but helpful..")

    return ""

# Main routine starts here..
# The list for valid yes / no responses
yes_no = [
    ["yes", "y"]
    ["no", "n"]
]

# Ask if the instructions are needed
instructions(yes_no)
print()
print("Program Launches..")


