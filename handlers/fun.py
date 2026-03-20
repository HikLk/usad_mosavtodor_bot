# from aiogram import Router, F
# from aiogram.types import Message
# 
# from config import BUTTON_ANDREY
# 
# router = Router(name="fun")
# 
# 
# @router.message(F.text == BUTTON_ANDREY)
# async def send_andrey_photo(message: Message):
#     photo_url = "https://i.ibb.co/XZ8GpFxV/photo-2025-09-19-15-29-08.jpg"
# 
#     try:
#         await message.answer_photo(
#             photo=photo_url,
#             caption="Вот Андрей 👀"
#         )
#     except Exception as e:
#         await message.answer(f"Не удалось отправить фото 😔\nОшибка: {str(e)}")