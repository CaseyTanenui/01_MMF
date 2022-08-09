# number checking function
def int_check(question, low_num, high_num):

    error = "Please enter a number between {} and {}".format(low_num, high_num)

    valid = False
    while not valid:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print(error)


# Main routine
ticket_num = int_check("How many tickets", 1, 50)
print(ticket_num)
