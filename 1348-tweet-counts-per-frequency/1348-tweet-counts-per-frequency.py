from collections import defaultdict
import bisect

class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> list[int]:
        if freq == "minute":
                interval = 60
        elif freq == "hour":
            interval = 3600
        else: # "day"
            interval = 86400

        times = self.tweets[tweetName]
        # Nb of chunks
        n_chunks = (endTime - startTime) // interval + 1
        counts = [0] * n_chunks

        #For each chunk, count tweets in [chunk_start, chunk_end]
        for i in range(n_chunks):
            chunk_start = startTime + i * interval
            chunk_end = min(endTime, chunk_start + interval - 1)
            left = bisect.bisect_left(times, chunk_start)
            right = bisect.bisect_right(times, chunk_end)
            counts[i] = right - left

        return counts