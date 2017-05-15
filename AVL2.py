outputdebug = True
newKey = ''


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


def insert_template_preorder(in_sequence, expected_preorder, print_tree):
    print '\nInserting: ' + str(in_sequence)

    a = AVLTree2()
    for i in in_sequence:
        a.insert(i)

    if print_tree:
        a.display()

    return a.preorder_traverse() == expected_preorder


