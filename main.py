import ollama

# === SETTINGS ===
MODEL = 'gemma3:12b'# 'ollama list' in OS terminal
LANGUAGE = 'ru'     # requires 'en'|'ru'|'ua'
TEMPERATURE = 1.0   # creative 0.0-2.0

isSmart = False
if int(MODEL.split(':')[1][0:-1]) > 4: isSmart = True

Elements = []
with open('Elements', 'a', encoding='utf-8') as f: f.close()
with open('Elements', 'r', encoding='utf-8') as f:
    f = f.read()
    if (f == '') and (LANGUAGE == 'en'): Elements = ['Water', 'Earth', 'Fire']
    elif (f == '') and (LANGUAGE == 'ru'): Elements = ['Вода', 'Земля', 'Огонь']
    elif (f == '') and (LANGUAGE == 'ua'): Elements = ['Вода', 'Земля', 'Вогонь']
    else: Elements = f.split(';% ')

if LANGUAGE == 'en': Prompt = ('You\'re an alchemist\'s game.\nThe user enters the text in the format:\n```txt\nthe_first_word + the_second_word =\n```\nYou need to answer with one word, which will indicate the mixing of these elements in the framework of the game of alchemist.\nWrite without formatting, just one word or phrase, don\'t write too much.' if isSmart else 'You\'re an alchemist\'s game.\nfirst word + second word = insert your answer\nWrite only the result.')
elif LANGUAGE == 'ru': Prompt = ('Ты - игра в алхимика.\nПользователь вводит текст в формате:\n```txt\nпервое_слово + второе_слово =\n```\nТебе нужно отвечать одним словом, которое будет обозначать смешивание этих элементов в рамках игры в алхимика.\nОтвечай без форматирования, только одно слово или словосочитание, не пиши лишнее.' if isSmart else 'Ты - игра в алхимика.\nпервое слово + второе слово = вставь свой ответ\nПиши только результат.')
elif LANGUAGE == 'ua': Prompt = ('Ти - гра в алхіміка.\nКористувач вводить текст в форматі:\n```txt\nперше_слово + друге_слово =\n```\nТобі потрібно відповісти одноим словом, яке буде позначати змішування ціх елементів в рамках гри в алхіміка.\nВідповідай без формати форматування, тільки одно слово або словосполучення, не пиши зайве.' if isSmart else 'Ти - гра в алхимика.\nперше слово + друге слово = встав свою відповідь\nПиши тільки результат.')
else: input(f'LANGUAGE error!\n{LANGUAGE=}, requires "en"|"ru"|"ua"'); quit()

while True:
    if LANGUAGE == 'en': print(f'\nYou have: {Elements}\nSelect two elements from this and they will connect:')
    elif LANGUAGE == 'ru': print(f'\nУ вас есть: {Elements}\nВыберите из этого два элемента и они соединятся:')
    elif LANGUAGE == 'ua': print(f'\nУ вас є: {Elements}\nВиберіть із цих двух елементів та вони з\'єднаються:')

    try:
        first = input('1> ').strip()
        if not (first in Elements):
            if LANGUAGE == 'en': print(f'{first} is not a list item!'); continue
            elif LANGUAGE == 'ru': print(f'{first} не является элементом списка!'); continue
            elif LANGUAGE == 'ua': print(f'{first} не є елементом списка!'); continue

        second = input('2> ').strip()
        if not (second in Elements):
            if LANGUAGE == 'en': print(f'{second} is not a list item!'); continue
            elif LANGUAGE == 'ru': print(f'{second} не является элементом списка!'); continue
            elif LANGUAGE == 'ua': print(f'{second} не є елементом списка!'); continue
    except KeyboardInterrupt:
        if LANGUAGE == 'en': print('Welcome!')
        elif LANGUAGE == 'ru': print('Добро пожаловать!')
        elif LANGUAGE == 'ua': print('Ласкаво просимо!')
        while True:
            _ = input('\n>> ').lower()
            if _ == 'end': break
            elif _ == 'exit': quit()
            elif _ == 'exec': exec(input('exec> '))
            elif _ == 'eval': print(eval(input('eval> ')))
            elif _ == 'help': print('end|exit|exec|eval|help')
        
    response = ollama.chat(model=MODEL, messages=[{'role': 'system', 'content': Prompt}, {'role': 'user', 'content': f'{first} + {second} = ?'}], options={'num_predict': (None if isSmart else 32), 'temperature': TEMPERATURE})
    if str(response['message']['content']).strip() == '': continue
    NewElement = str(response['message']['content']).strip()
    if LANGUAGE == 'en': print(f'\nYou now have a new {NewElement} element!')
    elif LANGUAGE == 'ru': print(f'\nУ вас теперь есть новый элемент {NewElement}!')
    elif LANGUAGE == 'ua': print(f'\nУ вас тепер є новий елемент {NewElement}!')

    if not (NewElement in Elements): Elements.append(NewElement)
    with open('Elements', 'w', encoding='utf-8') as f:
        Crypt = ';% '.join(Elements)
        f.write(Crypt)