from products import Product

class RBNode:

    def __init__(self, val):
        self.red = False

        self.parent = None

        self.key = val.name

        self.left = None

        self.right = None
        self.values = [val]

class RBTree:

    def __init__(self):

        self.nil = RBNode(Product("mne nuzhno chto-to chego tochno net","weq",1,1))

        self.nil.red = False

        self.nil.left = None

        self.nil.right = None

        self.root = self.nil

    def insert(self, val):

        # Ordinary Binary Search Insertion

        new_node = RBNode(val)

        new_node.parent = None

        new_node.left = self.nil

        new_node.right = self.nil

        new_node.red = True  # new node must be red

        parent = None

        current = self.root

        while current != self.nil:

            parent = current

            if new_node.key < current.key:

                current = current.left

            elif new_node.key > current.key:

                current = current.right

            else:
                current.values.append(val)
                return

        # Set the parent and insert the new node

        new_node.parent = parent

        if parent is None:

            self.root = new_node

        elif new_node.key < parent.key:

            parent.left = new_node

        else:

            parent.right = new_node

        # Fix the tree

        self.fix_insert(new_node)

    def fix_insert(self, new_node):

        while new_node != self.root and new_node.parent.red:

            if new_node.parent == new_node.parent.parent.right:

                u = new_node.parent.parent.left  # uncle

                if u.red:

                    u.red = False

                    new_node.parent.red = False

                    new_node.parent.parent.red = True

                    new_node = new_node.parent.parent

                else:

                    if new_node == new_node.parent.left:
                        new_node = new_node.parent

                        self.rotate_right(new_node)

                    new_node.parent.red = False

                    new_node.parent.parent.red = True

                    self.rotate_left(new_node.parent.parent)

            else:

                u = new_node.parent.parent.right  # uncle

                if u.red:

                    u.red = False

                    new_node.parent.red = False

                    new_node.parent.parent.red = True

                    new_node = new_node.parent.parent

                else:

                    if new_node == new_node.parent.right:
                        new_node = new_node.parent

                        self.rotate_left(new_node)

                    new_node.parent.red = False

                    new_node.parent.parent.red = True

                    self.rotate_right(new_node.parent.parent)

        self.root.red = False

    def exists(self, productname):

        curr = self.root

        while curr != self.nil and productname != curr.key:

            if productname < curr.key:

                curr = curr.left

            else:

                curr = curr.right

        if curr.key == productname:
            return curr.values
        else:
            return False

    # rotate left at node x

    def rotate_left(self, x):

        y = x.right

        x.right = y.left

        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent

        if x.parent == None:

            self.root = y

        elif x == x.parent.left:

            x.parent.left = y

        else:

            x.parent.right = y

        y.left = x

        x.parent = y

    # rotate right at node x

    def rotate_right(self, x):

        y = x.left

        x.left = y.right

        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent

        if x.parent == None:

            self.root = y

        elif x == x.parent.right:

            x.parent.right = y

        else:

            x.parent.left = y

        y.right = x

        x.parent = y



