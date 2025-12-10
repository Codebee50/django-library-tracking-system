import random
rand_list = [random.randint(1, 20) for i in range(10)]

print("Random number list", rand_list)

list_comprehension_below_10 = [i for i in rand_list if i < 10]

print("List comprehension below ten", list_comprehension_below_10)

list_comprehension_below_10_filter = list(filter(lambda x: x < 10, rand_list))

print("List comprehension below ten filter", list_comprehension_below_10_filter)
