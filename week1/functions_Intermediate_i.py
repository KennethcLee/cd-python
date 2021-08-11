x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

for j in range(len(x)):
    for k in range(len(x[j])):
        if x[j][k] == 10:
            x[j][k] = 15

students[0]['last_name']='Bryant'
print(students)

sports_directory['soccer'][0]='Andres'
print(sports_directory)

z[0]['y']=30
print(z)

students = [
    {'first_name' : 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(x):
    for j in range(len(x)):
        print(f"first_name - {x[j]['first_name']}, last_name - {x[j]['last_name']}")
iterateDictionary(students)

def iterateDictionary(x):
    for j in x:
        print(f"first_name - {x['first_name']}, last_name - {x['last_name']}")
iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
"""
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonelcopy
"""

def iterateDictionary2(key_name, some_list):
    for j in range(len(some_list)):
        print(some_list[j][key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for j in some_dict:
        print(len(some_dict[j]), j.upper())
        for k in some_dict[j]:
            print(k)
printInfo(dojo)