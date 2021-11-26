# Leetcode Problem #1

**Problem Title**: Two Sum
**Date Solved**: November 25, 2021

## Problem

**Difficulty:** Easy

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have **_exactly_ one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

### Example 1

**Input:** nums = [2, 7, 11, 15], target = 9
**Output:** [0, 1] - Because nums[0] + nums[1] == 9, we return [0, 1].

### Example 2

**Input:** nums = [3,2,4], target = 6
**Output:** [1,2]

### Example 3

**Input:** nums = [3,3], target = 6
**Output:** [0,1]

## Solution

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Consider a complement to be a number that, when paired with a specific value, causes the two values
to sum to `target`.

Create an auxiliary hash table (in Python, this will be a dict) to store complements.

Iterate through the `nums` array. For each `num` in `nums`, calculate its complement and perform a look up
against the auxiliary hash table for this value. If it is found, return the index of its complement (stored in the hash table) and the index of the current `num`.

If the complement of the current `num` in `nums` was not found in the lookup table, create a new entry in the lookup table with the current `num` as the key, and the `index` of the current num as the value to allow for it to be discovered as the iteration progresses.

If no pairs are found, return an empty array.