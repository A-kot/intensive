def func(node):
    if node:  # если у вершины есть потомки -> рекурсивно вывести левую ветвь, вершину, правую
        func(node.left)
        print(node.val)
        func(node.right)

