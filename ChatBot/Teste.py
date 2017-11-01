from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')

convI = ['oi', 'olá', 'olá, bom dia', 'bom dia', 'bom dia, como vai?', 'estou bem']

convFilme = ['que filme voccê gosta?', 'eu gosto de Ex Machine']

bot.set_trainer(ListTrainer)

bot.train(convI)
bot.train(convFilme)

while True:
    quest = input('Você: ')
    response = bot.get_response(quest)
    print('Bot:', response)