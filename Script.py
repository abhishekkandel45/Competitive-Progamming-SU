import os

# Define file names
files = [
    "Chocolate Distribution Problem.py",
    "Search in Rotated Sorted Array.py",
    "Next Permutation.py",
    "Best time to Buy and Sell Stock.py",
    "Repeat and Missing Number Array.py",
    "Kth-Largest Element in an Array.py",
    "Trapping Rain Water.py",
    "Product of Array Except Self.py",
    "Maximum Product Subarray.py",
    "Find Minimum in Rotated Sorted Array.py",
    "Find Pair with Sum in Sorted & Rotated Array.py",
    "3Sum.py",
    "Container With Most Water.py",
    "Given Sum Pair.py",
    "Kth - Smallest Element.py",
    "Merge Overlapping Intervals.py",
    "Group Anagrams.py",
    "Longest Palindromic Substring.py",
    "Palindromic Substrings.py",
    "Next Permutation.py",
    "Count Palindromic Subsequences.py",
    "Smallest Window in a String Containing all the Characters of Another String.py",
    "Wildcard String Matching.py",
    "Longest Prefix Suffix.py",
    "Rabin-Karp Algorithm for Pattern Searching.py",
    "Transform One String to Another using Minimum Number of Given Operation.py",
    "Minimum Window Substring.py",
    "Reorder List.py",
    "Detect and remove loop in a linked list.py",
    "Write a Function to get the Intersection Point of two Linked Lists.py",
    "Flatten a linked list with next and child pointers.py",
    "Linked list in zig-zag fashion.py",
    "Reverse a doubly linked list.py",
    "Delete nodes which have a greater value on right side.py",
    "Segregate even and odd Elements in a Linked List.py",
    "Point to next higher value node in a linked list with an Arbitrary Pointer.py",
    "Rearrange a given linked list in place.py",
    "Sort Biotonic Doubly Linked Lists.py",
    "Merge K Sorted Lists.py",
    "Merge sort for linked list.py",
    "Quicksort on singly-linked list.py",
    "Sum of two linked lists.py",
    "Stack permutations check if an array is stack permutation of other.py",
    "simplify-path.py",
    "Sort a stack using Recursion.py",
    "Queue based approach for first non repeating character in a stream.py",
    "The Celebrity Problem.py",
    "Next larger Element.py",
    "Distance of nearest cell.py",
    "Rotten-oranges.py",
    "Next smaller element.py",
    "Circular-tour.py",
    "Efficiently implement k-stacks single array.py",
    "The celebrity problem.py",
    "Iterative tower of hanoi.py",
    "Find the maximum of minimums for every window size in a given array.py",
    "lru cache implementation.py",
    "Find a tour that visits all stations.  for exmple: Chocolate Distribution Problem.py",
]

# Create each file with empty content
for file in files:
    with open(file, "w"):
        pass

print("Created the following files:")
for file in files:
    print(f"\t- {file}")
