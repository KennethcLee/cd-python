from product import Product
from store import Store

newstore=Store('ProduceRUs')
# print(newstore.name)
apple=Product('apple', 'fruit', 2)
orange=Product('orange', 'fruit', 3)
banana=Product('banana', 'fruit', 1)
lettuce=Product('lettuce', 'vegetable', 4)
chive=Product('chive', 'vegetable', 2)
newstore.add_product(apple).add_product(orange).add_product(banana).add_product(lettuce).add_product(chive)
apple.update_price(0.1, False)
newstore.sell_product(1)
newstore.inflation(0.5).list_product_ids('all')
newstore.set_clearance('vegetable', 0.2)

# print(product1.name, product1.category, product1.price)
# newstore.list_product_ids('all')
# newstore.list_product_ids(apple)
# print(newstore.products[0].name)
# print(newstore.products[1].name)


