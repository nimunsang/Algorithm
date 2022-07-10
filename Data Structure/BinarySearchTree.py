class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.root = None

    def setRoot(self, value):
        self.root = Node(value)

    def find(self, value):
        return self.findNode(self.root, value)

    def findNode(self, currentNode, value):
        if currentNode is None:
            return False
        elif value == currentNode.value:
            return currentNode
        elif value < currentNode.value:
            return self.findNode(currentNode.left, value)
        else:
            return self.findNode(currentNode.right, value)

    def insert(self, value):
        # root가 아직 없다면, value를 root으로 설정한다.
        if self.root is None:
            self.setRoot(value)
        else:
            self.insertNode(self.root, value)

    def insertNode(self, currentNode, value):
        # value가 currentNode.value보다 작다면, currentNode의 왼쪽
        # value가 currentNode.value보다 크다면, currentNode의 오른쪽
        # 같은 경우는 없다.
        # 삽입의 시간 복잡도 : O(h)

        if value < currentNode.value:
            if currentNode.left:
                self.insertNode(currentNode.left, value)
            else:
                currentNode.left = Node(value)

        elif value > currentNode.value:
            if currentNode.right:
                self.insertNode(currentNode.right, value)
            else:
                currentNode.right = Node(value)

    def delete(self):
        # 리프 노드라면, 그냥 삭제하면 된다.
        if self.left is None and self.right is None:
            if self.root.value > self.value:
                self.root.left = None
            else:
                self.root.right = None
            self.root = None

        # 자식이 한쪽 방향에만 있는 경우
        if self.right is None:
            self.root.left = self.left
            self.left.root = self.root

            self.root = None
            self.left = None

        elif self.left is None:
            self.root.right = self.right
            self.right.root = self.root

            self.root = None
            self.right = None

        #자식이 양쪽 방향에 있는 경우
        successorNode = self.right.find_min_in_subtree()
        successorNode.value, self.value = self, successorNode.value
        successorNode.delete()


    def find_min_in_subtree(self):
        if self.left is None:
            return self

        return self.left.find_min_in_subtree()








