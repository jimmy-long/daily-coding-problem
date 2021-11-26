from typing import List

class Solution:

    @classmethod
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # Keep track of numbers that are needed to cause a previously encountered
        # number to sum to target
        complements = {}
        
        for index, num in enumerate( nums ):
            complement = target - num

            if complement in complements:
                return [ complements[ complement ], index ]

            complements[ num ] = index

        return []