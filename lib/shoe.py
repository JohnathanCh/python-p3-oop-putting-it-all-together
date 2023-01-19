#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand):
        self.brand = brand
        
    def set_size(self, size):
        if type(size) == int:
            self._size = size
        else:
            print("Size must be an integer")
    
    def get_size(self):
        if "_size" in self.__dict__:
            return self._size
    
    size = property(get_size, set_size)
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")