from sortedcontainers import SortedSet
from collections import defaultdict
import copy
class Twitter:

    def __init__(self):
        self.followers = {}
        self.user_tweets = defaultdict(SortedSet)
        self.time_counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.followers:
            self.followers[userId] = []
        self.user_tweets[userId].add((self.time_counter, tweetId))
        self.time_counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.followers:
            return []
        followers_id_list = self.followers[userId]
        sorted_set = copy.deepcopy(self.user_tweets[userId])

        for user_id in followers_id_list:
            sorted_set = sorted_set | self.user_tweets[user_id]

        if len(sorted_set) > 10:
            # get the last 10 tweets from the sorted set
            last_10_tweet = sorted_set[-10:]
        else:
            last_10_tweet = sorted_set
        # return the last 10 tweet ids
        return [id for time, id in last_10_tweet][::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = [followeeId]
        else:
            self.followers[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)