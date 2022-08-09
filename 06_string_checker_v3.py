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

# Valid snacks holds list of all snacks, each item in valid snacks is a list with valid options fo each snack <full name, letter code (a-e)
# and possible abbreviations etc
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M", "m&m", "mms", "m", "b"],
    ["Pita Chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]

# Valid options for yes/no
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]
 
# holds the snack order 
snack_order = []

# Checks to see if user would like a snack 
check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want to order snacks? ").lower()
    check_snack = string_check(want_snack, yes_no)

# If they say yes, ask what snacks they want (and add to our snacks)
if check_snack == "Yes":

    desired_snack = ""
    while desired_snack != "xxx":
        # ask user for desired snack and put it in lowercase
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            break 

        # Checks to see if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)
        print("Snack Choice: ", snack_choice)

        # add snacks to list...

        # checks that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_choice)

# show snack order
print()
if len(snack_order) == 0:
    print("Snacks Ordered: None")

else:
    print("Snacks ordered:")

    for item in snack_order:
        print(item)

