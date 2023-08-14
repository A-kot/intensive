class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def func(queue, visited):
    if len(queue) > 0:
        if queue[0] is not None:
            visited.add(queue[0].value)
            print(queue[0].value)
            queue.append(queue[0].left)
            queue.append(queue[0].right)
            queue = queue[1:]
            func(queue, visited)


node = Node(8)
node.left = Node(5)
node.right = Node(10)
node.left.left = Node(3)
node.left.right = Node(6)
node.right.left = Node(9)
node.right.right = Node(11)

visited = set()
queue = [node]
print(func(queue, visited))
