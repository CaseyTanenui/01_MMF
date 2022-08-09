# Functions go here     

def not_blank(question):    
    valid = False 

    while not valid: 
        response = input(question)

        if response != "":
            return response 
        else: 
            print("sorry - this cant be blank")


# Main routine goes here 
name = not_blank("Name: ")