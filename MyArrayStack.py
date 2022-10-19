import numpy as np

class MyArrayStack():
    '''
    ArrayStack: Implementation of the Stack interface based on numpy Arrays. 
    '''
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n: int) -> np.array:
        '''
        Generates new numpy array of zeroes

        Parameters:
        n (int): size of array to be created

        Returns:
        np.array: numpy array of zeroes of n size
        '''
        return np.zeros(n, object)
    
    def resize(self):
        '''
        Resizes the array
        '''
        b = self.new_array(max(1, 2 * self.n))
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b

    def get(self, i : int) -> object:
        '''
        Returns the value at index i 

        Parameters:
        i (int): index of object to be returned

        Returns:
        object: object stored in index i 
        '''
        if i < 0 or i >= self.n: raise IndexError()
        return self.a[i]
    
    def set(self, i : int, x : object) -> object:
        '''
        Sets object x as the value for index i

        Parameters:
        i (int): index at which to place object x
        x (object): object to insert 

        Returns:
        object: object replaced by the new object x 
        originally stored in index i
        '''
        if i < 0 or i > self.n: raise IndexError()
        y = self.a[i]
        self.a[i] = x
        return y
    
    def add(self, i: int, x : object) :
        '''
        Shift all j > i one position to the right
        and add element x in position i

        Parameters:
        i (int): index to insert object x
        x (object): object to insert at index i
        '''
        if i < 0 or i > self.n: raise IndexError()
        if self.n == len(self.a):
            self.resize()
        index = self.n
        while index > i:
            self.a[index] = self.a[index-1]
            index-=1
        self.a[i] = x
        self.n+=1

    def remove(self, i : int) -> object :
        '''
        Remove element i and shift all j > i one 
        position to the left

        Parameters: 
        i (int): index of value to remove

        Returns:
        object: the value removed from index i
        '''
        if i < 0 or i > self.n: raise IndexError()
        x = self.a[i]
        for i in range (i, self.n - 1):
            self.a[i] = self.a[i + 1]
        self.n -= 1
        if len(self.a) >= 3 * self.n:
            self.resize()
        return x

    def push(self, x : object) :
        '''
        Adds an object x to the end of the arraystack

        Parameters:
        x (object): object to be pushed
        '''
        self.add(self.n, x)
    
    def pop(self) -> object :
        '''
        Removes and returns last value in arraystack
        '''
        return self.remove(self.n-1)

    def peek(self) -> object :    
        '''
        Returns last value in arraystack
        '''
        a = self.a[self.n - 1]
        return a

    def size(self) :
        '''
        Returns the size of the stack
        '''
        return self.n
        
    def __str__(self) -> str:
        '''
        Returns string with the content of the arraystack where
        object contents are converted to their string forms
        '''
        s = "["
        for i in range(0, self.n):
            s += "%r" % str(self.a[i])
            if i  < self.n-1:
                s += ","
        return s + "]"
