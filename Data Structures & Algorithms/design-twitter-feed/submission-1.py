class Twitter:

    def __init__(self):
        self.follows = dict()
        self.tweets = dict()
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:

        max_heap = []
        heapq.heapify(max_heap)
        feed = []

        sources = set(self.follows.get(userId, set()))
        sources.add(userId)
        
        for source_id in sources:
            tweet_list = self.tweets.get(source_id, [])
            if tweet_list:
                last_idx = len(tweet_list) - 1
                t, tweet_id = tweet_list[last_idx]
                heapq.heappush(max_heap, (-t, tweet_id, source_id, last_idx))
            
        while max_heap and len(feed) < 10:
            _, tweet_id, source_id, idx = heapq.heappop(max_heap)
            feed.append(tweet_id)

            if idx > 0:
                prev_idx = idx - 1
                t, prev_tweet_id = self.tweets[source_id][prev_idx]
                heapq.heappush(max_heap, (-t, prev_tweet_id, source_id, prev_idx))
        
        return feed


        

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId != followeeId:
            if followerId not in self.follows:
                self.follows[followerId] = set()
            
            self.follows[followerId].add(followeeId)


        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)
        
