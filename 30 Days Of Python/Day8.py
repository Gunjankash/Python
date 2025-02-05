# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#         }
# }
# person['job_title'] = 'Instructor'
# person['skills'].append('HTML')
# print(person)

# 💻 Exercises: Day 8

# Create an empty dictionary called dog
dog={}
print(type(dog))

# Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name':'Doggy',
    'breed':'Lab',
    'legs':4,
    'age':2
}
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name':'Gunjan',
    'last_name':'Kashyao',
    'gender':'Female',
    'age':21,
    'country':'India',
    'city':'Ghy',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
}}

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list

skill = student['skills']
print(skill)
print(type(skill))

# Modify the skills values by adding one or two skills
student['skills'].append('C')
print(student['skills'])

# Get the dictionary keys as a list
keys_list = list(student.keys())
# Get the dictionary values as a list
print(keys_list)
# Change the dictionary to a list of tuples using items() method
tup = list(student.items())
print(tup)
# Delete one of the items in the dictionary
del student['city']
# Delete one of the dictionaries
del dog