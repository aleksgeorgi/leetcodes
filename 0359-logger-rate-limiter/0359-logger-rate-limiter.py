class Logger:

    def __init__(self):
        self.my_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:   
        # case where first time message being printed 
        if message not in self.my_dict:
            self.my_dict[message] = timestamp
            return True
        
        if timestamp - self.my_dict[message] >=10:
            self.my_dict[message] = timestamp 
            return True 
        else:
            return False
        



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)