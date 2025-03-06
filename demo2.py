array1 = [i for i in range(10,16)]
print(array1)

name = "prakash"

array2 = [i for i in name]
print(array2)

dic = {
    "one": 1,
    'two': 2
}


for key, value in dic, dic.values() :
    print(key, value)

array3 = [(i, j) for i, j in (dic, dic.values())]
print(array3)