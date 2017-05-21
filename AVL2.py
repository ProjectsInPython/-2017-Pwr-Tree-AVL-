outputdebug = True
newKey = ''
commandReceived = ''
breakLoop = False
continueLoop = True


def debug(msg):
    if outputdebug:
        print msg


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class AVLTree2:
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
            self.node.left = AVLTree2()
            self.node.right = AVLTree2()
            debug("Inserted key [" + str(key) + "]")

        elif key < tree.key:
            tree.left.insert(key)

        elif key > tree.key:
            tree.right.insert(key)

        else:
            debug("Key [" + str(key) + "] already in tree")

        self.rebalance()

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

    def rebalance(self):
        self.update_heights(recurse=False)
        self.update_balances(recurse=False)

        while self.balance < -1 or self.balance > 1:
            if self.balance < -1:
                if self.node.left.balance > 0:
                    self.node.left.lrotate()
                    self.update_heights(recurse=True)
                    self.update_balances(recurse=True)
                self.rrotate()
                self.update_heights(recurse=True)
                self.update_balances(recurse=True)

            if self.balance > 1:
                if self.node.right.balance < 0:
                    self.node.right.rrotate()
                    self.update_heights(recurse=True)
                    self.update_balances(recurse=True)
                self.lrotate()
                self.update_heights(recurse=True)
                self.update_balances(recurse=True)

    def rrotate(self):
        # Rotate right pivoting on self
        debug('Rotating ' + str(self.node.key) + ' right')
        X = self.node
        Y = X.left.node
        T = Y.right.node

        self.node = Y
        Y.right.node = X
        X.left.node = T

    def lrotate(self):
        # Rotate left pivoting on self
        debug('Rotating ' + str(self.node.key) + ' left')
        X = self.node
        Y = X.right.node
        T = Y.left.node

        self.node = Y
        Y.left.node = X
        X.right.node = T

    def update_heights(self, recurse):
        if self.node:
            if recurse:
                if self.node.left:
                    self.node.left.update_heights(True)
                if self.node.right:
                    self.node.right.update_heights(True)

            self.height = max(self.node.left.height, self.node.right.height) + 1

        else:
            self.height = -1

    def update_balances(self, recurse):
        if self.node:
            if recurse:
                if self.node.left:
                    self.node.left.update_balances(True)
                if self.node.right:
                    self.node.right.update_balances(True)

            self.balance = self.node.right.height - self.node.left.height
        else:
            self.balance = 0

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
        self.update_heights(True)
        self.update_balances(True)
        if self.node:
            print '-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(
                self.balance) + "]", 'L' if self.is_leaf() else ''
            if self.node.left:
                self.node.left.display(level + 1, '<')
            if self.node.right:
                self.node.right.display(level + 1, '>')

    def dispatchByCommand(self):
        if 'Insert' in commandReceived:
            self.display()
            self.insert(int(newKey))
        elif 'Delete' in commandReceived:
            self.display()
            self.delete(newKey)
        else:
            print('Unknown command')

        self.display()

def message_received_from_user_is_proper():
    global newKey
    global commandReceived
    global breakLoop
    global continueLoop

    pureInput = raw_input("Key to add: ")
    tokenizedInput = pureInput.split(' ')

    commandReceived = tokenizedInput[0]
    if 'Exit' in commandReceived:
        return breakLoop
    else:
        newKey = tokenizedInput[1]

    return continueLoop

def insert_template_preorder(in_sequence, expected_preorder, print_tree):
    print '\nInserting: ' + str(in_sequence)

    a = AVLTree2()
    for i in in_sequence:
        a.insert(i)

    if print_tree:
        a.display()

    return a.preorder_traverse() == expected_preorder


def delete_template_preorder(in_sequence, keyToDel,  expected_preorder, print_tree):
    print '\nDeleting: ' + str(in_sequence)

    a = AVLTree2()
    for i in in_sequence:
        a.insert(i)

    a.display()

    a.delete(keyToDel)

    if print_tree:
        a.display()

    return a.preorder_traverse() == expected_preorder
