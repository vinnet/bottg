import requests
import pickle
import datetime
from time import gmtime, strftime
from datetime import timedelta, datetime
import telebot
import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from telebot import types

clear = lambda: os.system('cls')

url1 = 'https://game-tournaments.com/dota-2'
url = 'https://game-tournaments.com'
url2 = 'https://game-tournaments.com/csgo'
jacascrpt = 'https://game-tournaments.comjavascript:;'

bot = telebot.TeleBot('993258364:AAEA58fPxdOOencktnGjtCnI_BZdzda9WG0')

table_prof = [{'ID': 457225002, 'NAME': 'Калы', 'DATE': '9999.01.01'}]
table_admin = [{'ID': 457225002, 'NAME': 'Калы', 'DATE': '9999.01.01'}]
table_analys = []




@bot.message_handler(commands=['help', 'start'])
def start(message):
    prof_idx = 0

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('id')
    btn2 = types.KeyboardButton('Анализировать')
    btn3 = types.KeyboardButton('О подписке')
    markup.add(btn1, btn2, btn3)
    send_mess = f"<b>Приветствую {message.from_user.first_name} ! </b>\nНапиши 'id', чтобы узнать id  "
    prof_idx = prof_idx + 1
    prof_idxa = prof_idx - 1
    with open('idx.pickle', 'wb') as f:
        pickle.dump(prof_idxa, f)
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    final_mess = ""
    back_mess = "Назад"
    with open('data.pickle', 'rb') as f:
        table_analys = pickle.load(f)
    time = strftime("%Y.%m.%d", gmtime())
    with open('idx.pickle', 'rb') as f:
        prof_idxa = pickle.load(f)
    if message.text == 'id':
        bot.send_message(message.chat.id, 'Ваш id:')
        bot.send_message(message.chat.id, message.from_user.id)
        bot.send_message(message.chat.id, 'Теперь отправьте этот id: https://t.me/Ban_Valued')
    elif message.text == 'О подписке':
        bot.send_message(message.chat.id, '\n'
                                          '\n'
                                          '                           Бот находится в разработке!'
                                          '\n'
                                          '\n'
                                          'Привет! Я бот, который выдает прогнозы на кибер спорт, анализируя матчи, с помощью искуственного интелекта! '
                                          'Каждый день я собираю статистику с разных сайтов и улучшаю себя! Буду рад тебя видеть в рядах людей, которые нуждаются во мне!\n'                     
                                          '\n'
                                          '             Прайс-лист:\n'
                                          '\n'
                                          '1 месяц - 300 рублей\n'
                                          '3 месяца - 700 рублей\n'
                                          'Для оплаты писать: https://t.me/Ban_Valued')
    elif message.text == 'Анализировать':
        idf = 0
        d = 0
        a = int(message.from_user.id)
        if idf < 1:
            for i in table_analys:
                id = int(table_analys[d]['ID'])
                date = str(table_analys[d]['DATE'])
                d = d + 1
                if a == id and date > time:
                    bot.send_message(message.chat.id, 'Ваша подписка закончится: ')
                    bot.send_message(message.chat.id, date)
                    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                    idf = idf + 1
                    btn4 = types.KeyboardButton('CS:GO')
                    btn5 = types.KeyboardButton('DOTA 2(NOT-WORK)')
                    btn9 = types.KeyboardButton('Домой')
                    markup1.add(btn4, btn5, btn9)
                    bot.send_message(message.chat.id, 'Выберите спорт', reply_markup=markup1)
        if idf == 0:
            bot.send_message(message.chat.id,'Вам этот раздел не доступен, свяжитесь с https://t.me/Ban_Valued, чтобы оплатить подписку')
    elif message.text == 'CS:GO':
        idf = 0
        d = 0
        a = int(message.from_user.id)
        if idf < 1:
            for i in table_analys:
                id = int(table_analys[d]['ID'])
                date = str(table_analys[d]['DATE'])
                d = d + 1
                if a == id and date > time:
                    idx = 0
                    num = 0
                    page = requests.get(url2)
                    soup = BeautifulSoup(page.content, "html.parser")
                    tables = soup.select('div[id^="block_matches_current"]')  # таблица с сайта
                    table1 = []
                    clear()
                    for table in tables:  # парсинг команд
                        bot.send_message(message.chat.id,
                                         '\n          Расписание матчей CS:GO (game-tournaments)\n')

                        trs = table.select('tr')

                        for tr in trs:
                            l = "LIVE (tested)"
                            if tr.attrs.get('class'):
                                team1 = tr.select_one('.teamname.c1')
                                team2 = tr.select_one('.teamname.c2')
                                href = urljoin(url1, tr.select_one('.mlink').get('href'))
                                match = requests.get(href)
                                soup = BeautifulSoup(match.content, "html.parser")
                                tournaments = soup.select('div[class^="match-nav-mobile"]')
                                for tournament in tournaments:
                                    hreft = tournament.select_one('a').get('href')
                                matchs = soup.select('div[class^="match-info"]')
                                a = 0
                                for match in matchs:
                                    h33 = match.select('h3')
                                    for h3 in h33:
                                        if h3.attrs.get('class'):
                                            if a <= 0:
                                                href1 = h3.select_one('a').get('href')
                                                href1 = url + href1
                                            elif a > 0:
                                                href2 = h3.select_one('a').get('href')
                                                href2 = url + href2
                                            a = a + 1
                                hreft = url + hreft
                                tournament = requests.get(hreft)
                                soup = BeautifulSoup(tournament.content, "html.parser")

                                table1.append({
                                    'NUMBER': idx + 1,
                                    'TEAM1': team1.text.strip(),
                                    'HREF1': href1,
                                    'TEAM2': team2.text.strip(),
                                    'HREF2': href2,
                                    'HREF': href,
                                    'HREFT': url + hreft})
                                bot.send_message(message.chat.id,
                                                 '{}. {} VS {} ({})'.format(idx + 1, team1.text.strip(),
                                                                            team2.text.strip(),
                                                                            l))

                                idx = idx + 1

                            else:
                                team1 = tr.select_one('.teamname.c1')
                                team2 = tr.select_one('.teamname.c2')
                                href = urljoin(url1, tr.select_one('.mlink').get('href'))

                                match = requests.get(href)
                                soup = BeautifulSoup(match.content, "html.parser")
                                tournaments = soup.select('div[class^="match-nav-mobile"]')
                                for tournament in tournaments:
                                    hreft = tournament.select_one('a').get('href')
                                matchs = soup.select('div[class^="match-info"]')
                                a = 0
                                for match in matchs:
                                    h33 = match.select('h3')
                                    for h3 in h33:
                                        if h3.attrs.get('class'):
                                            if a <= 0:
                                                href1 = h3.select_one('a').get('href')
                                                href1 = url+ href1
                                            elif a > 0:
                                                href2 = h3.select_one('a').get('href')
                                                href2 = url + href2
                                            a = a + 1
                                hreft = url + hreft
                                tournament = requests.get(hreft)
                                soup = BeautifulSoup(tournament.content, "html.parser")
                                table1.append({
                                    'NUMBER': idx + 1,
                                    'TEAM1': team1.text.strip(),
                                    'HREF1': href1,
                                    'TEAM2': team2.text.strip(),
                                    'HREF2': href2,
                                    'HREF': href,
                                    'HREFT': hreft})
                                final1 = []
                                final2 = []
                                href11 = table1[idx]['HREF1']
                                if href11 != jacascrpt:
                                    team11 = requests.get(href11)
                                    soup = BeautifulSoup(team11.content, "html.parser")
                                    places1 = soup.select('div[class^="col col-xs-3"]')
                                    a = 0
                                    for i in places1:
                                        if a == 0:
                                            place1 = i.select_one('b').get_text()
                                            place1 = str(place1.split()[0])
                                            if place1 == '–':
                                                place1 = 999
                                            elif place1 == '0':
                                                place1 = 999
                                            a = a + 1
                                        elif a == 1:
                                            forma1 = i.select_one('b').get_text()
                                            forma1 = str(forma1.split()[0])
                                            if forma1 == '–':
                                                forma1 = 0
                                            elif forma1 == '0':
                                                forma1 = 0
                                            a = a + 1
                                        elif a == 2:
                                            wins1 = i.select_one('b').get_text()
                                            wins1 = str(wins1.split()[0])
                                            if wins1 == '–':
                                                wins1 = 0
                                            elif wins1 != '–':
                                                wins1 = int(wins1)
                                            a = a + 1
                                        elif a == 3:
                                            loses1 = str(i.select_one('b').get_text())
                                            loses1 = str(loses1.split()[0])
                                            if loses1 == '–':
                                                loses1 = 0
                                            elif loses1 != '–':
                                                loses1 = int(loses1)
                                            a = 0

                                    try:
                                        winpercent1 = round(wins1 / (wins1 + loses1) * 100)
                                    except ZeroDivisionError:
                                        winpercent1 = 0
                                    matches1 = wins1 + loses1
                                    final1.append({
                                        'PLACE1': place1,
                                        'FORMA1': forma1,
                                        'WINS1': wins1,
                                        'WINPERCENT1': winpercent1,
                                        'LOSES1': loses1,
                                        'MATCHES1': matches1
                                    })
                                href22 = table1[idx]['HREF2']
                                if href22 != jacascrpt:
                                    team22 = requests.get(href22)
                                    soup = BeautifulSoup(team22.content, "html.parser")
                                    places2 = soup.select('div[class^="col col-xs-3"]')
                                    a = 0
                                    for i in places2:
                                        if a == 0:
                                            place2 = i.select_one('b').get_text()
                                            place2 = str(place2.split()[0])
                                            if place2 == '–':
                                                place2 = 999
                                            elif place2 == '0':
                                                place2 = 999
                                            a = a + 1
                                        elif a == 1:
                                            forma2 = i.select_one('b').get_text()
                                            forma2 = str(forma2.split()[0])
                                            if forma2 == '–':
                                                forma2 = 0
                                            elif forma2 == '0':
                                                forma2 = 0
                                            a = a + 1
                                        elif a == 2:
                                            wins2 = i.select_one('b').get_text()
                                            wins2 = str(wins2.split()[0])
                                            if wins2 == '–':
                                                wins2 = 0
                                            elif wins2 != '–':
                                                wins2 = int(wins2)
                                            a = a + 1
                                        elif a == 3:
                                            loses2 = str(i.select_one('b').get_text())
                                            loses2 = str(loses2.split()[0])
                                            if loses2 == '–':
                                                loses2 = 0
                                            elif loses2 != '–':
                                                loses2 = int(loses2)
                                            a = 0
                                    try:
                                        winpercent2 = round(wins2 / (wins2 + loses2) * 100)
                                    except ZeroDivisionError:
                                        winpercent2 = 0
                                    matches2 = wins2 + loses2
                                    final2.append({
                                        'PLACE2': place2,
                                        'FORMA2': forma2,
                                        'WINS2': wins2,
                                        'WINPERCENT2': winpercent2,
                                        'LOSES2': loses2,
                                        'MATCHES2': matches2
                                    })
                                prof_idx1 = 0
                                prof_idx2 = 0
                                place1 = int(final1[0]['PLACE1'])
                                forma1 = int(final1[0]['FORMA1'])
                                wins1 = int(final1[0]['WINS1'])
                                winpercent1 = int(final1[0]['WINPERCENT1'])
                                loses1 = int(final1[0]['LOSES1'])
                                matches1 = int(final1[0]['MATCHES1'])

                                place2 = int(final2[0]['PLACE2'])
                                forma2 = int(final2[0]['FORMA2'])
                                wins2 = int(final2[0]['WINS2'])
                                winpercent2 = int(final2[0]['WINPERCENT2'])
                                loses2 = int(final2[0]['LOSES2'])
                                matches2 = int(final2[0]['MATCHES2'])

                                if place1 == place2:
                                    prof_idx1 = prof_idx1 + 1
                                    prof_idx2 = prof_idx2 + 1
                                    if wins1 == wins2:
                                        prof_idx1 = prof_idx1 + 1
                                        prof_idx2 = prof_idx2 + 1
                                        if winpercent1 == winpercent2:
                                            prof_idx1 = prof_idx1 + 1
                                            prof_idx2 = prof_idx2 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                        elif winpercent1 > winpercent2:
                                            prof_idx1 = prof_idx1 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                        elif winpercent2 > winpercent1:
                                            prof_idx2 = prof_idx2 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                    elif wins1 > wins2:
                                        prof_idx1 = prof_idx1 + 1
                                        if winpercent1 == winpercent2:
                                            prof_idx1 = prof_idx1 + 1
                                            prof_idx2 = prof_idx2 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                        elif winpercent1 > winpercent2:
                                            prof_idx1 = prof_idx1 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                        elif winpercent2 > winpercent1:
                                            prof_idx2 = prof_idx2 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                    elif wins2 > wins1:
                                        prof_idx2 = prof_idx2 + 1
                                        if winpercent1 == winpercent2:
                                            prof_idx1 = prof_idx1 + 1
                                            prof_idx2 = prof_idx2 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                        elif winpercent1 > winpercent2:
                                            prof_idx1 = prof_idx1 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                        elif winpercent2 > winpercent1:
                                            prof_idx2 = prof_idx2 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                elif place1 > place2:
                                    prof_idx2 = prof_idx2 + 1
                                    if wins1 == wins2:
                                        prof_idx1 = prof_idx1 + 1
                                        prof_idx2 = prof_idx2 + 1
                                        if winpercent1 == winpercent2:
                                            prof_idx1 = prof_idx1 + 1
                                            prof_idx2 = prof_idx2 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                        elif winpercent1 > winpercent2:
                                            prof_idx1 = prof_idx1 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                        elif winpercent2 > winpercent1:
                                            prof_idx2 = prof_idx2 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                    elif wins1 > wins2:
                                        prof_idx1 = prof_idx1 + 1
                                        if winpercent1 == winpercent2:
                                            prof_idx1 = prof_idx1 + 1
                                            prof_idx2 = prof_idx2 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                        elif winpercent1 > winpercent2:
                                            prof_idx1 = prof_idx1 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                        elif winpercent2 > winpercent1:
                                            prof_idx2 = prof_idx2 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                    elif wins2 > wins1:
                                        prof_idx2 = prof_idx2 + 1
                                        if winpercent1 == winpercent2:
                                            prof_idx1 = prof_idx1 + 1
                                            prof_idx2 = prof_idx2 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                        elif winpercent1 > winpercent2:
                                            prof_idx1 = prof_idx1 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                        elif winpercent2 > winpercent1:
                                            prof_idx2 = prof_idx2 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                elif place2 > place1:
                                    prof_idx1 = prof_idx1 + 1
                                    if wins1 == wins2:
                                        prof_idx1 = prof_idx1 + 1
                                        prof_idx2 = prof_idx2 + 1
                                        if winpercent1 == winpercent2:
                                            prof_idx1 = prof_idx1 + 1
                                            prof_idx2 = prof_idx2 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                        elif winpercent1 > winpercent2:
                                            prof_idx1 = prof_idx1 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                        elif winpercent2 > winpercent1:
                                            prof_idx2 = prof_idx2 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                    elif wins1 > wins2:
                                        prof_idx1 = prof_idx1 + 1
                                        if winpercent1 == winpercent2:
                                            prof_idx1 = prof_idx1 + 1
                                            prof_idx2 = prof_idx2 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                        elif winpercent1 > winpercent2:
                                            prof_idx1 = prof_idx1 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                        elif winpercent2 > winpercent1:
                                            prof_idx2 = prof_idx2 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                    elif wins2 > wins1:
                                        prof_idx2 = prof_idx2 + 1
                                        if winpercent1 == winpercent2:
                                            prof_idx1 = prof_idx1 + 1
                                            prof_idx2 = prof_idx2 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                        elif winpercent1 > winpercent2:
                                            prof_idx1 = prof_idx1 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                        elif winpercent2 > winpercent1:
                                            prof_idx2 = prof_idx2 + 1
                                            if loses1 == loses2:
                                                prof_idx1 = prof_idx1 + 1
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses1 > loses2:
                                                prof_idx2 = prof_idx2 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                            elif loses2 > loses1:
                                                prof_idx1 = prof_idx1 + 1
                                                if matches1 == matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                    prof_idx2 = prof_idx2 + 1
                                                elif matches1 > matches2:
                                                    prof_idx1 = prof_idx1 + 1
                                                elif matches2 > matches1:
                                                    prof_idx2 = prof_idx2 + 1
                                final_idx = prof_idx1 + prof_idx2
                                final_idx1 = round(prof_idx1 / (final_idx) * 100)
                                final_idx2 = round(prof_idx2 / (final_idx) * 100)
                                bot.send_message(message.chat.id,

                                                     '{}. ({}%) {}  VS {} ({}%)'.format(idx + 1,final_idx1, team1.text.strip(),
                                                                           team2.text.strip(), final_idx2))
                                idx = idx + 1
                    bot.send_message(message.chat.id, 'Анализ завершен! ')

    elif message.text == 'DOTA 2':
        idf = 0
        d = 0
        a = int(message.from_user.id)
        if idf < 1:
            for i in table_analys:
                id = int(table_analys[d]['ID'])
                date = str(table_analys[d]['DATE'])
                d = d + 1
                if a == id and date > time:
                    idx = 0
                    num = 0
                    page = requests.get(url1)
                    soup = BeautifulSoup(page.content, "html.parser")
                    tables = soup.select('div[id^="block_matches_current"]')  # таблица с сайта
                    table1 = []
                    clear()
                    for table in tables:  # парсинг команд
                        bot.send_message(message.chat.id,
                                         '\n          Расписание матчей Dota 2 (game-tournaments)\n')

                        trs = table.select('tr')

                        for tr in trs:
                            l = "LIVE (tested)"
                            if tr.attrs.get('class'):
                                team1 = tr.select_one('.teamname.c1')
                                team2 = tr.select_one('.teamname.c2')
                                href = urljoin(url1, tr.select_one('.mlink').get('href'))

                                match = requests.get(href)
                                soup = BeautifulSoup(match.content, "html.parser")
                                tournaments = soup.select('div[class^="match-nav-mobile"]')
                                for tournament in tournaments:
                                    hreft = tournament.select_one('a').get('href')
                                matchs = soup.select('div[class^="match-info"]')
                                a = 0
                                for match in matchs:
                                    h33 = match.select('h3')
                                    for h3 in h33:
                                        if h3.attrs.get('class'):
                                            if a <= 0:
                                                href1 = h3.select_one('a').get('href')
                                                href1 = url + href1
                                            elif a > 0:
                                                href2 = h3.select_one('a').get('href')
                                                href2 = url + href2
                                            a = a + 1
                                hreft = url + hreft
                                tournament = requests.get(hreft)
                                soup = BeautifulSoup(tournament.content, "html.parser")
                                fonds = soup.select('span[class^="userbet"]')
                                for fonds1 in fonds:
                                    fond = fonds1.select_one('b').get_text()
                                table1.append({
                                    'NUMBER': idx + 1,
                                    'TEAM1': team1.text.strip(),
                                    'HREF1': href1,
                                    'TEAM2': team2.text.strip(),
                                    'HREF2': href2,
                                    'HREF': href,
                                    'FOND': fond,
                                    'HREFT': url + hreft})
                                bot.send_message(message.chat.id,
                                                 '{}. {} VS {} ({})'.format(idx + 1, team1.text.strip(),
                                                                            team2.text.strip(),
                                                                            l))

                                idx = idx + 1

                            else:
                                team1 = tr.select_one('.teamname.c1')
                                team2 = tr.select_one('.teamname.c2')
                                href = urljoin(url1, tr.select_one('.mlink').get('href'))

                                match = requests.get(href)
                                soup = BeautifulSoup(match.content, "html.parser")
                                tournaments = soup.select('div[class^="match-nav-mobile"]')
                                for tournament in tournaments:
                                    hreft = tournament.select_one('a').get('href')
                                matchs = soup.select('div[class^="match-info"]')
                                a = 0
                                for match in matchs:
                                    h33 = match.select('h3')
                                    for h3 in h33:
                                        if h3.attrs.get('class'):
                                            if a <= 0:
                                                href1 = h3.select_one('a').get('href')
                                                href1 = url + href1
                                            elif a > 0:
                                                href2 = h3.select_one('a').get('href')
                                                href2 = url + href2
                                            a = a + 1
                                hreft = url + hreft
                                tournament = requests.get(hreft)
                                soup = BeautifulSoup(tournament.content, "html.parser")
                                fonds = soup.select('span[class^="userbet"]')
                                for fonds1 in fonds:
                                    fond = fonds1.select_one('b').get_text()
                                table1.append({
                                    'NUMBER': idx + 1,
                                    'TEAM1': team1.text.strip(),
                                    'HREF1': href1,
                                    'TEAM2': team2.text.strip(),
                                    'HREF2': href2,
                                    'HREF': href,
                                    'FOND': fond,
                                    'HREFT': hreft})

                                bot.send_message(message.chat.id,
                                                 '{}. {} VS {}'.format(idx + 1, team1.text.strip(),
                                                                       team2.text.strip()))
                                idx = idx + 1

                    bot.send_message(message.chat.id, 'Анализ завершен! ')
                    print(table1)

    elif message.text == '/admin':
        if message.from_user.id == table_admin[0]['ID']:
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn6 = types.KeyboardButton('Посмотреть список подписок')
            btn7 = types.KeyboardButton('Добавить пользователя')
            btn8 = types.KeyboardButton('Удалить пользователя')
            btn9 = types.KeyboardButton('Домой')
            markup2.add(btn6, btn7, btn8, btn9)
            bot.send_message(message.chat.id, 'Что будем делать?', reply_markup=markup2)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton('id')
            btn2 = types.KeyboardButton('Анализировать')
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=markup)
    elif message.text == 'Посмотреть список подписок':
        if message.from_user.id == table_admin[0]['ID']:
            d = 0
            with open('data.pickle', 'rb') as f:
                table_analys = pickle.load(f)
            for i in table_analys:
                id = int(table_analys[d]['ID'])
                name = str(table_analys[d]['NAME'])
                date = str(table_analys[d]['DATE'])
                d = d+1
                bot.send_message(message.chat.id, d - 1)
                bot.send_message(message.chat.id, id)
                bot.send_message(message.chat.id, name)
                bot.send_message(message.chat.id, date)

    elif message.text == 'Добавить пользователя':
        if message.from_user.id == table_admin[0]['ID']:
            send = bot.send_message(message.chat.id, 'Введите ID, DATE  ')
            bot.register_next_step_handler(send, add_user)
    elif message.text == 'Удалить пользователя':
        if message.from_user.id == table_admin[0]['ID']:
            send = bot.send_message(message.chat.id, 'Порядковый номер')
            bot.register_next_step_handler(send, del_user)
    elif message.text == 'Домой':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('id')
        btn2 = types.KeyboardButton('Анализировать')
        btn3 = types.KeyboardButton('О подписке')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=markup)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('id')
        btn2 = types.KeyboardButton('Анализировать')
        btn3 = types.KeyboardButton('О подписке')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=markup)

