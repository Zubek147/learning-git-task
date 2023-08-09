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

#zadanie 3

print('Zadanie 3')
print('')
weekdays = ['pon','śro','pią','sob']
weekdays.insert(1,'wto')
weekdays.insert(3,'czw')
weekdays.append('nie')
print('Pełna lista dni tygodnia')
print(weekdays)
print('')


#zadanie 4
print('Zadanie 4')
print('')
a = '•włącz czajnik'
b = '•znajdź opakowanie herbaty'
c = '•zalej herbatę'
d = '•nalej wody do czajnika'
e = '•wyjmij kubek'
f = '•włóż herbatę do kubka'    
print('Sekwencja nieposortowana')
sequence = [a, b, c, d, e, f]
print(sequence)
print('')
del sequence[0:3]
sequence.insert(1,a)
sequence.insert(3,b)
sequence.append(c)
print('Sekwencja posortowana')
print(sequence)


###Specjalne pozdrowienia dla mentora z teamu Kodilla ;)