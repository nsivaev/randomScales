import telebot
import random

# Создаем экземпляр бота и указываем токен
bot = telebot.TeleBot('6020939166:AAFO2iroqaO197_rBD7vDUVD7b1KPlVwoyw')

# Устанавливаем клавиатуру для стартового сообщения
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'lets play!', reply_markup=keyboard)

# Создаем клавиатуру с кнопками
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = telebot.types.KeyboardButton('random')
button2 = telebot.types.KeyboardButton('определенное кол-во знаков')
button3 = telebot.types.KeyboardButton('до скольки знаков?')
keyboard.add(button1, button2, button3)

# Глобальная переменная для хранения отправленных строк
sent_strings = []





# Обрабатываем нажатие на первую кнопку

@bot.message_handler(func=lambda message: message.text == 'random')
def handle_button1_click(message):
    # Создаем список строк
    strings = ['C-dur', 'a-moll', 'G-dur', 'e-moll', 'D-dur', 'h-moll', 'A-dur', 'fis-moll', 'E-dur', 'cis-moll', 'H-dur', 'gis-moll', 'Fis-dur', 'dis-moll', 'Cis-dur', 'ais-moll', 'F-dur', 'd-moll', 'B-dur', 'g-moll', 'Es-dur', 'c-moll', 'As-dur', 'f-moll', 'Des-dur', 'b-moll', 'Ges-dur', 'es-moll', 'Ces-dur', 'as-moll']
    # Ищем строки, которые еще не были отправлены
    unsent_strings = list(set(strings) - set(sent_strings))
    # Если все строки уже были отправлены, начинаем выборку заново
    if not unsent_strings:
        sent_strings.clear()
        unsent_strings = strings
    # Генерируем случайный индекс элемента списка
    random_index = random.randint(0, len(unsent_strings) - 1)
    # Выбираем случайную строку из списка
    random_string = unsent_strings[random_index]
    # Добавляем выбранную строку в список отправленных
    sent_strings.append(random_string)
    # Отправляем выбранную строку пользователю
    bot.send_message(message.chat.id, random_string)





# Обрабатываем нажатие на вторую кнопку

@bot.message_handler(func=lambda message: message.text == 'определенное кол-во знаков')
def handle_button2_click(message):
    # Создаем клавиатуру с кнопками уровней
    level_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    level_buttons = ['noob (0)', '1 знак', '2 знака', '3 знака', '4 знака', '5 знаков', '6 знаков', 'pro (7)']
    for button in level_buttons:
        level_keyboard.add(telebot.types.KeyboardButton(button))
    # Отправляем клавиатуру пользователю
    bot.send_message(message.chat.id, 'Выберите уровень:', reply_markup=level_keyboard)

# Обработчики нажатия на кнопки уровней
@bot.message_handler(func=lambda message: message.text == 'noob (0)')
def handle_level1_click(message):
    strings = ['C-dur', 'a-moll']
    # Ищем строки, которые еще не были отправлены
    unsent_strings = list(set(strings) - set(sent_strings))
    # Если все строки уже были отправлены, начинаем выборку заново
    if not unsent_strings:
        sent_strings.clear()
        unsent_strings = strings
    # Генерируем случайный индекс элемента списка
    random_index = random.randint(0, len(unsent_strings) - 1)
    # Выбираем случайную строку из списка
    random_string = unsent_strings[random_index]
    # Добавляем выбранную строку в список отправленных
    sent_strings.append(random_string)
    # Отправляем выбранную строку пользователю
    bot.send_message(message.chat.id, random_string)

@bot.message_handler(func=lambda message: message.text == '1 знак')
def handle_level2_click(message):
    strings = ['G-dur', 'e-moll', 'F-dur', 'd-moll']
    # Ищем строки, которые еще не были отправлены
    unsent_strings = list(set(strings) - set(sent_strings))
    # Если все строки уже были отправлены, начинаем выборку заново
    if not unsent_strings:
        sent_strings.clear()
        unsent_strings = strings
    # Генерируем случайный индекс элемента списка
    random_index = random.randint(0, len(unsent_strings) - 1)
    # Выбираем случайную строку из списка
    random_string = unsent_strings[random_index]
    # Добавляем выбранную строку в список отправленных
    sent_strings.append(random_string)
    # Отправляем выбранную строку пользователю
    bot.send_message(message.chat.id, random_string)

