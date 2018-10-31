class Node:
    def __init__(self, key=""):
        self.key = key
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.height = 0
        self.poz = -1

    def __str__(self):
        return str(self.key) + "(" + str(self.height) + ")"

    def is_leaf(self):
        return self.height == 0

    def max_children_height(self):
        if self.left_child and self.right_child:
            return max(self.left_child.height, self.right_child.height)
        elif self.left_child and not self.right_child:
            return self.left_child.height
        elif not self.left_child and self.right_child:
            return self.right_child.height
        else:
            return -1

    def balance(self):
        return (self.left_child.height if self.left_child else -1) - (self.right_child.height if self.right_child else -1)


class AVLTree:
    def __init__(self, *args):
        self.rootNode = None
        self.elements_count = 0
        self.rebalance_count = 0
        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def height(self):
        if self.rootNode:
            return self.rootNode.height
        else:
            return 0

    def rebalance(self, node_to_rebalance):
        self.rebalance_count += 1
        a = node_to_rebalance
        f = a.parent  # allowed to be NULL
        if node_to_rebalance.balance() == -2:
            if node_to_rebalance.right_child.balance() <= 0:
                """Rebalance, case RRC """
                b = a.right_child
                c = b.right_child
                assert (a is not None and b is not None and c is not None)
                a.right_child = b.left_child
                if a.right_child:
                    a.right_child.parent = a
                b.left_child = a
                a.parent = b
                if f is None:
                    self.rootNode = b
                    self.rootNode.parent = None
                else:
                    if f.right_child == a:
                        f.right_child = b
                    else:
                        f.left_child = b
                    b.parent = f
                self.recompute_heights(a)
                self.recompute_heights(b.parent)
            else:
                """Rebalance, case RLC """
                b = a.right_child
                c = b.left_child
                assert (a is not None and b is not None and c is not None)
                b.left_child = c.right_child
                if b.left_child:
                    b.left_child.parent = b
                a.right_child = c.left_child
                if a.right_child:
                    a.right_child.parent = a
                c.right_child = b
                b.parent = c
                c.left_child = a
                a.parent = c
                if f is None:
                    self.rootNode = c
                    self.rootNode.parent = None
                else:
                    if f.right_child == a:
                        f.right_child = c
                    else:
                        f.left_child = c
                    c.parent = f
                self.recompute_heights(a)
                self.recompute_heights(b)
        else:
            assert (node_to_rebalance.balance() == +2)
            if node_to_rebalance.left_child.balance() >= 0:
                b = a.left_child
                c = b.left_child
                """Rebalance, case LLC """
                assert (a is not None and b is not None and c is not None)
                a.left_child = b.right_child
                if a.left_child:
                    a.left_child.parent = a
                b.right_child = a
                a.parent = b
                if f is None:
                    self.rootNode = b
                    self.rootNode.parent = None
                else:
                    if f.right_child == a:
                        f.right_child = b
                    else:
                        f.left_child = b
                    b.parent = f
                self.recompute_heights(a)
                self.recompute_heights(b.parent)
            else:
                b = a.left_child
                c = b.right_child
                """Rebalance, case LRC """
                assert (a is not None and b is not None and c is not None)
                a.left_child = c.right_child
                if a.left_child:
                    a.left_child.parent = a
                b.right_child = c.left_child
                if b.right_child:
                    b.right_child.parent = b
                c.left_child = b
                b.parent = c
                c.right_child = a
                a.parent = c
                if f is None:
                    self.rootNode = c
                    self.rootNode.parent = None
                else:
                    if f.right_child == a:
                        f.right_child = c
                    else:
                        f.left_child = c
                    c.parent = f
                self.recompute_heights(a)
                self.recompute_heights(b)

    @staticmethod
    def recompute_heights(start_from_node):
        changed = True
        node = start_from_node
        while node and changed:
            old_height = node.height
            node.height = (node.max_children_height() + 1 if (node.right_child or node.left_child) else 0)
            changed = node.height != old_height
            node = node.parent

    def add_as_child(self, parent_node, child_node):
        node_to_rebalance = None
        if child_node.key < parent_node.key:
            if not parent_node.left_child:
                parent_node.left_child = child_node
                child_node.parent = parent_node
                if parent_node.height == 0:
                    node = parent_node
                    while node:
                        node.height = node.max_children_height() + 1
                        if not node.balance() in [-1, 0, 1]:
                            node_to_rebalance = node
                            break  # we need the one that is furthest from the root
                        node = node.parent
            else:
                self.add_as_child(parent_node.left_child, child_node)
        else:
            if not parent_node.right_child:
                parent_node.right_child = child_node
                child_node.parent = parent_node
                if parent_node.height == 0:
                    node = parent_node
                    while node:
                        node.height = node.max_children_height() + 1
                        if not node.balance() in [-1, 0, 1]:
                            node_to_rebalance = node
                            break  # we need the one that is furthest from the root
                        node = node.parent
            else:
                self.add_as_child(parent_node.right_child, child_node)

        if node_to_rebalance:
            self.rebalance(node_to_rebalance)

    def insert(self, key):
        new_node = Node(key)
        if not self.rootNode:
            self.rootNode = new_node
        else:
            if not self.find(key):
                self.elements_count += 1
                self.add_as_child(self.rootNode, new_node)

    def inorder_non_recursive(self):
        node = self.rootNode
        retlst = []
        while node.left_child:
            node = node.left_child
        while node:
            retlst += [node.key]
            if node.right_child:
                node = node.right_child
                while node.left_child:
                    node = node.left_child
            else:
                while node.parent and (node == node.parent.right_child):
                    node = node.parent
                node = node.parent
        return retlst

    def inorder(self, node, retlst=None):
        if retlst is None:
            retlst = []
        if node.left_child:
            retlst = self.inorder(node.left_child, retlst)
        retlst += [node]
        if node.right_child:
            retlst = self.inorder(node.right_child, retlst)
        return retlst

    def find(self, key):
        return self.find_in_subtree(self.rootNode, key)

    def find_in_subtree(self, node, key):
        if node is None:
            return None  # key not found
        if key < node.key:
            return self.find_in_subtree(node.left_child, key)
        elif key > node.key:
            return self.find_in_subtree(node.right_child, key)
        else:  # key is equal to node key
            return node
