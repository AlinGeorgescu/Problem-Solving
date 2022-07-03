# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n

        while start <= end:
            mid = (start + end) // 2

            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid

                end = mid - 1
            else:
                start = mid + 1

        return mid_