class Store:
    def __init__(self, name):
        self.name=name
        self.products=[]

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

    def sell_product(self, id):
        self.products.pop(id)
        return self

    def inflation(self, percent_increase):
        for j in self.products:
            j.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for j in self.products:
            if j.category == category:
                j.update_price(percent_discount, False)
        return self