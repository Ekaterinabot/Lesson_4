# Пример Импорта Сравнений
# Задача нечеткого сравнения строк. 
# Будем считать, что строки тем "похожи",
# чем больше в них совпадающих триграмм:
#                  компьютер
#                  компьютеризация

>>> def compare (S1, S2):
    ngrams = [
        S1[i:i+3] for i in range(len(S1))
        ]
    count = 0
    for ngram in ngrams:
        count += S2.count(ngram)
    return count/max(len(S1), len(S2))

>>> compare('компьютер', 'компьютеризация')
0.6
>>> compare('стол', 'стул')
0.25
>>> compare('стол', 'столик')
0.6666666666666666
>>> 
