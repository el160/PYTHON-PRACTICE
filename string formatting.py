# f formatting of strings
price = 70
text = f"Price is ${price}"
print(text)

#using a modifier : to format the string .2f means 2 decimal places with fixed point number
price = 60
txt = f"price is ${price:.2f}"
print(txt)

#performing operations inside the place holder
price = 70
txt = f"price is ${price * 1.1:.2f}"
print(txt)

#performing math operations on variables
kiss = 40
hug = 30
union = f"union is ${kiss * hug:.2f} "
print(union)

#perform if else inside place holders
price = 70
pay = f"its very  {'costly'if price >70  else   'cheap'}"
print(pay)