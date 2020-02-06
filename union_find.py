class union_find():
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Union-find size needs to be a positive integer")
        # Number of elements stored in union find.
        self.size = size
        # Initially number of components is equal to size since each element's root is itself.
        self.components = size
        # Stores the parent, and if ids[i] == i, i is a root node. Initially every element is a root.
        self.ids = [i for i in range(size)]
        # Stores the size of each component. Initially all components are size 1.
        self.sizes = [1 for i in range(size)]

    def __len__(self):
        return self.size
    
    def __repr__(self):
        return str(self.ids)

    # Returns the root of element p (where root identifies the component).
    def find_iter(self, p):
        if p < 0 or p > self.size - 1:
            return None
        root = p
        while (self.ids[root] != root):
            root = self.ids[root]
        #Path compression
        while (p != self.ids[p]):
            self.ids[p], p = root, self.ids[p]
        return root

    # Returns the root of element p (where root identifies the component).
    def find(self, p):
        if self.ids[p] == p:
            return p
        else:
            self.ids[p] = self.find(self.ids[p])
        return self.ids[p]

    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)

        # Already in the same component
        if rootp == rootq:
            return rootq

        # Union the smaller component into the larger component
        if self.sizes[rootp] > self.sizes[rootq]:
            self.sizes[rootp] += self.sizes[rootq]
            self.sizes[rootq] = 0 
            self.ids[rootq] = rootp
            return rootp
        else:
            self.sizes[rootq] += self.sizes[rootp]
            self.sizes[rootp] = 0
            self.ids[rootp] = rootq
            return rootq

        # Due to union, there is one less component
        self.components -= 1

    # Whether element p and element q are in the same component
    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def component_size(self, p):
        return self.sizes[self.find(p)]
    
def test():
    x = union_find(10)
    print(x)
    print(len(x))
    print(x.find(9))
    print(x.union(8,9))
    print(x.connected(8,9))
    print(x.component_size(8))
    print(x.union(7,8))
    print(x.find(7))
    print(x.component_size(8))
    print(x.union(1,7))
    print(x)
        
test()
