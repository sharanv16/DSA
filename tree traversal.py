class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is not None:
                    self.left.insert(data)
                else:
                    self.left=Node(data)
            else:
                if self.right is not None:
                    self.right.insert(data)
                else:
                    self.right=Node(data)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data),
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.data),
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()


    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)


if __name__=="__main__":
    A=Node(10)
    A.insert(5)
    A.insert(11)
    print("\nINORDER")
    A.inorder()
    print("\nPRETORDER")
    A.preorder()
    print("\nPOSTORDER")
    A.postorder()