import jsonpath
import json


obj = json.load(open('store.json','r',encoding='utf-8'))

# 书店所有书的作者
author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
print(author_list)

# 所有的作者
author_list = jsonpath.jsonpath(obj, '$..author')
print(author_list)

# store的所有元素。所有的bookst和bicycle
tag_list = jsonpath.jsonpath(obj, '$.store.*')
print(tag_list)

# store下面的所有东西的price
price_list = jsonpath.jsonpath(obj, '$.store..price')
print(price_list)

# 查询最后一本书
book = jsonpath.jsonpath(obj, '$..book[(@.length-1])')
print(book)

# 查询第三本书
book = jsonpath.jsonpath(obj, '$..book[3]')
print(book)

# 查询前两本书
book = jsonpath.jsonpath(obj, '$..book[:2]')
print(book)

# 过滤出所有含ISBN的书
book = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
print(book)

# 查询高于10元的书
book = jsonpath.jsonpath(obj, '$..book[?(@.price>10)]')