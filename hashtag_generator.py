"""
Генератор хэштегов

Команда маркетинга тратит слишком много времени на ввод хэштегов. Давайте поможем им
с помощью нашего собственного генератора хэштегов!

Вот в чем дело:

 Оно должно начинаться с хэштега (#).

 Во всех словах первая буква должна быть заглавной.

 Если конечный результат длиннее 140 символов, он должен возвращать
значение false.

 Если входные данные или результат являются пустой строкой, они должны
возвращать значение false.

Пример вывода функции:

" Hello there thanks for trying my Kata" => "#HelloThereThanksForTryingMyKata"

" Hello World " => "#HelloWorld"

"" => false
"""


def generate_hashtag(txt):
    # removing unnecessary spaces at the beginning and end in txt:
    txt = txt.strip()

    # check if txt is valid:
    if not txt:
        return False

    result = '#'
    # used to check whether the letter should be upper or not:
    is_start = True

    for c in txt:
        if c.isalpha():
            if is_start:
                result += c.upper()
                is_start = False
            else:
                result += c.lower()
        else:
            is_start = True
            if not c.isspace():
                result += c
    if len(result) <= 140:
        return result
    else:
        return False


print(generate_hashtag(" Hello there thanks for trying my Kata"))
print(generate_hashtag(" Hello there thanks for trying my 42 Kata"))
print(generate_hashtag(" Hello World "))
print(generate_hashtag(""))
print(generate_hashtag("42"))
