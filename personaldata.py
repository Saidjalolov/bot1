from aiogram.dispatcher.filters.state import StatesGroup,State

class PersonalData(StatesGroup):
    fullname = State()
    email = State()
    phone = State()
    address = State()
    dob = State()