class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time_to_live = timeToLive
        self.mapping_token_time = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.mapping_token_time[tokenId] = currentTime + self.time_to_live

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.mapping_token_time and self.mapping_token_time[tokenId] > currentTime:
            self.mapping_token_time[tokenId] = currentTime + self.time_to_live

    def countUnexpiredTokens(self, currentTime: int) -> int:
        token_values = list(self.mapping_token_time.values())
        token_indexes = list(self.mapping_token_time.keys())

        for i in range(len(token_indexes)):
            if token_values[i] <= currentTime:
                # delete the value from a mapping
                self.mapping_token_time.pop(token_indexes[i])

        return len(self.mapping_token_time)
# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
