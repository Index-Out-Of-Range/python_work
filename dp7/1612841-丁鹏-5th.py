class BinaryTree:
    def __init__(self, left_child, right_child):
        self.left_child = left_child
        self.right_child = right_child
        self.count = -1

    def __getitem__(self, item):
        return self.right_child[item]

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= len(self.left_child) - 1:
            raise StopIteration
        else:
            self.count += 1
            return self.left_child[self.count]


def print_child(tree):
    for i in range(len(tree.left_child)):
        yield tree.left_child[i]
    for i in range(len(tree.right_child)):
        yield tree.right_child[i]


tree = BinaryTree(['a', 'b', 'c'], ['1', '2', '3'])

print('The left child of the tree is:')
for i in tree:
    print(i)

print('The right child of the tree is:')
for i in range(len(tree.right_child)):
    print(tree[i])

print('The whole tree is:')
for i in print_child(tree):
    print(i)
