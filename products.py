products = [ ]
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':  #q為quit停止的意思
        break
    price = input('請輸入商品價格: ')
    products.append([name, price])
print(products)
print('....................')

            
for p in products:
	print(p[0], '價格是', p[1])
