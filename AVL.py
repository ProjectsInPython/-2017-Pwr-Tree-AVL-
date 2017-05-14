outputdebug = True
newKey = ''

def debug(msg):
    if outputdebug:
        print msg


class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0

        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def is_leaf(self):
        return self.height == 0

    def insert(self, key):
        tree = self.node

        if not tree:
            self.node = Node(key)
            self.node.left = AVLTree()
            self.node.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")

        elif key < tree.key:
            self.node.left.insert(key)

        elif key > tree.key:
            self.node.right.insert(key)

        else:
            debug("Key [" + str(key) + "] already in tree.")

        self.rebalance()

    def rebalance(self):
        ''' 
        Rebalance a particular (sub)tree
        '''
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate()  # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:

                if self.node.right.balance > 0:
                    self.node.right.rrotate()  # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()

    def rrotate(self):
        # Rotate right pivoting on self
        debug('Rotating ' + str(self.node.key) + ' right')
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    def lrotate(self):
        # Rotate left pivoting on self
        debug('Rotating ' + str(self.node.key) + ' left')
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    def update_heights(self, recurse=True):
        if self.node:
            if recurse:
                if self.node.left:
                    self.node.left.update_heights()
                if self.node.right:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if self.node:
            if recurse:
                if self.node.left:
                    self.node.left.update_balances()
                if self.node.right:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def delete(self, key):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.node:
            if self.node.key == key:
                debug("Deleting ... " + str(key))
                if not self.node.left.node and not self.node.right.node:
                    self.node = None  # leaves can be killed at will
                # if only one subtree, take that
                elif not self.node.left.node:
                    self.node = self.node.right.node
                elif not self.node.right.node:
                    self.node = self.node.left.node

                # worst-case: both children present. Find logical successor
                else:
                    replacement = self.logical_successor(self.node)
                    if replacement:  # sanity check
                        debug("Found replacement for " + str(key) + " -> " + str(replacement.key))
                        self.node.key = replacement.key

                        # replaced. Now delete the key from right child
                        self.node.right.delete(replacement.key)

                self.rebalance()
                return
            elif key < self.node.key:
                self.node.left.delete(key)
            elif key > self.node.key:
                self.node.right.delete(key)

            self.rebalance()
        else:
            return

    def logical_predecessor(self, node):
        ''' 
        Find the biggest valued node in LEFT child
        '''
        node = node.left.node
        if node:
            while node.right:
                if not node.right.node:
                    return node
                else:
                    node = node.right.node

    def logical_successor(self, node):
        ''' 
        Find the smallese valued node in RIGHT child
        '''
        node = node.right.node
        if node:  # just a sanity check

            while node.left:
                debug("LS: traversing: " + str(node.key))
                if not node.left.node:
                    return node
                else:
                    node = node.left.node
        return node

    def check_balanced(self):
        if not self or not self.node:
            return True

        # We always need to make sure we are balanced
        self.update_heights()
        self.update_balances()
        return (self.balance > 2 or self.balance < -2) and self.node.left.check_balanced() and self.node.right.check_balanced()

    def inorder_traverse(self):
        if not self.node:
            return []

        inlist = []
        l = self.node.left.inorder_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist

    def preorder_traverse(self):
        if not self.node:
            return []

        inlist = [self.node.key]

        l = self.node.left.preorder_traverse()
        for i in l:
            inlist.append(i)

        l = self.node.right.preorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist

    def display(self, level=0, pref=''):
        '''
        Display the whole tree. Uses recursive def.
        TODO: create a better display using breadth-first search
        '''
        self.update_heights()  # Must update heights before balances
        self.update_balances()
        if self.node:
            print '-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(
                self.balance) + "]", 'L' if self.is_leaf() else ' '
            if self.node.left:
                self.node.left.display(level + 1, '<')
            if self.node.right:
                self.node.right.display(level + 1, '>')


def messageReceivedFromUser():
    global newKey
    newKey = raw_input("Key to add: ")
    return newKey


def insert_template_preorder(inSequence, expectedPreorder, printTree):
    print '\nInserting: ' + str(inSequence)

    a = AVLTree()
    for i in inSequence:
        a.insert(i)

    if printTree:
        a.display()

    return a.preorder_traverse() == expectedPreorder