@bot.message_handler(func=lambda message: message.text == '2 знака')
def handle_level2_click(message):
    strings = ['D-dur', 'h-moll', 'B-dur', 'g-moll']
    # Ищем строки, которые еще не были отправлены
    unsent_strings = list(set(strings) - set(sent_strings))
    # Если все строки уже были отправлены, начинаем выборку заново
    if not unsent_strings:
        sent_strings.clear()
        unsent_strings = strings
    # Генерируем случайный индекс элемента списка
    random_index = random.randint(0, len(unsent_strings) - 1)
    # Выбираем случайную строку из списка
    random_string = unsent_strings[random_index]
    # Добавляем выбранную строку в список отправленных
    sent_strings.append(random_string)
    # Отправляем выбранную строку пользователю
    bot.send_message(message.chat.id, random_string)

@bot.message_handler(func=lambda message: message.text == '3 знака')
def handle_level2_click(message):
    strings = ['A-dur', 'fis-moll', 'Es-dur', 'c-moll']
    # Ищем строки, которые еще не были отправлены
    unsent_strings = list(set(strings) - set(sent_strings))
    # Если все строки уже были отправлены, начинаем выборку заново
    if not unsent_strings:
        sent_strings.clear()
        unsent_strings = strings
    # Генерируем случайный индекс элемента списка
    random_index = random.randint(0, len(unsent_strings) - 1)
    # Выбираем случайную строку из списка
    random_string = unsent_strings[random_index]
    # Добавляем выбранную строку в список отправленных
    sent_strings.append(random_string)
    # Отправляем выбранную строку пользователю
    bot.send_message(message.chat.id, random_string)

@bot.message_handler(func=lambda message: message.text == '4 знака')
def handle_level2_click(message):
    strings = ['E-dur' 'cis-moll', 'As-dur', 'f-moll']
    # Ищем строки, которые еще не были отправлены
    unsent_strings = list(set(strings) - set(sent_strings))
    # Если все строки уже были отправлены, начинаем выборку заново
    if not unsent_strings:
        sent_strings.clear()
        unsent_strings = strings
    # Генерируем случайный индекс элемента списка
    random_index = random.randint(0, len(unsent_strings) - 1)
    # Выбираем случайную строку из списка
    random_string = unsent_strings[random_index]
    # Добавляем выбранную строку в список отправленных
    sent_strings.append(random_string)
    # Отправляем выбранную строку пользователю
    bot.send_message(message.chat.id, random_string)

@bot.message_handler(func=lambda message: message.text == '5 знаков')
def handle_level2_click(message):
    strings = ['H-dur', 'gis-moll', 'Des-dur', 'b-moll']
    # Ищем строки, которые еще не были отправлены
    unsent_strings = list(set(strings) - set(sent_strings))
    # Если все строки уже были отправлены, начинаем выборку заново
    if not unsent_strings:
        sent_strings.clear()
        unsent_strings = strings
    # Генерируем случайный индекс элемента списка
    random_index = random.randint(0, len(unsent_strings) - 1)
    # Выбираем случайную строку из списка
    random_string = unsent_strings[random_index]
    # Добавляем выбранную строку в список отправленных
    sent_strings.append(random_string)
    # Отправляем выбранную строку пользователю
    bot.send_message(message.chat.id, random_string)

@bot.message_handler(func=lambda message: message.text == '6 знаков')
def handle_level2_click(message):
    strings = ['Fis-dur', 'dis-moll', 'Ges-dur', 'es-moll']
    # Ищем строки, которые еще не были отправлены
    unsent_strings = list(set(strings) - set(sent_strings))
    # Если все строки уже были отправлены, начинаем выборку заново
    if not unsent_strings:
        sent_strings.clear()
        unsent_strings = strings
    # Генерируем случайный индекс элемента списка
    random_index = random.randint(0, len(unsent_strings) - 1)
    # Выбираем случайную строку из списка
    random_string = unsent_strings[random_index]
    # Добавляем выбранную строку в список отправленных
    sent_strings.append(random_string)
    # Отправляем выбранную строку пользователю
    bot.send_message(message.chat.id, random_string)

@bot.message_handler(func=lambda message: message.text == 'pro (7)')
def handle_level2_click(message):
    strings = ['Cis-dur', 'ais-moll', 'Ces-dur', 'as-moll']
    # Ищем строки, которые еще не были отправлены
    unsent_strings = list(set(strings) - set(sent_strings))
    # Если все строки уже были отправлены, начинаем выборку заново
    if not unsent_strings:
        sent_strings.clear()
        unsent_strings = strings
    # Генерируем случайный индекс элемента списка
    random_index = random.randint(0, len(unsent_strings) - 1)
    # Выбираем случайную строку из списка
    random_string = unsent_strings[random_index]
    # Добавляем выбранную строку в список отправленных
    sent_strings.append(random_string)
    # Отправляем выбранную строку пользователю
    bot.send_message(message.chat.id, random_string)





