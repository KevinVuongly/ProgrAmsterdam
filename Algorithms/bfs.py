from Board import Board
from ReadBoard import ReadBoard
import sys

data = ReadBoard("../data/game1.csv")
game = Board(data.gridSize, data.changeable, data.fixed, data.direction, data.length)

"""
class Bfs()

def get_breadth_first_nodes(Board):
    nodes = []
    stack = [Board]
    while stack:
        cur_node = stack[0]
        stack = stack[1:]
        nodes.append(cur_node)
        for child in cur_node.get_children():
            stack.append(child)
    return nodes


   class Node(object):
    def __init__(self, id_):
        self.id = id_
        self.children = []
        
    def __repr__(self):
        return "Node: [%s]" % self.id
    
    def add_child(self, node):
        self.children.append(node) 
    
    def get_children(self):
        return self.children         
    
    def get_rev_children(self):
        children = self.children[:]
        children.reverse()
        return children  
 """