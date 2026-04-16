class Twitter:
    # 1. There should be a new class called User 
    # Each user will have its id, and a list of users that he follows 
    # Each user will also have its on min heap that contains date (can be a index) and the twitter id: [0, 123] for example. 
    # 

    

    class User:
        def __init__(self, id: int):
            self.id = id
            self.posts = []
            self.following = []
            self.news_feed = []
        
        def follow(self, followee):
            if followee != self and followee not in self.following:
                self.following.append(followee)
        
        def unfollow(self, followee):
            if followee in self.following:
                self.following.remove(followee)
        
        def getNewsFeed(self):
            news_feed = []
            for user in self.following:
                news_feed.extend(user.posts)

            news_feed.extend(self.posts)
            if not news_feed:
                return []
            heapq.heapify(news_feed)
            
            nsmallest_posts = heapq.nlargest(10, news_feed)
            res = [tweetId for ts, tweetId in nsmallest_posts]
            return res

        def postTweet(self, timestamp, tweetId: int):
            self.posts.append((timestamp, tweetId))


    def __init__(self):
        self.id_to_users = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.id_to_users:
            new_user = self.User(userId)
            self.id_to_users[userId] = new_user
        
        self.id_to_users[userId].postTweet(self.timestamp, tweetId)
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.id_to_users:
            new_user = self.User(userId)
            self.id_to_users[userId] = new_user
        return self.id_to_users[userId].getNewsFeed()

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.id_to_users:
            self.id_to_users[followerId] = self.User(followerId)
        if followeeId not in self.id_to_users:
            self.id_to_users[followeeId] = self.User(followeeId)
        self.id_to_users[followerId].follow(self.id_to_users[followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.id_to_users:
            self.id_to_users[followerId] = self.User(followerId)
        if followeeId not in self.id_to_users:
            self.id_to_users[followeeId] = self.User(followeeId)
        self.id_to_users[followerId].unfollow(self.id_to_users[followeeId])
