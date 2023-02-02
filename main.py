import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from aiogram.dispatcher import FSMContext
from personaldata import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)


@dp.message_handler(commands='anketa')
async def send_welcome(message: types.Message):
    await message.answer("To'liq ismingizni kiriting:")
    await PersonalData.fullname.set()

@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: types.Message, state=FSMContext):
    full_name = message.text
#   await state.update_data(name=fullname)
    await state.update_data(
        {'fullname': full_name}
    )
    await message.answer("Elektron pochtangizni kiriting:")
#   await PersonalData.next()
    await PersonalData.email.set()


@dp.message_handler(state=PersonalData.email)
async def answer_fullname(message: types.Message, state=FSMContext):
    e_mail = message.text
#   await state.update_data(name=fullname)
    await state.update_data(
        {'email': e_mail}
    )
    await message.answer("Telefon raqamingizni kiriting:")
#   await PersonalData.next()
    await PersonalData.phone.set()

@dp.message_handler(state=PersonalData.phone)
async def answer_fullname(message: types.Message, state=FSMContext):
    phone_number = message.text
#   await state.update_data(name=fullname)
    await state.update_data(
        {'phone': phone_number}
    )
    await message.answer("Manzilingizni kiriting:")
#   await PersonalData.next()
    await PersonalData.address.set()

@dp.message_handler(state=PersonalData.address)
async def answer_fullname(message: types.Message, state=FSMContext):
    address = message.text
#   await state.update_data(name=fullname)
    await state.update_data(
        {'address': address}
    )
    await message.answer("Tug'ilgan yilingizni kiriting:")
#   await PersonalData.next()
    await PersonalData.dob.set()

@dp.message_handler(state=PersonalData.dob)
async def answer_fullname(message: types.Message, state=FSMContext):
    date_of_birth = message.text
#   await state.update_data(name=fullname)
    await state.update_data(
        {'dob': date_of_birth}
    )

    data = await state.get_data()
    name = data.get("fullname name")
    email = data.get("email")
    phone = data.get("phone")
    address = data.get("address")
    dob = data.get("dob")

    msg = "Sizdan quyidagi ma'lumotlar olindi:\n"
    msg += f"To'liq ismingiz - {name}\n"
    msg += f"Elektron pochta - {email}\n"
    msg += f"Telefon raqam - {phone}\n"
    msg += f"Manzil - {address}\n"
    msg += f"Tug'ilgan yilingiz- {dob}\n"
    
    await message.answer(msg)

    await state.finish()








if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)