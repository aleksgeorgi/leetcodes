class MovingAverage:

    def __init__(self, size: int):
        # queue to store the objects data 
        self.size = size
        self.q = deque()
        self.window_sum = 0 
        self.count = 0

    def next(self, val: int) -> float:
        # will perform the queue updating and avg calculation 
        self.count +=1
        
        self.q.append(val)

        
        tail = self.q.popleft() if self.count > self.size else 0 
        
        self.window_sum = self.window_sum - tail + val

        return self.window_sum/(min(self.count, self.size))
            
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

        '''
        the value we're passing in, gets added to the right side of the queue 
        and the left side of the queue gets popped off
        then the average is calculated 


        '''