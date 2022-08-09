import re

# Function goes here 

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

    # if the snack is not Ok - ask question again 

    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"

# Get's the list of snacks 
def get_snack():
    # Regular expression to find if item starts with a number 
    number_regex = "^[1-9]"

    # Valid snacks holds list of all snacks, each item in valid snacks is a list with valid options fo each snack <full name, letter code (a-e)
    # and possible abbreviations etc
    valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M", "m&m", "mms", "m", "b"],
    ["Pita Chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
    ]

    # holds the snack order 
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []

        # Asks user for desired snack and put it in lower case 
        desired_snack = input("Snack ").lower()

        if desired_snack == "xxx":
            return snack_order

        # if item has a number , seperate it into two different numbers 
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]
    
        else:
            amount = 1
            desired_snack = desired_snack

        # Remove the spaces before and after the snack
        desired_snack = desired_snack.strip()

        # Checks if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)

        # Checks snack amount is valid (less than 5)
        if amount >= 5:
            print("Sorry - we have a four snack maximum")
            snack_choice = "invalid choice"

        snack_row.append(amount)
        snack_row.append(snack_choice)
            
        # Add snack and amount to list 
        amount_snack = "{} {}".format(amount, snack_choice)

        # checks that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_choice)

# Main routine starts here

# Valid options for yes/no
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# Checks to see if user would like a snack 
check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want to order snacks? ").lower()
    check_snack = string_check(want_snack, yes_no)

# If they say yes - ask what snacks they want
if check_snack == "Yes":
    get_order = get_snack()

else:
    get_order = [] 

# show snack order
print()
if len(get_order) == 0:
    print("Snacks Ordered: None")
    
else:
    print("Snacks ordered:")

    for item in get_order:
        print(item)

    print(get_order)