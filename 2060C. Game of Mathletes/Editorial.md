Sort the array first.

Use two pointers: one starting from the beginning (i) and one from the end (j).

Check the sum of the numbers at positions i and j:

If the sum is greater than k, move the right pointer j leftward (since larger numbers are at the end in a sorted list).

If the sum is less than k, move the left pointer i rightward (to increase the sum).

If the sum is exactly k, count it as a valid pair and move both pointers.

Repeat this process until i < j.
