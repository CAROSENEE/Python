class Bag:
    def __init__(self):
        self.items = []
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __iter__(self):
        return iter(self.items)

bag = Bag()
bag.items.extend(["Book", "Pen", "Laptop"])
print(len(bag))       # 3
print(bag[1])         # Pen
for item in bag:      # Iteration works
    print(item)
