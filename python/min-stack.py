class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min=[]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.min and self.min[-1]<val:
            return
        self.min.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self.min[-1]==self.stack[-1]:
            self.min.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
