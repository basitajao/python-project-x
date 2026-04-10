# new_set = set()
# set_with_things = {'pepperoni','sugar','chicken','noodles'}

# print(len(set_with_things))

# print('is it there :', 'rice' in set_with_things,'pepperoni' in set_with_things)

# set_with_things.add('rice')
# vegetables = {'carrot','cabbage','lettuce','spinach'}
# vegetables.update(['onion','pepper','cucumber'])
# set_with_things.update(vegetables)

# set_with_things.remove('tea') if 'tea' in set_with_things else print('tea not found')

# print(set_with_things, len(set_with_things), vegetables) 

# set_with_things.remove('rice') if 'rice' in set_with_things else print('rice not found')
# set_with_things.remove('chicken')
# set_with_things.discard('noodles')
# set_with_things.pop()
# print('\n',set_with_things)
# set_with_things.clear()
# print('after clear:', set_with_things)
# del set_with_things
# print('after delete:', set_with_things)



# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('twitter')

it_companies.update(['yahoo','tumblr','reddit','opay'])

it_companies.remove('yahoo')

print(it_companies)

C = A.union(B)

A.intersection(B)
A.issubset(B)
A.isdisjoint(B)

A.update(B)
B.update(A)
A.symmetric_difference(B)

del A
del B

set_age = set(age)

print('comparing length', len(age) == len(set_age))

find_in = 'I am a teacher and I love to inspire and teach people'
unique_words = set(find_in.split())
print(unique_words)