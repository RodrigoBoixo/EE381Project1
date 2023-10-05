from random import random
def create_transmitted_message(prob):
    num = random()
    message = 0 if num <= prob else 1
    return message

def create_received_signal(message, e_0, e_1):
    num = random()
    if message == 0:
        signal = 1 if num <= e_0 else 0
    else:
        signal = 1 if num > e_1 else 0
    return signal

def calculate_conditional_probability(e_0, e_1, num_experiments):
    """Calculates the conditional probability P(R=1|S=1).

    Args:
        e_0: The probability of a 0 bit being received incorrectly.
        e_1: The probability of a 1 bit being received incorrectly.
        num_experiments: The number of experiments to perform.

    Returns:
        The conditional probability P(R=1|S=1).
    """

    num_successes = 0
    for _ in range(num_experiments):
        message = create_transmitted_message(0.35)
        signal = create_received_signal(message, e_0, e_1)
        if message == 1 and signal == 1:
            num_successes += 1

    conditional_probability = num_successes / num_experiments
    return conditional_probability

# Set the transmission error probabilities.
e_0 = 0.01
e_1 = 0.02

# Calculate the conditional probability.
conditional_probability = calculate_conditional_probability(e_0, e_1, 10000)

# Print the conditional probability.
print("Conditional probability P(R=1|S=1):", conditional_probability)