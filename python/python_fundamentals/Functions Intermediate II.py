# x = [ [5,2,3], [10,8,9] ]
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]
# ********************************************************
# x[1][0]=15
# print(x)
#*****************************
# students[0]['last_name']="Bryant"
# print(students)
#********************************)
# sports_directory['soccer'][0]='Andres'
# print(sports_directory)
#*********************************
# z[0]['y']=30
# print(z)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def iterateDictionary(arr):
#     for i in range(0,len(arr)):
#         print("first_name - ", arr[i]['first_name'], ",", "last_name - ", arr[i]['last_name'])
#     return arr
# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# arr=students
# iterateDictionary(arr)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def iterateDictionary2(key, arr):
#     for i in range(0,len(arr)):
#         print(arr[i][key])
#     return arr
# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# arr=students
# iterateDictionary2('last_name', arr)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def printInfo(dict):
#     print(int(len(dict['locations'])), "locations")
#     for i in range(0,int(len(dict['locations']))):
#         print(dict['locations'][i])
#     print(int(len(dict['instructors'])), "instructors")
#     for i in range(0,int(len(dict['locations']))):
#         print(dict['instructors'][i])
#     return dict
# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# printInfo(dojo)