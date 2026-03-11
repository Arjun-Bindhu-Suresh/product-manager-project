class ProductManager:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def display_product(self):
        return f"Product: {self.product_name}, Price: ${self.price}"