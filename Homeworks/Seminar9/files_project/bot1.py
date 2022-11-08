import cmath
import datetime
from telebot import types
import telebot
from telebot import TeleBot
import math

bot = TeleBot('5467983987:AAF0S2mUejKSMilXUk_BWchyWrYI53689Ws')

keyboard = types.InlineKeyboardMarkup()
keyboard.row(   types.InlineKeyboardButton('j', callback_data='j'),
                types.InlineKeyboardButton('C', callback_data='c'),
                types.InlineKeyboardButton('<=', callback_data='<='),
                types.InlineKeyboardButton('Pi', callback_data='pi'))

keyboard.row(   types.InlineKeyboardButton('%', callback_data='%'),
                types.InlineKeyboardButton('1/x', callback_data='1/x'),
                types.InlineKeyboardButton('x^2', callback_data='x^2'),
                types.InlineKeyboardButton('√', callback_data='2^x'))

keyboard.row(   types.InlineKeyboardButton('sin', callback_data='sin'),
                types.InlineKeyboardButton('cos', callback_data='cos'),
                types.InlineKeyboardButton('tg', callback_data='tan'),
                types.InlineKeyboardButton('/', callback_data='/'))

keyboard.row(   types.InlineKeyboardButton('7', callback_data='7'),
                types.InlineKeyboardButton('8', callback_data='8'),
                types.InlineKeyboardButton('9', callback_data='9'),
                types.InlineKeyboardButton('*', callback_data='*'))

keyboard.row(   types.InlineKeyboardButton('4', callback_data='4'),
                types.InlineKeyboardButton('5', callback_data='5'),
                types.InlineKeyboardButton('6', callback_data='6'),
                types.InlineKeyboardButton('-', callback_data='-'))

keyboard.row(   types.InlineKeyboardButton('1', callback_data='1'),
                types.InlineKeyboardButton('2', callback_data='2'),
                types.InlineKeyboardButton('3', callback_data='3'),
                types.InlineKeyboardButton('+', callback_data='+'))

keyboard.row(   types.InlineKeyboardButton('+/-', callback_data='+/-'),
                types.InlineKeyboardButton('0', callback_data='0'),
                types.InlineKeyboardButton(',', callback_data='.'),
                types.InlineKeyboardButton('=', callback_data='='))

keyboard.row(   types.InlineKeyboardButton('(', callback_data='('),
                types.InlineKeyboardButton(')', callback_data=')'))

value = ''
old_value = ''
Help_MESSAGE = '/start, /calculater - вызывают калькулятор \n/log - бот пришлет файл логирования событий(историю)'


def logger_action(action: str):
    today = datetime.datetime.today()
    with open('log.txt', 'a', encoding='utf-8') as data:
        data.write(\
            f'{today.strftime("%Y-%m-%d-(%H) %H:%M")} Пользователь {action} \n')


@bot.message_handler(content_types=['document'])
def hello_document(msg: types.Message):
    file = bot.get_file(msg.document.file_id)
    downloaded_file = bot.download_file(file.file_path)
    with open(msg.document.file_name, 'wb') as f_out:
        f_out.write(downloaded_file)
    logger_action(f'{msg.from_user} загрузил документ: {msg.document.file_name}.')


@bot.message_handler(commands=['help'])
def help_answer(message: types.Message):
    logger_action('посмотрел справку.')
    bot.send_message(message.from_user.id, text=Help_MESSAGE)


@bot.message_handler(commands=['log'])
def bay_bay_log(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='лог')
    logger_action(f'{msg.from_user} скачал файл логгера.')
    bot.send_document(msg.from_user.id, document=open('log.txt', 'rb'))


@bot.message_handler(commands=['start', 'calculater'])
def start(message: telebot.types.Message):
    logger_action('запустил калькулятор.')
    global value
    if value == '':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_function(query):
    global value, old_value
    data = query.data

    logger_action(f'внес данные: {data} .')
    if data == 'no':
        pass
    elif data == 'c':
        if old_value != '':
            value = ''
        else:
            pass
    elif data == '%':
        if value != '':
            try:
                value = str((eval(value) / 100))
            except:
                value = 'Error'
        else:
            pass
    elif data == 'sin':
        if value != '':
            try:
                value = str(math.sin(eval(value)))
            except:
                try:
                    value = str(cmath.sin(eval(value)))
                except:
                    value = 'Error'
        else:
            value = str(math.sin(0))
        logger_action(f'получил значение {value}')
    elif data == 'cos':
        if value != '':
            try:
                value = str(math.cos(eval(value)))
            except:
                try:
                    value = str(cmath.cos(eval(value)))
                except:
                    value = 'Error'
        else:
            value = str(math.cos(0))
        logger_action(f'получил значение {value}')
    elif data == 'tan':
        if value != '':
            try:
                value = str(math.tan(eval(value)))
            except:
                try:
                    value = str(cmath.tan(eval(value)))
                except:
                    value = 'Error'
        else:
            value = str(math.tan(0))
        logger_action(f'получил значение {value}')
    elif data == 'pi':
        value += str(math.pi)
    elif data == '1/x':
        if value != '':
            try:
                value = str(1 / (eval(value)))
            except:
                value = 'Error'
            logger_action(f'получил значение {value}')
        else:
            pass
    elif data == 'x^2':
        if value != '':
            try:
                value = str(pow(eval(value), 2))
            except:
                value = 'Error'
            logger_action(f'получил значение {value}')
        else:
            pass
    elif data == '2^x':
        if value != '':
            try:
                if value.count('j'):
                    value = str(cmath.sqrt(eval(value)))
                else:
                    value = str(math.sqrt(eval(value)))
            except:
                value = 'Error'
            logger_action(f'получил значение {value}')
        else:
            pass
    elif data == '=':
        try:
            if value.count('j'):
                logger_action('производит расчеты с комплексными числами.')
            logger_action(f'ввел пример: {value}')
            value = str(eval(value))
            logger_action(f'получил значение: {value} .')
        except Exception:
            value = 'Error'
            logger_action(f'получил ошибку вычисления.')
    elif data == '<=':
        if value != '':
            value = value[:-1]
            logger_action(f'получил значение {value}')
        else:
            pass
    elif data == '+/-':
        try:
            value = str( eval(value) * -1 )
            logger_action(f'получил значение {value}')
        except:
            value = 'Error'
    elif data == '0':
        try:
            if old_value != '0':
                value += data
            else:
                raise Exception
        except Exception:
            value = 'Error'
    elif data == 'j':
        if value[-1] != 'j':
            value += data
        else:
            pass
    else:
        if (value == '0' and not data.isdigit()) or value != '0':
            value += data
        elif value == '0' and data.isdigit():
            value += data
            value = value[1:]
    try:
        if (value != old_value and value != '') \
            or (old_value != '0' and value == ''):
            if value == '':
                bot.edit_message_text(\
                    chat_id=query.message.chat.id,\
                        message_id=query.message.message_id,\
                            text='0',\
                                reply_markup=keyboard)
                old_value = '0'
            else:
                bot.edit_message_text(\
                    chat_id=query.message.chat.id,\
                        message_id=query.message.message_id,\
                            text=value, reply_markup=keyboard)
                old_value = value
        else:
            raise Exception
    except Exception:
        value = 'Error'
    old_value = value

    if value == 'Error':
        logger_action('получил ошибку ввода')
        value = ''


bot.polling(non_stop=True, interval=0)
