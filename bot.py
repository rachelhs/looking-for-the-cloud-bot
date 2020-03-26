from rivescript import RiveScript
import os

file = os.path.dirname(__file__)
brain = os.path.join(file, 'brain')

bot = RiveScript()
bot.load_directory(brain)
bot.sort_replies()

while True:
	msg = str(input('You> '))

	if msg == 'q':
		break

	else:
		print('Bot>'+bot.reply('localuser', msg))