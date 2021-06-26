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
    # pop first elem from string
    # then initialize root to popped_elem
    val = string.pop(0)
    root = Node(val)
    
    # check if any elem in string
    if len(string):
        # check first elem should not be marker
        if string[0] != -1:
            root.left = deserialize(string) # initialize left root
        else:
            # if first elem is marker then pop it
            string.pop(0) 
            # again, check first elem should not be marker
            if string[0] != -1:
                root.right = deserialize(string) # initialize right root
            else:
                # if marker then pop and return root to backtrack
                string.pop(0)
                return root
    
    # again, check if any elem in left in string
    if len(string):
        # initialized right of backtracked root
        root.right = deserialize(string) 
            
    return root

if __name__ == '__main__':
    n = int(input())
    node = Node(n)
    insertion(n, node) # based on prime factorization
    # s = serialize(node)
    # node1 = deserialize(s) 
    # inorder(node1)
    assert deserialize(serialize(node)).left.left.val == node.left.left.val
    print()
    print('Worked!')