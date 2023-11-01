# 2. Throw 2 6-sided dice simultaneously 10000 times and find the frequency of occurrence of sum of the two values displayed.
# Plot the frequency of occurrence on the terminal like the following
# val1: ****
# val2: ****
# val3: ********
# val4: **************
# val5: *******
# val6: *****
# val7: ****
# etc.
# If you feel comfortable, you may also plot the same with matplotlib.pyplot as a 'histogram'. Draw a 'scatter' plot of the 
# two numbers displayed.


import random
# import matplotlib.pyplot as plt

# one roll  = random.randint(1, 6)
# rolling two 6-sided dice 10,000 times and then adding them and appending into a list
rolls_value = [random.randint(1, 6) + random.randint(1, 6) for _ in range(10000)]

# Calculate the frequency of each sum
frequency = {} #json for key value structure
for roll in rolls_value:
    if roll in frequency:
        frequency[roll] += 1
    else:
        frequency[roll] = 1

# Print the frequency of occurrence as asterisks on the terminal
print("Frequency of Sum Occurrence:")
scale = 15 #to scale down the output
for val, count in sorted(frequency.items()):
    print(f"val{val}: {'*' * int(count/scale)}")

# Create a histogram of the sum frequencies
# plt.hist(rolls_value, bins=range(2, 14), rwidth=0.8, align='left', alpha=0.7, edgecolor='black')
# plt.xlabel("Sum of Two Dice")
# plt.ylabel("Frequency")
# plt.title("Histogram of Sum of Two Dice Rolls")

# # Show a scatter plot of the two dice values
# x = [random.randint(1, 6) for _ in range(10000)]
# y = [random.randint(1, 6) for _ in range(10000)]

# plt.figure()
# plt.scatter(x, y, alpha=0.5)
# plt.xlabel("First Dice")
# plt.ylabel("Second Dice")
# plt.title("Scatter Plot of Two Dice Values")

# # Display the plots
# plt.show()
