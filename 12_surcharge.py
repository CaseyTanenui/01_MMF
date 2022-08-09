# Import Statements
import pandas 
import re

def string_check(choice, options):

    is_valid = ""
    chosen = ""
    
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

# Main routine starts here..

pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

# Loop until exit code...
name = ""
while name != "xxx":
    name = input("What is your name?: ")
    if name == "xxx":
        break

    # Ask for the payment method... 
    how_pay = "Invalid Choice"
    while how_pay == "Invalid Choice":
        how_pay = input("Please choose a payment method first (Cash or card): ").lower()
        how_pay = string_check(how_pay, pay_method)

    # Ask for the subtotal (for testing purposes)
    subtotal = float(input("Sub total? $"))

    if how_pay == "Credit":
        surcharge = 0.05 * subtotal
    else:
        surcharge = 0

    total = subtotal + surcharge

    print("Name: {} | Subtotal: ${:.2f} | Surcharge: ${:.2f} | Total Payable: ${:.2f}".format(name, subtotal, surcharge, total))

    # Calculate Surcharge...