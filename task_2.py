# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

text = """
Слова — это средство, с помощью которого мы наиболее четко и 
материально воплощаем свои внутренние желания и переживания. 
И хотя в любой точке мира у людей есть свой собственный язык, диалект и слова, 
которые для нас незнакомы, значение, которое мы вкладываем в них, одинаково, 
независимо от способа их выражения. И это во многом предполагает сходство наших разговоров. 
В этой статье познакомимся с самые популярными словами.
Сегодня Мы будем дистанцироваться от того, что нам нужно для любого типа речи, 
короткие слова или предлоги, такие как «ниже», «выше», «до», «и», «но», 
потому что рейтинги будут выглядеть совсем иначе.
"""

word_count = {}
text = text.lower()

punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for i in punctuation:
    text = text.replace(i, ' ')

words = text.split()
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print(sorted_words[:10])