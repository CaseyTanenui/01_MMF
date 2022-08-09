# Valid snacks holds list of all snacks, each item in valid snacks is a list with valid options fo each snack <full name, letter code (a-e)
# and possible abbreviations etc
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M", "m&m", "mms", "m", "b"],
    ["Pita Chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]

# initialize variables 
snack_ok = ""
snack = ""

# Loop three times to make testing quicker 
for item in range (0, 3):

    # Ask user for desired snack and put it in lowercase
    desired_snack = input("Snack: ").lower() 

    for var_list in valid_snacks:

        # if the snack is in one of the lists, return the full 
        if desired_snack in var_list:

            # get full name of snack and put it in 
            # in title case so it looks nice when outputted
            snack = var_list[0].title()
            snack_ok = "yes"
            break

        # if the chosen snack is not valid - set snack_ok to no
        else:
            snack_ok = "no"

    if snack_ok == "yes":
        print("Snack Choice: ", snack)
    else:
        print("Inavalid choice")