from functools import reduce

number = [2, 4, 6, 8, 10]

double_num= list(map(lambda x:x*2, number))

product_of_double_num = reduce(lambda x,y:x*y, double_num )

print(product_of_double_num)