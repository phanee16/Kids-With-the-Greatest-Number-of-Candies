def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
        richest = max(candies)
        for i in range(len(candies)):
            candies[i] = candies[i] + extraCandies >= richest
        return candies
