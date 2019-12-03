import json

person_dict = {'first': 'Christopher', 'last': 'Harrison'}
person_dict['City'] = 'Seattle'
language_list = ['CSharp', 'Python', 'JavaScript']
person_dict['Languages'] = language_list
person_json = json.dumps(person_dict)
person_json1 = json.loads(person_json)  # 需要使用json.loads()才能正确读取

print(person_dict)
print(person_dict['first'])
print(person_json1)
print(person_json1['first'])

# Create a subkey in json
staff_dict = {}
staff_dict['Program Manager'] = person_dict
staff_json = json.dumps(staff_dict)


print()
print(staff_json)
print(staff_dict['Program Manager'])
print(staff_dict['Program Manager']['first'])
