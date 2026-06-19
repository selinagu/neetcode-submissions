class Twitter:

    def __init__(self):
        self.twitter = defaultdict(list)
        self.time = 0
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.twitter[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        follows = self.follows[userId]
        follows.add(userId)

        news_feed = []
        res = []
        for followee in follows:
            news = self.twitter[followee][-10:]
            for a in news:
                heapq.heappush(news_feed, a)

        num = 0
        while news_feed:
            _, tweet = heapq.heappop(news_feed)
            num += 1
            res.append(tweet)
            if num == 10:
                break

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
