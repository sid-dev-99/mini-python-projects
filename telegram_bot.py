#!/usr/bin/python3

import telegram
from telegram.ext import Updater, CommandHandler
from PIL import Image, ImageDraw
import remo

# Define a function to generate the wallpaper
def generate_wallpaper(update, context):
    # Generate a new wallpaper using the Pillow library
    img = Image.new('RGB', (800, 600), color = (0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), "Hello, World!", fill=(255,255,255))
    img.save('wallpaper.jpg')

    # Send the generated wallpaper to the user
    update.message.reply_photo(photo=open('wallpaper.jpg', 'rb'))

# Create a new Telegram bot
TOKEN = remo.API_KEY
bot = telegram.Bot(token=TOKEN)

# Create an updater object and add a CommandHandler to it
updater = Updater(TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler('wallpaper', generate_wallpaper))

# Start the bot
updater.start_polling()
updater.idle()
