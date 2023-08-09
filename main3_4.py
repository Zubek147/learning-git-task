#zadanie 1

print('Zadanie 1')
print('')
name_dictionary = {}
name_list = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
for name in name_list:
  print(name, len(name_list))
name_dictionary = dict.fromkeys(name_list, len(name_list))
print(name_dictionary)
print('')
