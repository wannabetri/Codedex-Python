# Write code below 💖

stock_prices = [6.15, 5.81, 5.70, 5.65, 5.33, 5.62, 5.19, 6.13, 7.20, 7.34, 7.95, 7.53, 7.39, 7.59, 7.27]

def price_at(x):
  return stock_prices[x-1]

def max_price(a, b):
  top = 0
  for x in range(a, b + 1):
    top = max(top, price_at(x))
  return top

def min_price(a, b):
  low = price_at(a)
  for x in range(a, b + 1):
    low = min(low, price_at(x))
  return low


print(max_price(1, 10))
print(min_price(1, 10))
print(price_at(5))
