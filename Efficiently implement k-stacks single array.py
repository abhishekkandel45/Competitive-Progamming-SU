from os import *
from sys import *
from collections import *
from math import *

class NStack:
    def __init__(self, n, s):
        self.stack_size = s  # Size of each stack
        self.num_stacks = n  # Number of stacks
        self.array = [0] * (n * s)  # Initialize array to hold all stacks
        self.stack_pointers = [-1] * n  # Keep track of top element index for each stack

    # Pushes 'x' into the Mth stack. Returns True if it gets pushed into the stack, and False otherwise.
    def push(self, x, m):
        if m < 0 or m >= self.num_stacks:
            return False  # Invalid stack number

        if self.stack_pointers[m] < self.stack_size - 1:
            self.stack_pointers[m] += 1
            self.array[self._get_index(m)] = x
            return True
        return False  # Stack overflow

    # Pops top element from Mth Stack. Returns -1 if the stack is empty, otherwise returns the popped element.
    def pop(self, m):
        if m < 0 or m >= self.num_stacks:
            return -1  # Invalid stack number

        if self.stack_pointers[m] >= 0:
            popped = self.array[self._get_index(m)]
            self.stack_pointers[m] -= 1
            return popped
        return -1   # Stack underflow

    # Helper function to get the index for a particular stack
    def _get_index(self, m):
        return m * self.stack_size + self.stack_pointers[m]

