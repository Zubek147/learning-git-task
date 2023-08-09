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

#zadanie 2

print('Zadanie 2')
list_of_numbers = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
list_of_prime_numbers = []
print('')
print(f'Liczby z zadania \n{list_of_numbers}')
print('')
for number in list_of_numbers:
  if number == 2 or number == 3:
    list_of_prime_numbers.append(number)
  if number % 2 == 0 or number % 3 == 0 or number <= 1:
    pass
  else:
    list_of_prime_numbers.append(number)
print('Liczby pierwsze')
print(list_of_prime_numbers)
print('')
