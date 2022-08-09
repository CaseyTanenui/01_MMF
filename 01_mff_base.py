# import statement...
import re 
import pandas

# functions go here...

# Checks that the ticket name is not blank...
def not_blank(question, error_message):
    valid = False 

    while not valid: 
        response = input(question)

        if response != "":
            return response 
        else: 
            print(error_message)

# Checks for a integer more than 0...
def int_check(question): 
  
  error = "Please enter a whole number between 12 and 130"

  valid = False 
  while not valid:

    try:
      response = int(input(question))

      if response <= 0:
        print(error)
      else:
        return response

    except ValueError:
      print(error)

# Checks number of tickets left and warns user
# If the maximum has been aproached 
def check_tickets(tickets_sold, ticket_limit):
    # Tells user how many seats are left
    if ticket_count < MAX_TICKETS - 1: 
        print("You have {} seats left".format(MAX_TICKETS - ticket_count))
    # Warns the user that there is only one seat left.
    else:
        print("You only have one available seat left.")
    # Returns the statement
    return ""

# Tickets prices based off their ages
def get_ticket_price():

    # Gets age between 12 and 120
    age = int_check("Age: ")

    # Checks that age is valid...
    if age < 12:
        print("Sorry you are too young for this movie")
        return "Invalid Ticket Price"
    elif age > 120:
        print("That is very old - this must be a mistake on your part")
        return "Invalid Ticket Price"

    if age < 12:
        ticket_price = 7.5
    elif age < 120:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    return ticket_price
    
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

# Get's the list of snacks 
def get_snack():

    # Regular expression to find if item starts with a number 
    number_regex = "^[1-9]"

    # Valid snacks holds list of all snacks, each item in valid snacks is a list with valid options fo each snack <full name, letter code (a-e)
    # and possible abbreviations etc
    valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&Ms", "M&M", "m&m", "mms", "m", "b"],
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
            snack_order.append(snack_row)

# Main routine starts here...

# Setup dictionaries / lists needed to hold the data

# the list for valid yes / no responses
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# the lists for valid surcharge responses
pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

# initialise loop so that it runs atleast once 
MAX_TICKETS = 5 

name = ""
ticket_count = 0 
ticket_sales = 0

# Initialize list (to make data-frame in due course)
all_names = []
all_tickets = []

# Snacks Lists...
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snacks_lists = [popcorn, mms, pita_chips, water, orange_juice]

# store surcharge multiplier
surcharge_mult_list = []

# Data frame dictionaries 
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn':popcorn,
    'Water':water,
    'Pita Chips':pita_chips,
    'M&Ms':mms,
    'Orange Juice':orange_juice,
    'Surcharge Multiplier': surcharge_mult_list
}

# Cost of each snack...
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25
}

# Loop to get ticket details
while name != "xxx" and ticket_count < MAX_TICKETS:

    # Checks to see if the limit has not been exceeded
    check_tickets(ticket_count, MAX_TICKETS)

    # Get name (cannot be blank)
    name = not_blank("Name: ", "sorry - name cannot be blank")

    # End the loop if the exit code is typed
    if name == "xxx":
        break

    # Get ticket price based off their age 
    ticket_price = get_ticket_price()

    # If the age is invalid - restart the loop (and get the name again)
    if ticket_price == "Invalid ticket price":
        continue

    ticket_count += 1 
    ticket_sales += ticket_price

    # add name and ticket price to lists
    all_names.append(name)
    all_tickets.append(ticket_price)

    # Get snacks 
    # ask the user if they want a snack
    check_snack = "Invalid choice"
    while check_snack == "Invalid choice":
        want_snack = input("Do you want to order a snack(s)?: ")
        check_snack = string_check(want_snack, yes_no)

    # If they say yes , ask what snacks they want (and loop)
    if check_snack == "Yes":
        snack_order = get_snack()
    else:
        snack_order = []

    # Assume no snacks have been brought...
    for item in snacks_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1]=amount

    # Ask for the payment method... 
    how_pay = "Invalid Choice"
    while how_pay == "Invalid Choice":
        how_pay = input("Please choose a payment method first (Cash or card): ").lower()
        how_pay = string_check(how_pay, pay_method)

    # working credit or cash 
    if how_pay == "Credit":
        surcharge_multiplier = 0.05 
    else:
        surcharge_multiplier = 0
    
    surcharge_mult_list.append(surcharge_multiplier)

# End of tickets / snacks / payment loop...

# Create dataframe and set index to name collumn
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

# Create collumn called 'Sub-Total'
# Fill it prace for snacks and tickets

movie_frame["Sub Total"] = \
    movie_frame['Ticket'] + \
    movie_frame['Popcorn']*price_dict['Popcorn'] + \
    movie_frame['Water']*price_dict['Water'] + \
    movie_frame['Pita Chips']*price_dict['Pita Chips'] + \
    movie_frame['M&Ms']*price_dict['M&Ms'] + \
    movie_frame['Orange Juice']*price_dict['Orange Juice'] 

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + \
    movie_frame['Surcharge']

# Shorten collumn names...
movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ', 'Pita Chips': 'Chips', 'Surcharge Multiplier': 'SM'})

# Setup Columns to be printed..
pandas.set_option('display.max_columns', None)

# Display number to 2 dp..
pandas.set_option('precision', 2)

print_all = input("Print all columns?? (y) for yes ")
if print_all == "y":
    print(movie_frame)
else:
    print(movie_frame[['Ticket', 'Sub Total', 'Surcharge', 'Total']])

print()

# Calculate ticket profit...
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket Profit : ${:.2f}".format(ticket_profit))

# Tells users if they have unsold tickets
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
