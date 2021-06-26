class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# divide number from bet of its factors
def divideBet(n):
    quotient = n
    for i in range(1, n+1):
        x = divmod(n, i)
        if x[1] == 0:
            divisor = i
            if divisor == x[0]:
                quotient = x[0]
                break
            
            if divisor == quotient:
                divisor = x[0]
                break
            
            quotient = x[0]
            
    return (divisor, quotient)

# automated insertion in manner of prime factorization
def insertion(n, node):
    left, right = divideBet(n)
    
    if left == 1: return
    
    node.left, node.right = Node(left), Node(right)
    
    insertion(left, node.left)
    insertion(right, node.right)

# inoder traversal to check the tree
def inorder(node):
    if (not node):
        return
    
    inorder(node.left)
    print(node.val, end=" ")
    inorder(node.right)
    
    
# serialize tree in a list and return that list
def serialize(node, string=[], marker=-1):
    # traversal of tree 
    # if not node found then return to backtrack
    if (not node):
        string.append(marker)
        return
    
    # if node found
    # push the value of node to string 
    string.append(node.val)
    serialize(node.left) # go the same for left node
    serialize(node.right) # go the same for right node
    
    # when tree is completly traverse
    # then return string
    return string


# deserialize string back to tree
def deserialize(string):
    root = r = None
    for s in string:
        if s == -1:
            if r == root.left:
                r = root.right
                continue
            if r == root.right:
                r = root
                continue
        r = Node(s)
        r = root.left    
    
n = 8
node = Node(n)
insertion(n, node)
s = serialize(node)
# print(s)
node1 = None
deserialize(s, node1, 0) 
inorder(node1)