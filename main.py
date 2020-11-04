import telebot
from telebot import types

bot = telebot.TeleBot('1454773809:AAG33BTYdim-H_H_XzrK_EU8ZWaIQOVIHuw')


@bot.message_handler(commands=['start'])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    url_button = types.InlineKeyboardButton(text="instagram", url="https://www.instagram.com/kitep_kgz/?hl=ru")
    keyboard.add(url_button)

    u_keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    u_keyboard.row("catalog", "prices")
    bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name} {message.from_user.last_name}!",reply_markup=keyboard)
    bot.send_message(message.chat.id, "Choose action:", reply_markup=u_keyboard)

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == 'prices':
         bot.send_message(message.chat.id, '1.”Кармический менеджмент” МАЙКЛ РОУЧ-680 \n'
                                          '2.”Девушка в Dior” АННИ ГЕТЦИНГЕР-910с \n'
                                          '3.”Отец “ АБДУЛМАНАП НУРМАГОМЕДОВ, ИГОРЬ РЫБАКОВ-820с \n'
                                          '4."Феномен ZARA" КОВАДОНГА ОШИ-760c \n'
                                          '5."Чизкейк внутри" ВИКТОРИЯ МЕЛЬНИК-710 \n')
    if message.text == 'catalog':
        key = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton(text="1.”Кармический менеджмент” МАЙКЛ РОУЧ", callback_data='1')
        btn2 = types.InlineKeyboardButton(text='2.”Девушка в Dior” АННИ ГЕТЦИНГЕР', callback_data='2')
        btn3 = types.InlineKeyboardButton(text='3.”Отец “ АБДУЛМАНАП НУРМАГОМЕДОВ, ИГОРЬ РЫБАКОВ', callback_data='3')
        btn4 = types.InlineKeyboardButton (text='4."Феномен ZARA" КОВАДОНГА ОШИ', callback_data='4')
        btn5= types. InlineKeyboardButton (text='5."Чизкейк внутри" ВИКТОРИЯ МЕЛЬНИК', callback_data='5')

        key.add(btn,btn2,btn3,btn4,btn5)
        bot.send_message(message.chat.id, 'select a book' ,reply_markup=key)
@bot.callback_query_handler(func=lambda call:True)
def callback_worker(call):
    if call.message:
        if call.data =="1":
            bot.edit_message_text=('Как при помощи законов кармы создать сильный бизнес,наийти верных партнеров и увеличить продажи?В книге «Кармическиий менеджмент:эффект бумеранга в бизнесе и в жизни»вы узнаете, как благодаря системе 4 шагов можно посадить то,чего вы жаждете и осуществить свои мысли в реальность.')
        elif call.data == "2":
         bot.edit_message_text =('Книга «Девушка в Диор» прекрасно и интересно рассказывает о становлении Dior, о его работе через вымышленного персонажа – модного журналиста Клары Ноан.')
        elif call.data == "3":
         bot.edit_message_text=(' К сожалению, не у всех есть мудрые отцы-тренеры, которые способны вдохновлять, правильно поощрять и убеждать в праведности пути. Но к счастью, эта книга может заменить вам отца или наставника.  В книге вы узнаете какие навыки нужны для достижения выдающихся результатов в спорте, бизнесе и жизни.')
        elif call.data == "4":
         bot.edit_message_text=('Inditex Group – компания по продаже одежды номер один в мире и признанная законодательница моды. На улицах Нью-Йорка, Парижа, Токио, Москвы вы обязательно встретите красивых, уверенных в себе людей, на которых будут вещи таких брендов, как Zara, Massimo Dutti, Pull & Bear, Stradivarius, Oysho, Bershka. Магазины Inditex имеют неизменный успех по всему миру, а марку Zara по праву можно назвать культовой. ')
        elif call.data == "5":
         bot.edit_message_text = ('Ч, которые побили мировой рекорд в кулинарном мире. Так, наверное, можно сказать про первую книгу кондитера и популярного блогера Виктории Мельник «Чизкейк внутри», ставшую бестселлером в 2018 году. В понятные и доступные рецепты идеальных десертов влюбились тысячи домашних кондитеров. Вторая книга Виктории – перед вами. Абсолютно новые оригинальные авторские рецепты чизкейков и других сладостей, дополненные разделом теории. Восхитительные вдохновляющие фотографии и понятное описание приготовления. Почувствуйте себя настоящим кондитером!')
    bot.send_message(call.message.chat.id, bot.edit_message_text)

bot.polling(none_stop=True)
