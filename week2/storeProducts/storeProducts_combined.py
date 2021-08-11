class Product:
    def __init__ (self, name, category, price, store):
        self.name=name
        self.category=category
        self.price=price
        self.id=Store.next_id(store)

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price *= (1 + percent_change)
        else:
            self.price *= (1 - percent_change)
        self.print_info()
        return self

    def print_info(self):
        print(f"Name: {self.name.title()}, Category: {self.category.title()}, Price: ${'{:.2f}'.format(self.price)}, ID: {self.id}")
        return self

class Store:
    def __init__(self, name):
        self.name=name
        self.products=[1,2]

    def add_product(self, new_product):
        self.products.append(new_product)
        self.products[-1].print_info()
        return self

    def list_product_ids(self, product):
        if product == "all":
            for j in self.products:
                print(f"{j.name.title()} id is {self.products.index(j)}")
        else:
            print(f"{self.products[self.products.index(product)].name.title()} id is {self.products.index(product)}")
        return self

    def next_id(self):
        if self.products == []:
            return 0
        else:
            return (len(self.products))

    def sell_product(self, id):
        self.products.pop(id)
        return self

    def inflation(self, percent_increase):
        for j in self.products:
            print(j, apple)
            apple.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for j in self.products:
            if j.category == category:
                j.update_price(percent_discount, False)
        return self

newstore=Store('ProduceRUs')
apple=Product('apple', 'fruit', 2, newstore)

orange=Product('orange', 'fruit', 3, newstore)
banana=Product('banana', 'fruit', 1, newstore)
lettuce=Product('lettuce', 'vegetable', 4, newstore)
chive=Product('chive', 'vegetable', 2, newstore)
newstore.add_product(apple).add_product(orange).add_product(banana).add_product(lettuce).add_product(chive)
apple.update_price(0.1, False)
newstore.sell_product(1)
newstore.inflation(0.5)
# newstore.list_product_ids('all')
# newstore.set_clearance('vegetable', 0.2)
# print(len(newstore.products))
# print(Store.next_id(newstore))


# print(newstore.name)
# print(product1.name, product1.category, product1.price)
# newstore.list_product_ids('all')
# newstore.list_product_ids(apple)
# print(newstore.products[0].name)
# print(newstore.products[1].name)


