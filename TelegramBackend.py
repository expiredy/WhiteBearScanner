import subprocess
import time
import telebot
from PIL import Image, ImageDraw
from requests import get

bot = telebot.TeleBot("1764288430:AAET7WJM1Dgq0hiFh0jpZKzB_OALSxhQi7E")  # You can set parse_mode by default. HTML or MARKDOWN


def photo_interaction(message, file_info):
    bot.reply_to(message, "Starting preprocessing your photo")
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'image.jpg'
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    subprocess.run("AnalyzingSpace/image_preprocessor.exe")
    time.sleep(2)
    image_with_bears = Image.open('image_processed.png')
    draw = ImageDraw.Draw(image_with_bears)
    draw.rectangle((200, 100, 300, 200), outline="red", width=10)
    image_with_bears.save("image_processed.png")
    time.sleep(1)
    photo = open('image_processed.png', 'rb')
    return photo

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=["document"])
def echo_all(message):
    file_info = bot.get_file(message.document.file_id)
    photo = photo_interaction(message, file_info)
    bot.send_document(message.chat.id, photo)

@bot.message_handler(content_types=['photo'])
def echo_all(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    photo = photo_interaction(message, file_info)
    bot.send_photo(message.chat.id, photo)





bot.polling()
