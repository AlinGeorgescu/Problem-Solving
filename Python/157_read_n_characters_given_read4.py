class Solution:
    def read(self, buf: str, n: int) -> int:
        num_read = 0

        while num_read < n:
            tmp = ''

            count = read4(tmp)
            if not count:
                return num_read

            count = min(count, n - num_read)
            buf += tmp[ : count]
            num_read += count

        return num_read