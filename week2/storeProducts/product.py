class Product:
    def __init__ (self, name, category, price):
        self.name=name
        self.category=category
        self.price=price

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price *= (1 + percent_change)
        else:
            self.price *= (1 - percent_change)
        self.print_info()
        return self

    def print_info(self):
        print(f"Name: {self.name.title()}, Category: {self.category.title()}, Price: ${'{:.2f}'.format(self.price)}")
        return self
