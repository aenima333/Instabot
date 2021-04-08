from instabot import Bot

bot = Bot()

bot.login(username='username', password='password')
bot.follow_followers('username')
bot.send_message("Tetxto",['username'])
bot.upload_photo("imagen.png", caption="generic code")
#Recuerda usar cada instruccion por separado comentando la linea de codigo que no vas a utilizar e instalar instabot
# pip install Instabot















