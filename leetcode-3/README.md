# Leetcode Problem #3

**Problem Title:** Longest Substring Without Repeating Characters
**Date Solved:** November 27, 2021

## Problem

**Difficulty:** Medium

Given a string `s`, find the length of the **longest substring** without repeating characters.

### Example 1

**Input:** s = "abcabcbb"

**Output:** 3

**Explanation:** The answer is "abc", with the length of 3.

### Example 2

**Input:** s = "bbbbb"

**Output:** 1

**Explanation:** The answer is "b", with the length of 1.

### Example 3

**Input:** s = "pwwkew"

**Output:** 3

**Explanation:** The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

### Example 4

**Input:** s = ""

**Output:** 0

## Solution

Test is the given string, `s`, is of length 0 or length 1. If it is, immediately return the length of the string as the longest substring, no computation is necessary.

If the string has more than on character, initialize an auxiliary hash table to use in computing the length of the longest substring. This will allow "look-backs" in constant time and prevent the solution from having to perform nested traversals of the string. Each time a character is encountered, the it will be inserted into the has table using the character as a key, and the index as the value. This will ensure that the last index of the character (within the partially traversed string) is always stored in the hash table for constant time lookup.

Start traversing the string, character by character. For each character, check the auxiliary hash table to determine if it was previously encountered. If it was, a substring of unique characters exists beginning at the index stored in the has table, and ending at the current index - 1. The length of this substring will need to be calculated, and compared to the length of the current longest substring. If it is longer, set the length of the current longest substring to the length of the current substring.

Once the entire string has been traversed, return the length of the longest substring found.

An edge case exists - if the entire string is composed of unique characters, a longest substring will not be detected as no character repeats to trigger the comparison logic. To account for this scenario, the `longest_substring` variable is initialized to `None`, and a comparison is performed after traversal. If `longest_substring` is still `None`, the length of the supplied string is returned.