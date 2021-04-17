import discord
import requests
from googletrans import Translator
import asyncio
import random

TOKEN = 'ODA4NjMwMjE4NTc0MjY2NDA4.YCJVkw.vvqCIqPeeXRjDvbSx_jCBqdnCSs'
with open('russia', encoding='utf-8') as f:
    rus = f.readlines()

'''
class WeatherReq():
    def __init__(self, city):
        self.API = '2c6c62ecc0d20abf473f5b3274545e06'
        self.req = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.API}')

    def m_info(self):
        if self.req.status_code == 500:
            return 'Wrong city name or something else'
        else:
            wth = self.req.json()
            print(wth)
            return (f'{wth["name"]}, {wth["sys"]["country"]}: ' \
                    f'{wth["main"]["temp"]}*F, {wth["weather"][0]["main"]}')

'''


class DisBot(discord.Client):
    async def on_ready(self):
        print(f'{self.user} подключён к Discord !!!! ')
        for guild in client.guilds:
            print(
                f'{client.user} подключился к тусе:\n'
                f'{guild.name} (id: {guild.id})'
            )
        self.ln_src = 'ru'
        self.ln_dest = 'en'

    async def on_message(self, message):
        if message.author == self.user:
            return
        if 'кот' in message.content.lower():
            res = requests.get('https://api.thecatapi.com/v1/images/search')
            await message.channel.send(res.json()[0]['url'])
        if 'собака' in message.content.lower():
            res = requests.get('https://dog.ceo/api/breeds/image/random')
            await message.channel.send(res.json()['message'])
        if message.content.lower() == '!help':
            await message.channel.send('''List of commands:
*!help* - command list
*!russia* - 
                '''
                                       )
        if message.content.lower() == 'привет кремлебот':
            await message.channel.send("Приветствую, гражданин самой великой державы")
        if message.content.lower() == '!russia':
            await message.channel.send(rus[random.randint(0, len(rus) - 1)])
        if 'кремлебот почему' in message.content.lower():
            if 'плох' in message.content.lower() or 'ужас' in message.content.lower() or 'гряз' in message.content.lower() or 'холод' in message.content.lower():
                await message.channel.send("Во всем виноваты враги с запада!")
            elif 'хорош' in message.content.lower() or 'прекр' in message.content.lower() or 'чист' in message.content.lower() or 'высокие зарплаты' in message.content.lower():
                await message.channel.send("Все благодаря Путину!")
            else:
                await message.channel.send(
                    "Это не важно. Нам нужно сплотиться вокруг сильного лидера и поддерживать духовные скрепы!")
        if message.content.lower() == '!putin':
            await message.channel.send(file=discord.File(f'{random.randint(1, 6)}.jpg'))
            await message.channel.send('Вот так должен выглядеть настоящий мужчина!')

        '''
        if message.content.startswith('!trans'):
            needtotr = message.content[6:]
            translator = Translator()
            translated_one = translator.translate(needtotr, dest='ru').text
            await message.channel.send(translated_one)
        if message.content.startswith('!change'):
            self.ln_src = message.content[8:10]
            self.ln_dest = message.content[11:13]
            await message.channel.send(f'{self.ln_src}-{self.ln_dest} are chosen')
        if message.content.startswith('!text'):
            needtotr = message.content[5:]
            translator = Translator()
            translated_one = translator.translate(needtotr, src=self.ln_src, dest=self.ln_dest).text
            await message.channel.send(translated_one)
'''
        if message.content.lower().startswith('!set_timer'):
            hours, minutes = int(message.content.split()[1]), int(message.content.split()[3])
            await message.channel.send(f'Таймер установлен на {hours} часов и  {minutes} минут')
            await asyncio.sleep(hours * 3600 + minutes * 60)
            await message.channel.send('Ваше время вышло :alarm_clock:')


client = DisBot()
client.run(TOKEN)
