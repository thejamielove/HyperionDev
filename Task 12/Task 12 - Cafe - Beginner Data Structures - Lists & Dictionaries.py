print("Hello & Welcome to your Cafe Inventory Management Program!\n")

# list of menu items in cafe
menu_list = ["croissant", "coffee", "quiche", "sandwich"]

# dictionaries defining the stock purchase price & menu price of items in cafe
stock_dict = {'croissant': 5,
              'coffee': 10,
              'quiche': 15,
              'sandwich': 20}

price_dict = {'croissant': 1.5,
              'coffee': 8,
              'quiche': 10,
              'sandwich': 15}

# total_stock_value variable to store total cafe stock value
total_stock_value = 0

# for loop used to calculate the total stock value in the cafe by indexing menu items with stock & menu prices
for item in menu_list:
    item_value = stock_dict[item] * price_dict[item]
    total_stock_value += item_value

# for loop is used to iterate over dictionary key (menu item) & value
print("Current Stock Purchase Price of items:")
for item, value in stock_dict.items():
    print(f"{item} : £{value:,.2f}") # prints out, on separate lines, cafe items & stock purchase price

print("\nCurrent Menu Price of items:")
for item, value in price_dict.items():
    print(f"{item} : £{value:,.2f}") # prints out, on separate lines, cafe items & menu price

print(f"\nTotal Stock value of Cafe = £{total_stock_value:,.2f}") # print out of total stock value of cafe