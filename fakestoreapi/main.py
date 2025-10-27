import requests

# запросили и считали данные по эндпойнту
response = requests.get('https://fakestoreapi.com/products')
# распаковали данные в формате json
products = response.json()
# print(products)
list_of_products = []
for item in products:
    product_selection = {}
    product_selection.update({
        'Название':item['title'],
        'Цена': item['price'],
    })
    list_of_products.append(product_selection)
    print(product_selection)

print('---' * 30)
