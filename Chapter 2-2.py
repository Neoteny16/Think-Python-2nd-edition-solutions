# 1
r = 5
volume = 4/3 * 3.14 * r **3
print(volume)

# 2
book_price = 24.95    # currency - $
book_store_discount = 40    # in percents
shipping = 3    # for the first book
additional_book = 0.75 
discount = book_price * book_store_discount / 100
books_to_buy = 60
shipping_total = (books_to_buy - 1) * additional_book + 3
total_price = discount * books_to_buy + shipping_total
print(total_price)

# 3
