import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
random_numbers = np.random.random(size=4)
print(random_numbers)
heads = random_numbers < 0.5
print(heads)
print(np.sum(heads))

n_all_heads = 0

for _ in range(10000):
    heads = np.random.random(size=4) < 0.5
    n_heads = np.sum(heads)
    if n_heads == 4:
        n_all_heads += 1

res = n_all_heads / 10000

print(n_all_heads)



# Seed the random number generator
np.random.seed(42)

# Initialize random numbers: random_numbers
random_numbers = np.empty(100000)

# Generate random numbers by looping over range(100000)
for i in range(100000):
    random_numbers[i] = np.random.random()

# Plot a histogram
_ = plt.hist(random_numbers)

# Show the plot
plt.show()

def perform_bernoulli_trials(n, p):
    """Perform n Bernoulli trials with success probability p
    and return number of successes."""
    # Initialize number of successes: n_success
    n_success = ____


    # Perform trials
    for i in ____:
        # Choose random number between zero and one: random_number


        # If less than p, it's a success so add one to n_success
        if ____:
            ____

    return n_success