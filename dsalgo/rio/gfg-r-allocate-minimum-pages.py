# https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1

"""
You have n books, each with arr[i] a number of pages. 
m students need to be allocated contiguous books, 
with each student getting at least one book.
Out of all the permutations, the goal is to find the permutation 
where the sum of the maximum number of pages in a book allotted to a student 
should be the minimum, out of all possible permutations.

Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).

Examples:

Input: n = 4, arr[] = [12, 34, 67, 90], m = 2
Output: 113
Explanation: Allocation can be done in following ways:
{12} and {34, 67, 90} Maximum Pages = 191
{12, 34} and {67, 90} Maximum Pages = 157
{12, 34, 67} and {90} Maximum Pages =113.
Therefore, the minimum of these cases is 113, which is selected as the output.

Input: n = 3, arr[] = [15, 17, 20], m = 5
Output: -1
Explanation: Allocation can not be done.
"""

"""
Implementing binary search:
- recursive binary search where you first split arr[] down the middle and then with each recursive loop
you check if pages allocated is smaller
- since you're checking min allocated pages, need to go through entire dataset
- what to do when m > 2?
    - just have to think about 1 student, actually?
"""

def allocate_minimum_pages(n, arr, m):
    