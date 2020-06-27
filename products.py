#讀取檔案
products = [ ]
with open('products.csv', 'r', encoding = 'utf-8') as f:
    for line in f:
        if'商品, 價格' in line:
    	    continue #繼續新一輪迴圈
        name, price = line.strip().split(',')
        products.append([name, price])
        
print(products)
print('....................')

#讓使用者輸入
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':  #q為quit停止的意思
        break
    price = input('請輸入商品價格: ')
    products.append([name, price])
print(products)
print('....................')

#印出所有購買紀錄 
for p in products:
	print(p[0], '價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('商品, 價格\n' )
    for p in products:
    	f.write(p[0] + ',' + p[1] + '\n') #\n為分行符號

