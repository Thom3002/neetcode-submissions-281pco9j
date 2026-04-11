from typing import List
import heapq

# O(n log n) n -> users num
class LeaderBoard:
    class User:
        def __init__(self, userId: str, playersIds: List[str]) -> None:
            self.userId = userId
            self.playersIds = playersIds
            self.score = 0
            pass

    def __init__(self) -> None:
        self.players = {}
        self.users = []
        self.userIds = set()


    def addUser(self, userId: str, playersIds: List[str]) -> None:
        if userId in self.userIds:
            raise Exception("UserId already in use")
        tmp_score = 0
        for p in playersIds: # O(p)
            if p not in self.players:
                self.players[p] = 0
            tmp_score += self.players[p]

        self.users.append(self.User(userId, playersIds))
        self.users[-1].score = tmp_score
        self.userIds.add(userId)



    def addScore(self, playerId: str, score: int) -> None:
        if playerId not in self.players: # maybe change
            raise Exception("Player not defined")
        self.players[playerId] += score

        for user in self.users: # O(u * p)
            if playerId in user.playersIds:
                user.score += score


    def getTopK(self, k: int) -> List[str]:
        heap = []

        for user in self.users: # O(u log u)
            heapq.heappush(heap, (-user.score, user.userId))

        topk = heapq.nsmallest(k, heap) #O(k log u)
        res = []
        for user in topk: #(O(k))
            res.append(user[1])

        return res


lb = LeaderBoard()

lb.addUser("uA", ["p1", "p2"])

lb.addUser("uB", ["p2"])

print(lb.getTopK(2))

lb.addScore("p2", 10)
print(lb.getTopK(2))

lb.addScore("p1", 3)       # p1 = 3; uA=13, uB=10
print(lb.getTopK(1))              # ["uA"]

lb.addScore("p2", -5)      # p2 = 5; uA=8 (3+5), uB=5
print(lb.getTopK(5))              # return all users: ["uA", "uB"]
