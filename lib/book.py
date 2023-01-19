#!/usr/bin/env python3
import pdb
class Book:
    def __init__(self, title):
        self.title = title
        
    def set_page_count(self, page_count):
        if (type(page_count) is int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
            
    def get_page_count(self):
        # pdb.set_trace()
        if "_page_count" in self.__dict__:
            return self._page_count 
    
    page_count = property(get_page_count, set_page_count,)
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
