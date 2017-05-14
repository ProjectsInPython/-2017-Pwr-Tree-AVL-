from AVL import AVLTree
from AVL import insert_template_preorder

def insert_testCase1_onRightSide_preorder(printTree):  # rotate right -> rotate left, because + -> -
    return insert_template_preorder([3, 1, 7, 4, 10, 5], [4, 3, 1, 7, 5, 10], printTree)


def insert_testCase2_onRightSide_preorder(printTree):  # rotate left, because + -> +
    return insert_template_preorder([3, 1, 7, 4, 10, 11], [7, 3, 1, 4, 10, 11], printTree)


def insert_testCase1_onLeftSide_preorder(printTree):  # rotate left -> rotate right, because - -> +
    return insert_template_preorder([8, 10, 4, 3, 5, 6], [5, 4, 3, 8, 6, 10], printTree)


def insert_testCase2_onLeftSide_preorder(printTree):  # rotate right because - -> -
    return insert_template_preorder([8, 10, 4, 3, 5, 2], [4, 3, 2, 8, 5, 10], printTree)

if __name__ == "__main__":
    a = AVLTree()

# To run test cases uncomment below
##################################################################

    printTree = True
    print insert_testCase1_onRightSide_preorder(printTree)
    print insert_testCase2_onRightSide_preorder(printTree)

    print insert_testCase1_onLeftSide_preorder(printTree)
    print insert_testCase2_onLeftSide_preorder(printTree)

# To work in repl uncomment below
##################################################################

    # print("Please pass 'Exit' to end")
    # while receivedFromUser() != 'Exit':
    #     a.insert(int(newKey))
    #     a.display()

##################################################################

    # print "----- Deleting -------"
    # a.delete(3)
    # a.delete(4)
    # # a.delete(5)
    # a.display()
    #
    # print
    # print "Input            :", inlist
    # print "deleting ...       ", 3
    # print "deleting ...       ", 4
    # print "Inorder traversal:", a.inorder_traverse()