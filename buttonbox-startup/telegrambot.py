#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:05:54 2020

@author: ludo

"""
import logging
from aiogram import Bot, Dispatcher, executor, types
# Bot Informations :
# name:"jalalabot" , username="t.me/jalala2020_moustache17_bot", TOKEN:"1259785871:AAGUgSGHdqB1LONIbCNt_qWJCig9WmhToxU"

API_TOKEN="1259785871:AAGUgSGHdqB1LONIbCNt_qWJCig9WmhToxU"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm ButtonBot!\nPowered by LSB and aiogram.")

executor.start_polling(dp, skip_updates=True)
