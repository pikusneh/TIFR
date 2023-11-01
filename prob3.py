

import random

with open('numbers.txt', 'r') as file:
    lines = file.readlines()
    for i in range(0, len(lines), 10):
        print(' '.join(lines[i:i+10]))

with open('numbers.txt', 'r') as file:
    lines = file.readlines()

# Generate a random number between 5 and 15
num_entries = random.randint(5, 15)

# Randomly select 'num_entries' lines and save them to multi_numbers.txt
random_entries = random.sample(lines, num_entries)
with open('multi_numbers.txt', 'w') as outfile:
    outfile.writelines(random_entries)

with open('multi_numbers.txt', 'r') as file:
    lines = file.readlines()
    formatted_lines = [' '.join(lines[i:i+10]) for i in range(0, len(lines), 10)]
    for line in formatted_lines:
        print(line)