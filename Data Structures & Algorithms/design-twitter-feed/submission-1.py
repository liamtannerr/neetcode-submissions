class Twitter:

    def __init__(self):
        # Followees: {userid: [followees]}
        # Tweets: {userid: [tweets]}
        self.followees = {}
        self.tweets = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((-self.count, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:

        heap = []
        if userId in self.tweets:
            heap.extend(self.tweets[userId])

        if userId in self.followees:
            for user in self.followees[userId]:
                if user in self.tweets:
                    heap.extend(self.tweets[user])

        heapq.heapify(heap)

        res = []
        for _ in range(10):
            if heap:
                _, tweet = heapq.heappop(heap)
                res.append(tweet)

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None: 
        if followerId not in self.followees:
            self.followees[followerId] = {followeeId}
        else:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followees:
            self.followees[followerId].discard(followeeId)

        
