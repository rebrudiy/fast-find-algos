class BSTNode:

    def __init__(self, val=None):

        self.left = None

        self.right = None

        self.key = val.name

        self.values = [val]

    def insert(self, val):

        if not self.key:
            self.key = val.name
            self.values.append(val)

            return

        if self.key == val.name:
            self.values.append(val)

        if val.name < self.key:

            if self.left:
                self.left.insert(val)

                return

            self.left = BSTNode(val)

            return

        if self.right:
            self.right.insert(val)

            return

        self.right = BSTNode(val)

    def exists(self, valname):

        if valname == self.key:
            return self.values

        if valname < self.key:
            if self.left == None:
                return False

            return self.left.exists(valname)

        if self.right == None:
            return False

        return self.right.exists(valname)
