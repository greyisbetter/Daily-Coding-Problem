# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 11:20:28 2022

@author: Kushan
"""

from typing import Tuple

class XORNode:
    def __init__(self, data: int, prev: int, next: int) -> None:
        self.data = data
        self.npx = id(next) ^ id(prev)
        
    def next_node(self, prev_idx: int) -> int:
        return self.npx ^ prev_idx
    
    def prev_node(self, next_idx: int) -> int:
        return self.npx ^ next_idx
        
class XORLinkedList:
    def __init__(self):
        self.memory = [(XORNode(None, -1, -1))]
        
    def head(self) -> Tuple[int, int, XORNode]:
        # head node index, prev node index, head node
        return 0, -1, self.memory[0]
        
    def add(self, val: int) -> None:
        current_node_index, previous_node_index, current_node = self.head()
        while True:
            # walk down the list until the end is found
            next_node_index = current_node.next_node(previous_node_index)
            if next_node_index == -1:
                # the end is reached
                break
            previous_node_index, current_node_index = (
                current_node_index,
                next_node_index,)
            current_node = self.memory[next_node_index]
        # allocation
        new_node_index = len(self.memory)
        current_node.npx = previous_node_index ^ new_node_index
        self.memory.append(XORNode(val, current_node_index, -1))
        
            
    def printList(self):
        temp = self.tail
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
        
        
def value(id):
    return ctypes.cast(id, ctypes.py_object).value
        
if __name__ == "__main__":
    llist = XORLinkedList()
    
    # create three node
    llist.add(5)
    llist.add(6)
    llist.add(7)
    llist.add(8)
    
    
   # print(llist.head.data)

    #traverse(llist.head)
    # llist.printList()      

    print(llist.head.data)     
    print(llist.head.npx.data)
    