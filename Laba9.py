######### 1 #########
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def meow(self):
        print('Мяу!')
 
    def eat(self):
        print('Вискас - лучший деликатес!')
 
    def sleep(self):
        print('Ам слип')
 
    def __str__(self):
        return f'Я кот {self.name}, мне {self.age}'
 
 
cat = Cat('Гарфилд', 3)
print(cat)
cat.eat()
cat.meow()
cat.sleep()

######### 2 #########
year = int(input('Введите год: '))

if year % 4 != 0:
    print('Год не високосный.')

elif year % 100 == 0:
    if year % 400 == 0:
        print('Год високосный.')
    else:
        print('Год не високосный.')
else:
    print('Год високосный.')
    
######### 3 #########
# Вариант 10
# какая-то дичь недоделаная 
class Word:
    def __init__(self, word, page, countpages):
        self.word = word
        self.page = page
        self.countpages = countpages
 
    def wordsnum(self):
        print(f'Слова встречающиеся {self.page} раз: {wordsnum}')
 
    def alphabet(self):
        alphabet = sorted(wordsnum)
        print(f'Слова в алфавитном порядке {alphabet}')
 
    def counter(self):
        print('Я хз как это сделать')
 
    def __str__(self):
        return f'Слово: {self.word}, страница: {self.page}, кол-во страниц: {self.countpages}'
 
 
word = Word(input("Введите слово: "), int(input("Введите страницу: ")), int(input("Введите кол-во страниц: ")))
wordsnum = ['Lab', 'Practice', 'I', 'love', 'pihon'] 
print(word)
word.wordsnum()
word.alphabet()
# word.counter()