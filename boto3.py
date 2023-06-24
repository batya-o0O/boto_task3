import pymorphy2

morph = pymorphy2.MorphAnalyzer()

def beliberda(words):
    needed_pos = ["ADVB", "ADJS", "NPRO", "VERB", "PREP"] # список нужных part of the speech наречие, прилагательное, местоимение, глагол и предлог
    for word in words:  # для каждого слова деляем проверку, если хоть одно слово проходит проверку ответ Тру
    # print(snowball.stem(word))
        if morph.parse(word)[0].tag.POS in needed_pos: #узнаем part of the speech word-а и если он входит в список то ответ Тру
            print("TRUE")
            return True
    print("FALSE")
    return False


inp = input("Your response:")  # input 
words = inp.split()  # разделяем стринг по словам
beliberda(words)  # вызываем функцию
