class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        last_accepted_time = t - 3000
        for index in range(len(self.requests)):
            if self.requests[index] >= last_accepted_time:
                self.requests = self.requests[index:]
                break
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)