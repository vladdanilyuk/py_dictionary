#импорт библиотеки
import json

#загрузка json данных в виде словаря
data = json.load(open("dictionary.json"))

#фун-я для определения слова
def retrive_definition(word):
    return data[word]

#пользовательский ввод
word_user = input("Enter a word: ") 

#возврат определения слова, используя фун-ю и вывод результата
print(retrive_definition(word_user))
