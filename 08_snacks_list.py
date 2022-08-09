# Import Statements
import pandas
import re 

# Initialize snacks lists...

all_names = ['Rangi', 'Manaia', 'Talia', 'Arihi', 'Fetu']

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snacks_lists = [popcorn, mms, pita_chips, water, orange_juice]

movie_data_dict = {
    'Name': all_names,
    'Popcorn':popcorn,
    'Water':water,
    'Pita Chips':pita_chips,
    'M&M':mms,
    'Orange Juice':orange_juice
}

test_data = [
    [[2, 'Popcorn'], [1, 'Pita Chips'], [1, 'Orange Juice']],
    [[]],
    [[1, 'Water']],
    [[1, 'Popcorn'], [1, 'Orange Juice']],
    [[1, 'M&M'], [1, 'Pita Chips'], [3, 'Orange Juice']]
]

count = 0
for client_order in test_data:

    # Assume no snacks have been bought...
    for item in snacks_lists:
        item.append(0)

# Print(snacks_list)

# Get order (hard coded for easy testing...)
snack_order = test_data[count]
count += 1

for item in snack_order:
    if len(item) > 0:
        to_find = (item[1])
        amount = (item[0])
        add_list = movie_data_dict[to_find]
        add_list[-1] = amount

# Prints the names 
print()
print("Names: ", all_names)
print("Popcorn: ", snacks_lists[0])
print("M&Ms: ", snacks_lists[1])
print("Pita Chips: ", snacks_lists[2])
print("Water: ", snacks_lists[3])
print("Orange Juice: ", snacks_lists[4])
print()

# Print details 
movie_frame = pandas(movie_data_dict)
movie_frame = movie_frame.set_index('Name')
print(movie_frame)