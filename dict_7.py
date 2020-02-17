#импорт библиотеки
import json
from difflib import get_close_matches

#загрузка json данных в виде словаря
data = json.load(open("dictionary.json"))

#фун-я для определения слова
def retrive_definition(word):
	
	#убираем чувствительность к регистру
	#cat и CaT - должны иметь тот же вывод
	#конвертация в lowercase, тк данные в формате json 
	word = word.lower()

	#проверка на несуществующее слово
	#1st elif: Чтобы программа возвращала значения слов с заглавной буквы (e.g. Delhi, Texas)
	#2nd elif: Чтобы программа возвращала значения аббревиатур (e.g. USA, NATO)
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	#3rd elif: To find a similar word
	#-- len > 0 because we can print only when the word has 1 or more close matches
	#-- len > 0 вывод, если слово имеет 1 или больше совпадений
	#-- в return, last [0] - первый элемнт из списка совпадений
	elif len(get_close_matches(word, data.keys())) > 0:
	    action = input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])
	    #-- If the answers is yes, retrive definition of suggested word
	    if (action == "y"):
	        return data[get_close_matches(word, data.keys())[0]]
	    elif (action == "n"):
	        return ("The word doesn't exist, yet.")
	    else:
	        return ("We don't understand your entry. Apologies.")
#пользовательский ввод
word_user = input("Enter a word: ")

#возврат определения слова, используя фун-ю и вывод результата
output = retrive_definition(word_user)

#если у слова болльше одного значения, выводит определения рекурс
if type(output) == list:
    for item in output:
        print("-",item)
#для слов с одним значение
else:
    print("-",output)