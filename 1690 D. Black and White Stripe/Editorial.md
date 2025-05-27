To efficiently solve this problem within the given constraints, we utilize the Sliding Window Technique.

The idea is to:

Track the number of 'W' characters in every window (substring) of size k.

Minimize the number of white cells within those windows, as each white cell represents one required recoloring.

Since we’re dealing with consecutive characters, a sliding window is optimal because it allows us to:

Add the effect of the new character entering the window.

Remove the effect of the character leaving the window.

Maintain an updated count with O(1) operations per slide.