# Обрабатываем нажатие на третью кнопку

@bot.message_handler(func=lambda message: message.text == 'до скольки знаков?')
def handle_button2_click(message):
    # Создаем клавиатуру с кнопками уровней
    level_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    level_buttons = ['noob (0)', 'до 1 знака', 'до 2 знаков', 'до 3 знаков', 'до 4 знаков', 'до 5 знаков', 'до 6 знаков', 'pro (до 7 знаков)']
    for button in level_buttons:
        level_keyboard.add(telebot.types.KeyboardButton(button))
    # Отправляем клавиатуру пользователю
    bot.send_message(message.chat.id, 'Выберите уровень:', reply_markup=level_keyboard)

# Обработчики нажатия на кнопки уровней
@bot.message_handler(func=lambda message: message.text == 'noob (0)')
def handle_level1_click(message):
    strings = ['C-dur', 'a-moll']
    # Ищем строки, которые еще не были отправлены
    unsent_strings = list(set(strings) - set(sent_strings))
    # Если все строки уже были отправлены, начинаем выборку заново
    if not unsent_strings:
        sent_strings.clear()
        unsent_strings = strings
    # Генерируем случайный индекс элемента списка
    random_index = random.randint(0, len(unsent_strings) - 1)
    # Выбираем случайную строку из списка
    random_string = unsent_strings[random_index]
    # Добавляем выбранную строку в список отправленных
    sent_strings.append(random_string)
    # Отправляем выбранную строку пользователю
    bot.send_message(message.chat.id, random_string)

@bot.message_handler(func=lambda message: message.text == 'до 1 знака')
def handle_level2_click(message):
    strings = ['G-dur', 'e-moll', 'F-dur', 'd-moll', 'C-dur', 'a-moll']
    # Ищем строки, которые еще не были отправлены
    unsent_strings = list(set(strings) - set(sent_strings))
    # Если все строки уже были отправлены, начинаем выборку заново
    if not unsent_strings:
        sent_strings.clear()
        unsent_strings = strings
    # Генерируем случайный индекс элемента списка
    random_index = random.randint(0, len(unsent_strings) - 1)
    # Выбираем случайную строку из списка
    random_string = unsent_strings[random_index]
    # Добавляем выбранную строку в список отправленных
    sent_strings.append(random_string)
    # Отправляем выбранную строку пользователю
    bot.send_message(message.chat.id, random_string)

@bot.message_handler(func=lambda message: message.text == 'до 2 знаков')
def handle_level2_click(message):
    strings = ['D-dur', 'h-moll', 'B-dur', 'g-moll', 'G-dur', 'e-moll', 'F-dur', 'd-moll', 'C-dur', 'a-moll']
    # Ищем строки, которые еще не были отправлены
    unsent_strings = list(set(strings) - set(sent_strings))
    # Если все строки уже были отправлены, начинаем выборку заново
    if not unsent_strings:
        sent_strings.clear()
        unsent_strings = strings
    # Генерируем случайный индекс элемента списка
    random_index = random.randint(0, len(unsent_strings) - 1)
    # Выбираем случайную строку из списка
    random_string = unsent_strings[random_index]
    # Добавляем выбранную строку в список отправленных
    sent_strings.append(random_string)
    # Отправляем выбранную строку пользователю
    bot.send_message(message.chat.id, random_string)

@bot.message_handler(func=lambda message: message.text == 'до 3 знаков')
def handle_level2_click(message):
    strings = ['A-dur', 'fis-moll', 'Es-dur', 'c-moll', 'D-dur', 'h-moll', 'B-dur', 'g-moll', 'G-dur', 'e-moll', 'F-dur', 'd-moll', 'C-dur', 'a-moll']
    # Ищем строки, которые еще не были отправлены
    unsent_strings = list(set(strings) - set(sent_strings))
    # Если все строки уже были отправлены, начинаем выборку заново
    if not unsent_strings:
        sent_strings.clear()
        unsent_strings = strings
    # Генерируем случайный индекс элемента списка
    random_index = random.randint(0, len(unsent_strings) - 1)
    # Выбираем случайную строку из списка
    random_string = unsent_strings[random_index]
    # Добавляем выбранную строку в список отправленных
    sent_strings.append(random_string)
    # Отправляем выбранную строку пользователю
    bot.send_message(message.chat.id, random_string)

