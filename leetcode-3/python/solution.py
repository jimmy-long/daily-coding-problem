class Solution:

    @classmethod
    def length_of_longest_substring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        # Initialize an auxiliary hash table for O(1) lookups of previous indicies
        char_map = {}
        longest_substring = None

        for index, char in enumerate( s ):
            if char in char_map:
                curr_substring_length = index - char_map[ char ]

                if longest_substring is None or curr_substring_length > longest_substring:
                    longest_substring = curr_substring_length

            char_map[ char ] = index

        if longest_substring is None:
            return len( s )

        return longest_substring