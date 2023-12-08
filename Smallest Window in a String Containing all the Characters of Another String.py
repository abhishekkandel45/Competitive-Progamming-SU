from collections import Counter

class Solution:
    def smallestWindow(self, S, P):
        len_s = len(S)
        len_p = len(P)

        if len_s < len_p:
            return "-1"

        # Frequency of characters in P
        count_p = Counter(P)

        # Initializing window and string variables
        start = 0
        end = 0
        min_len = float('inf')
        min_start = 0
        count = 0
        window = Counter()

        # Sliding window approach
        while end < len_s:
            # Expand the window
            window[S[end]] += 1

            # If the character in S exists in P and the count matches
            if S[end] in count_p and window[S[end]] <= count_p[S[end]]:
                count += 1

            # If all characters in P are found in current window
            if count == len_p:
                # Try to minimize the window by removing extra characters from the beginning
                while S[start] not in count_p or window[S[start]] > count_p[S[start]]:
                    if S[start] in count_p and window[S[start]] > count_p[S[start]]:
                        window[S[start]] -= 1
                    start += 1

                # Update the minimum window length and start index
                window_len = end - start + 1
                if window_len < min_len:
                    min_len = window_len
                    min_start = start

            end += 1

        if min_len == float('inf'):
            return "-1"
        else:
            return S[min_start:min_start + min_len]