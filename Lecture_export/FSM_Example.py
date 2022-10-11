from random import random
from time import sleep


def state0():
    print("State0")
    # Delay is used to simulate some application logic
    sleep(0.5)
    if random() > 0.5:
        return state1
    else:
        return state2


def state1():
    print("State1")
    # Delay is used to simulate some application logic
    sleep(0.5)
    if random() > 0.5:
        return state0
    else:
        return state2


def state2():
    print("State2")
    # Delay is used to simulate some application logic
    sleep(0.5)
    if random() > 0.5:
        return state0
    else:
        return None  # End


# Main Function
if __name__ == "__main__":
    # Initial state
    state = state0
    while state:
        state = state()  # Loop FSM

    print("FSM Done.")
