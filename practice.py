# def flick_switch(lst):
#     for i in list:
#         if type(i) == str or '':
#             print(True)
#         elif i == 'flick':
#             print(False)
#     return i

def flick_switch(lst):
    for i in lst:
        if type(i) == str or i == '':
            print(True)
        elif i == 'flick' :
            print(False)
    return list[i]

book = "The Great Gatsby"

flick_switch(book)