

book = 'way of kings'

food = "beans"
# for char in book:
#     list = char
#     print(list)


#list comprehension
this_list = [char[0:5:] for char in book]
print(this_list)

bean = [fead[2::] for fead in food]

print(bean)




even_numbers = [i for i in range (1,12) if i %2 == 0]
odd_numbers = [i for i in range (1,12) if i %2 != 0]

mult_i = [(i,i*i) for i in range (1,11) ]

print(odd_numbers)
print(even_numbers)
print(mult_i)



groceries = [['milk', 'eggs', 'bread', 'butter'],
            ['carrots', 'celery', 'lettuce'],['chicken', 'beef', 'pork']]


single = [single for single in groceries]
item = [item for single in groceries for item in single]


numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

positive =  [num for num in numbers if num % 2 == 0 and num > 0 ]

print(positive)

# print(single)
# print(item)


add_two = lambda x: x + 2

# print(add_two(23))

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = [ite for flat in list_of_lists for ite in flat]

print(flat_list)


tuples_to_list = [(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]

new_lists = [flat_list for new_list in tuples_to_list for flat_list in new_list ]


print(new_lists)
tuo = (1,2,3,4,5)

tuoli = list(tuo)



countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]


dict_countries = {'country': [country.upper() for country,city in countries], 'city': [city for country,city in countries]}
print(dict_countries)