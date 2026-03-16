import ollama

# === SETTINGS ===
MODEL = 'gemma3:1b' # 'ollama list' in OS terminal
LANGUAGE = 'ru'     # requires 'en'|'ru'|'ua'

Elements = []
with open('Elements', 'a', encoding='utf-8') as f: f.close()
with open('Elements', 'r', encoding='utf-8') as f:
    f = f.read()
    if (f == '') and (LANGUAGE == 'en'): Elements = ['Water', 'Earth', 'Fire']
    elif (f == '') and (LANGUAGE == 'ru'): Elements = ['Вода', 'Земля', 'Огонь']
    elif (f == '') and (LANGUAGE == 'ua'): Elements = ['Вода', 'Земля', 'Вогонь']
    else: Elements = f.split(';% ')

if LANGUAGE == 'en': Prompt = 'You\'re an alchemist\'s game.\n{first word} + {second word} = {insert your answer}\nWrite only the result.'
elif LANGUAGE == 'ru': Prompt = 'Ты - игра в алхимика.\n{первое слово} + {второе слово} = {вставь свой ответ}\nПиши только результат.'
elif LANGUAGE == 'ua': Prompt = 'Ти - гра в алхимика.\n{перше слово} + {друге слово} = {встав свою відповідь}\nПиши тільки результат.'
else: input(f'LANGUAGE error!\n{LANGUAGE=}, requires "en"|"ru"|"ua"'); quit()

while True:
    if LANGUAGE == 'en': print(f'\nYou have: {Elements}\nSelect two elements from this and they will connect:')
    elif LANGUAGE == 'ru': print(f'\nУ вас есть: {Elements}\nВыберите из этого два элемента и они соединятся:')
    elif LANGUAGE == 'ua': print(f'\nУ вас є: {Elements}\nВиберіть із цих двух елементів та вони з\'єднаються:')

    first = input('1> ')
    if not (first in Elements):
        if LANGUAGE == 'en': print(f'{first} is not a list item!'); continue
        elif LANGUAGE == 'ru': print(f'{first} не является элементом списка!'); continue
        elif LANGUAGE == 'ua': print(f'{first} не є елементом списка!'); continue

    second = input('2> ')
    if not (second in Elements):
        if LANGUAGE == 'en': print(f'{second} is not a list item!'); continue
        elif LANGUAGE == 'ru': print(f'{second} не является элементом списка!'); continue
        elif LANGUAGE == 'ua': print(f'{second} не є елементом списка!'); continue

    response = ollama.chat(model=MODEL, messages=[{'role': 'system', 'content': Prompt}, {'role': 'user', 'content': f'{first} + {second} = ?'}], options={'num_predict': 32})
    if response == '': continue
    NewElement = str(response['message']['content']).strip()
    if LANGUAGE == 'en': print(f'\nYou now have a new {NewElement} element!')
    elif LANGUAGE == 'ru': print(f'\nУ вас теперь есть новый элемент {NewElement}!')
    elif LANGUAGE == 'ua': print(f'\nУ вас тепер є новий елемент {NewElement}!')

    Elements.append(NewElement)
    with open('Elements', 'w', encoding='utf-8') as f:
        Crypt = ';% '.join(Elements)
        f.write(Crypt)