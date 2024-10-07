class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_stock(self):
        stock =  self.price * self.quantity
        print( f"The total value of {self.name} in stock is: {stock} ksh")
prd1 = product('Banana', 10, 30)
prd1.total_stock()