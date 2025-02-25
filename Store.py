from Item import Item

class Store:

    def __init__(self):
        self.store = {}

    def addItem(self, item):
        category = item.category.upper() if item.category else None 
        if category not in self.store:
            self.store[category] = []
        self.store[category].append(item)

    def removeItem(self, item):
        category = item.category.upper() if item.category else None
        if not category or category not in self.store:
            return
        for sorteditem in self.store[category]:
            if sorteditem.upc == item.upc:
                self.store[category].remove(sorteditem)
                if not self.store[category]:
                    del self.store[category]
                return

    def removeCategory(self, category):
        if not category:
            return
        category = category.upper()
        if category in self.store:
            del self.store[category]

    def getItems(self, category):
        category = category.upper() 
        if category in self.store and self.store[category]:
            return '\n'.join([item.toString() for item in self.store[category]])
        else:
            return ''


    def doesItemExist(self, item):
        category = item.category.upper() if item.category else None
        for category in self.store:
            for sorteditem in self.store[category]:
                if sorteditem.upc == item.upc:
                    return True
    
        return False

    def countDollarItems(self):
        count = 0
        for category in self.store:
            count += sum(1 for item in self.store[category] if item.price <= 1.00)
        return count
