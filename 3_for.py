"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
from itertools import product
from operator import itemgetter


phonesales = [
  {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
  {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
  {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]

#print (type(phonesales[0]))

def amount_phones_sold():
  amount_phone_list = []
  for product in phonesales:
    amount_phone_list.extend(product['items_sold'])
    avg_phone_sold = sum (items_sold)/len(items_sold)
  return (round(avg_phone_sold,2))



def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    for i in range(len(phonesales)):
      phone = phonesales[i]['product']
      avg_phone_sold = sum (phonesales[i]['items_sold'])/(len(phonesales[i]['items_sold']))
      total_phone_sold = sum (phonesales[i]['items_sold'])
      print ('Средняя продажа {phone} телефонов: ' + str(round(avg_phone_sold,2)))
      print ('Всего продано {phone} телефонов: ' + str(round(total_phone_sold)))
    print ('Средняя продажа телефонов: ' + str(avg_phone_sold(phonesales)))
    
if __name__ == "__main__":
    main()
