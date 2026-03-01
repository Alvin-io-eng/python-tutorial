# digits = [1,2,3,4]
# combinations = []
# combination = []

# combinations.append(str(digits))

# print(digits.count(4))

# GEMINI

import itertools

def get_all_combinations(input_list):
    combinations = []
    # Loop through every possible length of combinations (from 1 N)
    for r in range(1,len(input_list) + 1):
        # itertool cobinations handles the math and logic 
        for combo in itertools.combinations(input_list,r):
            combinations.append(combo)
    return combinations

# Example Usage
my_list = [1,2,3]
all_combos = get_all_combinations(my_list)

print(f"Total number of combinations: {len(all_combos)}")
print(f"List of combinations: {all_combos}")
    