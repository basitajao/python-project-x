cat_dictionary = {'specimen1': 'small feline',
                  'specimen2': 'large feline',
                  'specimen3': 'striped feline',
                  'specimen4': 'fat feline',
                  'cat_colours': ['black','orange','tabby','calico','white','red']}

dog = dict()

dog['name'] = 'gerrard'
dog['color'] = 'brown'
dog['breed'] = 'labrador'
dog['legs'] = '4'
dog['age'] = 8

student_1 = {
    'name' : 'David',
    'surname' : 'Smith',
    'gender' : 'Male',
    'age' : 25,
    'marital status' : 'Single',
    'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country' : 'USA',
    'city' : 'New York', 
    'address' : '123, 5th Avenue'
}

student_2 = {
    'name' : 'Emma',
    'surname' : 'Johnson',
    'gender' : 'Female',
    'age' : 22,
    'marital status' : 'Married',
    'skills' : ['HTML', 'CSS', 'Java', 'C++', 'Python'],
    'country' : 'Canada',
    'city' : 'Toronto',
    'address' : '456, Queen Street'
}

len(cat_dictionary)
len(student_1)
len(student_2)

type(student_1['skills'][1])

student_1['skills'].append('SQL')
student_2['skills'].append('SQL')

cat_dictionary['cat_colours'].append('grey')

print(cat_dictionary.get('cat_colours'),'\n', student_1.get('skills'), '\n', student_2.get('skills'))

print(student_1.items())