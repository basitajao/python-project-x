empty_tuple = ()
another_empty_tuple = tuple('4')
truck = ('nissan', 'toyota', 'ford', 'chevrolet')
len(truck)

nissan = truck[0]
chevrolet = truck[-1]
toyota_ford = truck[1:3]

numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

odd_numbers = numbers[::2]
even_numbers = numbers[1::2]
reversed_numbers = numbers[::-1]

print(f'{odd_numbers},\n{even_numbers},\n{reversed_numbers}')
fruit_basket = ('apple', 'banana', 'orange', 'mango', 'grape', 'kiwi', 'pineapple')

modifiable_fruit_basket = list(fruit_basket)

new_fruit = tuple(modifiable_fruit_basket)

print(f'{fruit_basket},\n {modifiable_fruit_basket}')

print('appple' in fruit_basket)

a_new_tuple = another_empty_tuple + truck
print(a_new_tuple)

del a_new_tuple