@bot.message_handler(func=lambda message: message.text == 'до 4 знаков')
def handle_level2_click(message):
    strings = ['E-dur', 'cis-moll', 'As-dur', 'f-moll', 'A-dur', 'fis-moll', 'Es-dur', 'c-moll', 'D-dur', 'h-moll', 'B-dur', 'g-moll', 'G-dur', 'e-moll', 'F-dur', 'd-moll', 'C-dur', 'a-moll']
    # Ищем строки, которые еще не были отправлены
    unsent_strings = list(set(strings) - set(sent_strings))
    # Если все строки уже были отправлены, начинаем выборку заново
    if not unsent_strings:
        sent_strings.clear()
        unsent_strings = strings
    # Генерируем случайный индекс элемента списка
    random_index = random.randint(0, len(unsent_strings) - 1)
    # Выбираем случайную строку из списка
    random_string = unsent_strings[random_index]
    # Добавляем выбранную строку в список отправленных
    sent_strings.append(random_string)
    # Отправляем выбранную строку пользователю
    bot.send_message(message.chat.id, random_string)

@bot.message_handler(func=lambda message: message.text == 'до 5 знаков')
def handle_level2_click(message):
    strings = ['H-dur', 'gis-moll', 'Des-dur', 'b-moll', 'E-dur', 'cis-moll', 'As-dur', 'f-moll', 'A-dur', 'fis-moll', 'Es-dur', 'c-moll', 'D-dur', 'h-moll', 'B-dur', 'g-moll', 'G-dur', 'e-moll', 'F-dur', 'd-moll', 'C-dur', 'a-moll']
    # Ищем строки, которые еще не были отправлены
    unsent_strings = list(set(strings) - set(sent_strings))
    # Если все строки уже были отправлены, начинаем выборку заново
    if not unsent_strings:
        sent_strings.clear()
        unsent_strings = strings
    # Генерируем случайный индекс элемента списка
    random_index = random.randint(0, len(unsent_strings) - 1)
    # Выбираем случайную строку из списка
    random_string = unsent_strings[random_index]
    # Добавляем выбранную строку в список отправленных
    sent_strings.append(random_string)
    # Отправляем выбранную строку пользователю
    bot.send_message(message.chat.id, random_string)

@bot.message_handler(func=lambda message: message.text == 'до 6 знаков')
def handle_level2_click(message):
    strings = ['Fis-dur', 'dis-moll', 'Ges-dur', 'es-moll', 'H-dur', 'gis-moll', 'Des-dur', 'b-moll', 'E-dur', 'cis-moll', 'As-dur', 'f-moll', 'A-dur', 'fis-moll', 'Es-dur', 'c-moll', 'D-dur', 'h-moll', 'B-dur', 'g-moll', 'G-dur', 'e-moll', 'F-dur', 'd-moll', 'C-dur', 'a-moll']
    # Ищем строки, которые еще не были отправлены
    unsent_strings = list(set(strings) - set(sent_strings))
    # Если все строки уже были отправлены, начинаем выборку заново
    if not unsent_strings:
        sent_strings.clear()
        unsent_strings = strings
    # Генерируем случайный индекс элемента списка
    random_index = random.randint(0, len(unsent_strings) - 1)
    # Выбираем случайную строку из списка
    random_string = unsent_strings[random_index]
    # Добавляем выбранную строку в список отправленных
    sent_strings.append(random_string)
    # Отправляем выбранную строку пользователю
    bot.send_message(message.chat.id, random_string)

@bot.message_handler(func=lambda message: message.text == 'pro (до 7 знаков)')
def handle_level2_click(message):
    strings = ['Cis-dur', 'ais-moll', 'Ces-dur', 'as-moll', 'Fis-dur', 'dis-moll', 'Ges-dur', 'es-moll', 'H-dur', 'gis-moll', 'Des-dur', 'b-moll', 'E-dur', 'cis-moll', 'As-dur', 'f-moll', 'A-dur', 'fis-moll', 'Es-dur', 'c-moll', 'D-dur', 'h-moll', 'B-dur', 'g-moll', 'G-dur', 'e-moll', 'F-dur', 'd-moll', 'C-dur', 'a-moll']
    # Ищем строки, которые еще не были отправлены
    unsent_strings = list(set(strings) - set(sent_strings))
    # Если все строки уже были отправлены, начинаем выборку заново
    if not unsent_strings:
        sent_strings.clear()
        unsent_strings = strings
    # Генерируем случайный индекс элемента списка
    random_index = random.randint(0, len(unsent_strings) - 1)
    # Выбираем случайную строку из списка
    random_string = unsent_strings[random_index]
    # Добавляем выбранную строку в список отправленных
    sent_strings.append(random_string)
    # Отправляем выбранную строку пользователю
    bot.send_message(message.chat.id, random_string)


# Запускаем бота
bot.polling(non_stop=True)
