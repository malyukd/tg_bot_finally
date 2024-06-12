from aiogram import Router, F

router = Router()

@router.message(F.text == "/start")
async def start(message):
    await message.answer("Hi, I'm bot!")
    
