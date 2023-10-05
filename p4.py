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

def decode_triplet(triplet):


    if triplet[0] == triplet[1] == triplet[2]:
        return triplet[0]
    elif triplet[0] == triplet[1] != triplet[2]:
        return triplet[0]
    elif triplet[1] == triplet[2] != triplet[0]:
        return triplet[1]
    else:
        return triplet[2]

def simulate_experiment(e_0, e_1, num_experiments):

    num_failures = 0
    for _ in range(num_experiments):
        # Transmit the bit "S" three times.
        message = create_transmitted_message(0.35)
        message1 = message
        message2 = message
        message3 = message

        # Create the received signal.
        signal1 = create_received_signal(message1, e_0, e_1)
        signal2 = create_received_signal(message2, e_0, e_1)
        signal3 = create_received_signal(message3, e_0, e_1)

        # Decode the received triplet.
        decoded_bit = decode_triplet((signal1, signal2, signal3))

        # If the decoded bit is not equal to the transmitted bit, then the experiment is a failure.
        if decoded_bit != message:
            num_failures += 1

    return num_failures

# Set the transmission error probabilities.
e_0 = 0.01
e_1 = 0.02

# Simulate the experiment 10,000 times.
num_failures = simulate_experiment(e_0, e_1, 10000)

# Calculate the probability of failure.
probability_of_failure = num_failures / 1000

# Print the probability of failure.
print("Probability of failure:", probability_of_failure)