# №1.Оформить Функциями Поиск в Списке:

# Используя Цикл for:
fruits = ['orange', 'apple', 'banana', 'tomat']
for vegetable in fruits:
	if vegetable == 'tomat':
		print ('vegetable')
#vegetable

# Используя оператор in:
fruits = ['orange', 'apple', 'banana', 'tomat']
if 'tomat' in fruits: print('vegetable')
#vegetable

# Используя оператор not in:
fruits = ['orange', 'apple', 'banana', 'tomat']
if 'cherry' not in fruits:
	print('berry')
#berry

# С помощью лямбда функции: 
fruits = ['orange', 'apple', 'banana', 'tomat']
retrieved_elements = list(filter(lambda x: 'tomat' in x, fruits))
print(retrieved_elements)

# №2. Оформить Функциями Поиск в Словаре:
data = {
     'Иванов И. И.':
         {'род.': 1990, 
         'пол': 'мужской', 
         'рост': 170, 
         'вес': 80, 
         'профессия': 'инженер'}
     }
# С помощью лямбда функции:
retrieved_elements = list(filter(lambda x: 'Иванов И. И.' in x, data))
print(retrieved_elements)

# №3. # Сделать нечеткое сравнение элементов.
# Задание 3. Оформить compare (сравнение) в Словаре:
>>> data = {
     ('Иванов', 'Иван', 'Иванович'): {'род.': 1990, 'пол': 'мужской', 'рост': 170, 'вес': 80, 'профессия': 'инженер'},
     ('Смирнов', 'Петр', 'Аркадьевич'): {'род.': 1990, 'пол': 'мужской', 'рост': 165, 'вес': 95, 'профессия': 'менеджер'}
     }
>>> def compare (S1, S2):
	ngrams = [
	  S1[i:i+3] for i in range(len(S1))
	]
	count = 0
	for ngram in ngrams:
	    count += S2.count(ngram)
	return count/max(len(S1), len(S2))

>>> compare('Иванов', 'Смирнов')
0.42857142857142855
>>> compare('Иван', 'Петр')
0.0
>>> compare('Иванович', 'Аркадьевич')
0.3
>>>
