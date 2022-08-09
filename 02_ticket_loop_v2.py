# Start of loop 

# initialise loop so that it runs atleast once 
name = ""
count = 0 
MAX_TICKETS = 5 
ticket_count = 1

while name != "xxx" and ticket_count < MAX_TICKETS:
    
    # Tells user how many seats are left
    if count < 4: 
        print("You have {} seats left".format(MAX_TICKETS - count))

    else:
        print("You only have one available seat left.")

    # get details
    name = input("Name: ")
    count += 1 
    print()

if count == MAX_TICKETS:
    print("You have sold all of the available tickets!")
else:
    print("You have sold {} tickets. \n There are {} places still available".format(count, MAX_TICKETS - count))