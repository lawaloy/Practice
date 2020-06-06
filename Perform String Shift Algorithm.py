Complexity Analysis

Let LL be the length of the string and NN be the length of the shift array. Both sub-approaches here have the same complexity analysis.

Time complexity : O(N + L)O(N+L).

The algorithms presented in Approach 2 both break the task into two sub-steps: calculating an overall shift and applying the shift. We'll analyze these one at a time and then combine the results.

The first step loops through each of the NN entries in the shift array, adding up the total number of left shifts and the total number of right shifts. Handling each entry is an O(1)O(1) operation, so this first step has a total cost of O(N)O(N).

The second step applies a single string-shift operation. As discussed in the previous approach, a string-shift operation has a cost of O(L)O(L).

Because we are doing these steps one-after-the-other, and we don't know whether NN or LL is bigger, we add them to get a final time complexity of O(N + L)O(N+L).

Space complexity : O(L)O(L).

The first step uses constant extra space to keep track of the counts. This leaves us with the space complexity of modifying a string, which, as discussed before, requires auxiliary space of O(L)O(L).

As stated in the previous approach, it is possible to get the space complexity down to O(1)O(1) by using a language with mutable strings.
