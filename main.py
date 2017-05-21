#!/usr/bin/env python2

# To visualize how does it work, look on this webpage
# https://www.cs.usfca.edu/~galles/visualization/AVLtree.html

from AVL2 import insert_template_preorder
from AVL2 import delete_template_preorder
from AVL2 import message_received_from_user_is_proper
from AVL2 import AVLTree2
from AVL2 import newKey

def insert_testCase1_onRightSide_preorder(printTree):  # rotate right -> rotate left, because + -> -
    return insert_template_preorder([3, 1, 7, 4, 10, 5], [4, 3, 1, 7, 5, 10], printTree)


def insert_testCase2_onRightSide_preorder(printTree):  # rotate left, because + -> +
    return insert_template_preorder([3, 1, 7, 4, 10, 11], [7, 3, 1, 4, 10, 11], printTree)


def insert_testCase1_onLeftSide_preorder(printTree):  # rotate left -> rotate right, because - -> +
    return insert_template_preorder([8, 10, 4, 3, 5, 6], [5, 4, 3, 8, 6, 10], printTree)


def insert_testCase2_onLeftSide_preorder(printTree):  # rotate right because - -> -
    return insert_template_preorder([8, 10, 4, 3, 5, 2], [4, 3, 2, 8, 5, 10], printTree)

def delete_testCase1_upYes(printTree): # rotate left, because + -> +
    return delete_template_preorder([4, 3, 6, 5, 2, 8, 7], 3, [6, 4, 2, 5, 8, 7], printTree)

def delete_testCase2_upNo(printTree): # rotate left, because + -> +
    return delete_template_preorder([4, 3, 6, 5, 8], 3, [6, 4, 5, 8], printTree)

def delete_testCase3a(printTree): # rotate left, because + -> +
    return delete_template_preorder([6, 3, 11, 2, 12, 9, 8], 3, [9, 6, 2, 8, 11, 12], printTree)

if __name__ == "__main__":
    # To run test cases uncomment below
    ##################################################################
    #

    # To work in repl uncomment below
    ##################################################################

    a = AVLTree2()
    print("Please pass 'Exit' to end")
    while message_received_from_user_is_proper():
        a.dispatchByCommand()

##################################################################

    # inlist = [7, 5, 2, 6, 3, 4, 1, 8, 9, 0]
    # for i in inlist:
    #     a.insert(i)
    # a.display()
    # #
    # # print "----- Deleting -------"
    # a.delete(3)
    # # a.delete(4)
    # # # a.delete(5)
    # a.display()
    #
    # print
    # print "Input            :", inlist
    # print "deleting ...       ", 3
    # print "deleting ...       ", 4
    # print "Inorder traversal:", a.inorder_traverse()