def del_user(message):
    if message.text == 'Назад':
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn6 = types.KeyboardButton('Посмотреть список подписок')
        btn7 = types.KeyboardButton('Добавить пользователя')
        btn8 = types.KeyboardButton('Удалить пользователя')
        btn9 = types.KeyboardButton('Домой')
        markup2.add(btn6, btn7, btn8, btn9)
        bot.send_message(message.chat.id, 'Что будем делать?', reply_markup=markup2)
    else:
        with open('data.pickle', 'rb') as f:
            table_analys = pickle.load(f)
        idx_prof = message.text.split()[0]
        idx_prof = int(idx_prof)

        del table_analys[idx_prof]
        print(table_analys)
        with open('data.pickle', 'wb') as f:
            pickle.dump(table_analys, f)
        bot.send_message(message.chat.id, 'Пользователь удален')



def add_user(message):
    table_prof = []
    if message.text == 'Назад':
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn6 = types.KeyboardButton('Посмотреть список подписок')
        btn7 = types.KeyboardButton('Добавить пользователя')
        btn8 = types.KeyboardButton('Удалить пользователя')
        btn9 = types.KeyboardButton('Домой')
        markup2.add(btn6, btn7, btn8, btn9)
        bot.send_message(message.chat.id, 'Что будем делать?', reply_markup=markup2)
    else:
        userid = int(message.text.split()[0])
        date = message.text.split()[1]
        UsrInfo = bot.get_chat_member(userid, userid).user
        name = str(UsrInfo.first_name)
        with open('data.pickle', 'rb') as f:
            table_analys = pickle.load(f)
        table_analys.append({
            'ID': userid,
            'NAME': name,
            'DATE': date
        })
        print(table_analys)
        with open('data.pickle', 'wb') as f:
            pickle.dump(table_analys, f)
        bot.send_message(message.chat.id, 'Пользователь добавлен')
bot.polling(none_stop=True)