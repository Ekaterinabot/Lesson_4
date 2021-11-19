# Видео 6. Задание №1. Описать классами ваши данные, кот. ранее придумыали.
# Описываем через готовый модуль class Person через функцию init.
#data = {
#     ('Иванов', 'Иван', 'Иванович'): {'род.': 1990, 'пол': 'мужской', 'рост': 170, 'вес': 80, 'профессия': 'инженер'},
#     ('Смирнов', 'Петр', 'Аркадьевич'): {'род.': 1990, 'пол': 'мужской', 'рост': 165, 'вес': 95, 'профессия': 'менеджер'}
#     }
     
Person = {
    ("Иван", 30, "инженер"),
    ("Петр", 30, "менеджер")
}     
     
from pprint import pprint
class Person:
    def __init__(self, name, age, profession):
        self.name, self.age, self.profession = name, age, profession
        self.key = (name, profession)
    def __repr__(self):
        return "Person('%s', %s, '%s')" % (self.name, self.age, self.profession)
        
ivan = Person("Иван", 30, "инженер")
petr = Person("Петр", 30, "менеджер")
people = {
    ivan.key: ivan,
    petr.key: petr
}
pprint(people)
pprint(people[ivan.key])
