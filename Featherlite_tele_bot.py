from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os 
import telebot

bot = telebot.TeleBot('6683125242:AAHhsUJWj5b-e9wxa64V0hMFdXX7fhsnyks')

def tele_url (url,Location):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get(url)

    time.sleep(2)
    chat = driver.find_element(By.ID, 'details-button')
    chat.click()
    time.sleep(2)
    chat1 = driver.find_element(By.ID, 'proceed-link')
    chat1.click()
    time.sleep(2)
    username_input = driver.find_element(By.NAME, 'j_username')
    username_input.send_keys('admin')
    chat2 = driver.find_element(By.ID, 'login-submit')
    chat2.click()
    time.sleep(2)
    password_input = driver.find_element(By.NAME, 'j_password')
    password_input.send_keys('Admin@12345')
    chat3 = driver.find_element(By.ID, 'login-submit')
    chat3.click()
    time.sleep(2)

    driver.save_screenshot(r"C:\Users\Dell\Desktop\Telegram\{}.png".format(Location))

    driver.quit()
 

commands = ['/start', '/1FNORTH', '1FSOUTH', '/2FNORTH', '/2FSOUTH', '/3FNORTH', '/3FSOUTH','/4FNORTH', '4FSOUTH', '/5FNORTH', '/5FSOUTH', '/6FNORTH', '/6FSOUTH'
             '/7FNORTH', '7FSOUTH', '/8FNORTH', '/8FSOUTH', '/8FNORTH', '/9FSOUTH','/9FNORTH', '/GFNORTH', '/GFSOUTH', '/BACSU']

@bot.message_handler(content_types=['document'])
def handle_document(message):
    file_info = bot.get_file(message.document.file_id)
    file_path = file_info.file_path
    file_name = message.document.file_name

    
    save_path = r'C:\Users\Dell\Desktop\ARUN\Trash\Telegram\save' + file_name

    downloaded_file = bot.download_file(file_path)
    with open(save_path,'wb')as new_file:
        new_file.write(downloaded_file)

    bot.reply_to(message, 'File saved successfully!')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "HELLO, I AM A BOT OF ARUN FOR FEATHERLITE")

@bot.message_handler(commands=['4FNORTH', 'help'])
def send_image(message):
    
    URL = 'https://localhost/ord/station:%7Cslot:/Drivers/NiagaraNetwork/BA_1F_DDC2/points/AHU_DDC%7Cview:Graphic4'
    Location = '4FNORTH'
    my = tele_url(URL,Location)
    photo = open(r'C:\Users\Dell\Desktop\Telegram\{}.png'.format(Location),'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['2FSOUTH', 'help'])
def send_image(message):
    
    URL = 'https://localhost/ord/station:%7Cslot:/Drivers/NiagaraNetwork/BA_2F_SOUTH_DDC4/points/BA_2F_SOUTH_DDC%7Cview:Graphic4'
    Location = '2FSOUTH'
    my = tele_url(URL,Location)
    photo = open(r'C:\Users\Dell\Desktop\Telegram\{}.png'.format(Location),'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['1FSOUTH', 'help'])
def send_image(message):
    
    URL = 'https://localhost/ord/station:%7Cslot:/Drivers/NiagaraNetwork/BA_1F_DDC2/points/AHU_DDC%7Cview:Graphic4'
    Location = '1FSOUTH'
    my = tele_url(URL,Location)
    photo = open(r'C:\Users\Dell\Desktop\Telegram\{}.png'.format(Location),'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['2FNORTH', 'help'])
def send_image(message):
    
    URL = 'https://localhost/ord/station:%7Cslot:/Drivers/NiagaraNetwork/BA_2F_NORTH_DDC3/points/BA_2F_NORTH_DDC%7Cview:Graphic4'
    Location = '2FNORTH'
    my = tele_url(URL,Location)
    photo = open(r'C:\Users\Dell\Desktop\Telegram\{}.png'.format(Location),'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['3FNORTH', 'help'])
def send_image(message):
    
    URL = 'https://localhost/ord/station:%7Cslot:/Drivers/NiagaraNetwork/BA_3F_NORTH_DDC5/points/BA_3F_NORTH_DDC%7Cview:Graphic4'
    Location = '3FNORTH'
    my = tele_url(URL,Location)
    photo = open(r'C:\Users\Dell\Desktop\Telegram\{}.png'.format(Location),'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['ASUMMARY', 'help'])
def send_image(message):
    
    URL = 'https://localhost/ord/file:%5Epx/AHU/TowerA_AHU%20summary.px%7Cview:hx:HxPxView'
    Location = 'ASUMMARY'
    my = tele_url(URL,Location)
    photo = open(r'C:\Users\Dell\Desktop\Telegram\{}.png'.format(Location),'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['BSUMMARY', 'help'])
def send_image(message):
    
    URL = 'https://localhost/ord/file:%5Epx/AHU/AHU%20summary.px%7Cview:hx:HxPxView'
    Location = 'BSUMMARY'
    my = tele_url(URL,Location)
    photo = open(r'C:\Users\Dell\Desktop\Telegram\{}.png'.format(Location),'rb')
    bot.send_photo(message.chat.id, photo)

bot.polling()