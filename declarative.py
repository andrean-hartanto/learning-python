from random import randint

some_list = [randint(1, 101) for _ in range(10)]

# print isi some_list
print("some_list:", some_list)

# ambil semua bilangan genap, dan kalikan dengan bilangan itu sendiri
list_genap_and_double_it_value = \
    tuple(map(lambda item: (item, item*item),
               filter(lambda item: item % 2 == 0, sorted(some_list))))

print("list elemen genap dgn nilai double dari bilangan itu sendiri:")
for el, dbl in list_genap_ and_double_it_value:
    print(el, format(dbl, ","), sep=", ")
    