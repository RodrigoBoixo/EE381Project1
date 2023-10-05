from random import random
def create_transmitted_message(prob):
    num = random()
    message = 0 if num <= prob else 1
    return message

def create_received_signal(message, e_0, e_1):
    num = random()
    if message == 0:

        if num <= e_0:
            signal = 1
        else:
            signal = 0
    else:
        if num > e_1:
            signal = 1
        else:
            signal = 0
    return signal

e_0_prob = 0.01
e_1_prob = 0.02
N = 100000
num_successes = 0
for _ in range(N):
    message = create_transmitted_message(e_1_prob)  # Only consider transmissions where S = 1.
    signal = create_received_signal(message, e_0_prob, e_1_prob)
    if message == signal:
        num_successes += 1

conditional_probability = num_successes / N

print("Conditional probability PR(R=1|S=1):", conditional_probability)