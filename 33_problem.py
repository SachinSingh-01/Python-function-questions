'''Write a function apply_discount(price, discount=10) that:
Calculates final price after discount
Discount is in percentage
Returns the final price'''
def apply_discount(price, discount=10):
    discount_amount = price * discount / 100
    final_price = price - discount_amount
    return final_price
result=apply_discount(1030)
print(result)
