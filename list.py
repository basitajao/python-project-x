m = [2,3,4,12,5]
n = [239, 45,56,78,23]
o = [0, -24, 55,44,32]

m.extend(n)
n = m

p = m + n + o

print(f"m: {m}, n: {n} , p: {p}")

o.pop()

n.append(34)
n.insert(2,450)
# n.append(34)
del p[0:4]

# print(f"m: {m}, n: {n} , p: {p}")
gut = []


food = ['egusi', 'fufu', 'pounded yam', 'rice', 'beans', 'plantain', 'yam', 'spaghetti']
food.remove('yam')

favourite_food = food[3::3]

exist = 'yam' in food

fake = ['apple', 45, 5.67, True, 'banana']



# fake.clear()
# print(f"favourite food: {favourite_food} \n all food: {food}")
# print(f"Does yam exist in food list? {exist}")
# print(f"fake: {fake}")
# fake.reverse()
# print(fake)
# print(len(food))
# print(n)


