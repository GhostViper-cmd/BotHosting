import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

API_TOKEN = '7262077945:AAFgL_FUdyrsla0MBK6-2T8ER1GDhzDFvec'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

questions = {
    "uz": [
        {"question": "1. Python qanday tilda yozilgan?", "options": ["A) Kompilyator", "B) Interpritator", "C) HTML"], "answer": "B"},
        {"question": "2. Python'da ro'yxat qanday belgilanadi?", "options": ["A) {}", "B) []", "C) ()"], "answer": "B"},
        {"question": "3. 'print()' funksiyasi nima qiladi?", "options": ["A) Ma'lumotni kiritadi", "B) Chiqaradi", "C) O'chiradi"], "answer": "B"},
        {"question": "4. Telegram botni yaratishda qaysi kutubxona ishlatiladi?", "options": ["A) Flask", "B) NumPy", "C) Aiogram"], "answer": "C"},
        {"question": "5. GitHub nima?", "options": ["A) Hosting", "B) IDE", "C) Matn muharriri"], "answer": "A"},
        {"question": "6. Git komandasi bilan loyiha qanday yuklanadi?", "options": ["A) git pull", "B) git push", "C) git load"], "answer": "B"},
        {"question": "7. 'git init' komandasi nima qiladi?", "options": ["A) Yangi branch yaratadi", "B) Git reposini boshlaydi", "C) Faylni ochadi"], "answer": "B"},
        {"question": "8. Aiogram kutubxonasi nimaga asoslangan?", "options": ["A) Asinxronlik", "B) Sinxronlik", "C) Grafik interfeys"], "answer": "A"},
        {"question": "9. Python'da o'zgaruvchi qanday e'lon qilinadi?", "options": ["A) int a = 5", "B) var a = 5", "C) a = 5"], "answer": "C"},
        {"question": "10. 'asyncio' kutubxonasi nima uchun kerak?", "options": ["A) Sinxron kod yozish", "B) Asinxron kod yozish", "C) Fayl bilan ishlash"], "answer": "B"},
        {"question": "11. HTML nima uchun ishlatiladi?", "options": ["A) Stil berish", "B) Tuzilish berish", "C) Dasturlash"], "answer": "B"},
        {"question": "12. CSS nima uchun kerak?", "options": ["A) Interaktivlik", "B) Tuzilish", "C) Dizayn"], "answer": "C"},
        {"question": "13. JavaScript qayerda ishlaydi?", "options": ["A) Faqat serverda", "B) Brauzerda", "C) Faqat backendda"], "answer": "B"},
        {"question": "14. API nima?", "options": ["A) Ma'lumotlar ombori", "B) Foydalanuvchi interfeysi", "C) Dastur interfeysi"], "answer": "C"},
        {"question": "15. Gitda 'commit' nima?", "options": ["A) Yangi kod yozish", "B) O‘zgarishni saqlash", "C) Faylni ochish"], "answer": "B"},
        {"question": "16. Botga inline tugma qanday qo'shiladi?", "options": ["A) ReplyKeyboardMarkup", "B) InlineKeyboardMarkup", "C) MenuMarkup"], "answer": "B"},
        {"question": "17. Bot tokeni qayerdan olinadi?", "options": ["A) Google", "B) BotFather", "C) Aiogram"], "answer": "B"}
    ],
    "ru": [
        {"question": "1. На каком языке написан Python?", "options": ["A) Компилятор", "B) Интерпретатор", "C) HTML"], "answer": "B"},
        {"question": "2. Как обозначается список в Python?", "options": ["A) {}", "B) []", "C) ()"], "answer": "B"},
        {"question": "3. Что делает функция 'print()'?", "options": ["A) Вводит данные", "B) Выводит", "C) Удаляет"], "answer": "B"},
        {"question": "4. Какая библиотека используется для создания Telegram бота?", "options": ["A) Flask", "B) NumPy", "C) Aiogram"], "answer": "C"},
        {"question": "5. Что такое GitHub?", "options": ["A) Хостинг", "B) IDE", "C) Текстовый редактор"], "answer": "A"},
        {"question": "6. Какая команда Git используется для загрузки проекта?", "options": ["A) git pull", "B) git push", "C) git load"], "answer": "B"},
        {"question": "7. Что делает команда 'git init'?", "options": ["A) Создает новую ветку", "B) Инициализирует Git репозиторий", "C) Открывает файл"], "answer": "B"},
        {"question": "8. На чем основана библиотека Aiogram?", "options": ["A) Асинхронность", "B) Синхронность", "C) Графический интерфейс"], "answer": "A"},
        {"question": "9. Как объявляется переменная в Python?", "options": ["A) int a = 5", "B) var a = 5", "C) a = 5"], "answer": "C"},
        {"question": "10. Для чего нужна библиотека 'asyncio'?", "options": ["A) Синхронный код", "B) Асинхронный код", "C) Работа с файлами"], "answer": "B"},
        {"question": "11. Для чего используется HTML?", "options": ["A) Стилизация", "B) Структура", "C) Программирование"], "answer": "B"},
        {"question": "12. Для чего нужен CSS?", "options": ["A) Интерктивность", "B) Структура", "C) Дизайн"], "answer": "C"},
        {"question": "13. Где работает JavaScript?", "options": ["A) Только на сервере", "B) В браузере", "C) Только на бэкенде"], "answer": "B"},
        {"question": "14. Что такое API?", "options": ["A) Хранилище данных", "B) Пользовательский интерфейс", "C) Интерфейс программы"], "answer": "C"},
        {"question": "15. Что такое 'commit' в Git?", "options": ["A) Написание нового кода", "B) Сохранение изменений", "C) Открытие файла"], "answer": "B"},
        {"question": "16. Как добавить inline кнопку в бота?", "options": ["A) ReplyKeyboardMarkup", "B) InlineKeyboardMarkup", "C) MenuMarkup"], "answer": "B"},
        {"question": "17. Откуда берется токен бота?", "options": ["A) Google", "B) BotFather", "C) Aiogram"], "answer": "B"}
    ],
    "en": [
        {"question": "1. What type of language is Python?", "options": ["A) Compiler", "B) Interpreter", "C) HTML"], "answer": "B"},
        {"question": "2. How is a list defined in Python?", "options": ["A) {}", "B) []", "C) ()"], "answer": "B"},
        {"question": "3. What does the 'print()' function do?", "options": ["A) Input data", "B) Output data", "C) Delete data"], "answer": "B"},
        {"question": "4. Which library is used to create a Telegram bot?", "options": ["A) Flask", "B) NumPy", "C) Aiogram"], "answer": "C"},
        {"question": "5. What is GitHub?", "options": ["A) Hosting", "B) IDE", "C) Text editor"], "answer": "A"},
        {"question": "6. Which Git command is used to upload a project?", "options": ["A) git pull", "B) git push", "C) git load"], "answer": "B"},
        {"question": "7. What does the 'git init' command do?", "options": ["A) Creates a new branch", "B) Initializes a Git repository", "C) Opens a file"], "answer": "B"},
        {"question": "8. What is Aiogram library based on?", "options": ["A) Asynchronous", "B) Synchronous", "C) Graphical interface"], "answer": "A"},
        {"question": "9. How is a variable declared in Python?", "options": ["A) int a = 5", "B) var a = 5", "C) a = 5"], "answer": "C"},
        {"question": "10. What is the purpose of the 'asyncio' library?", "options": ["A) Writing synchronous code", "B) Writing asynchronous code", "C) Working with files"], "answer": "B"},
        {"question": "11. What is HTML used for?", "options": ["A) Styling", "B) Structure", "C) Programming"], "answer": "B"},
        {"question": "12. What is CSS for?", "options": ["A) Interactivity", "B) Structure", "C) Design"], "answer": "C"},
        {"question": "13. Where does JavaScript run?", "options": ["A) Only on the server", "B) In the browser", "C) Only on the backend"], "answer": "B"},
        {"question": "14. What is an API?", "options": ["A) Data storage", "B) User interface", "C) Application interface"], "answer": "C"},
        {"question": "15. What is a 'commit' in Git?", "options": ["A) Writing new code", "B) Saving changes", "C) Opening a file"], "answer": "B"},
        {"question": "16. How to add an inline button to a bot?", "options": ["A) ReplyKeyboardMarkup", "B) InlineKeyboardMarkup", "C) MenuMarkup"], "answer": "B"},
        {"question": "17. Where do you get the bot token?", "options": ["A) Google", "B) BotFather", "C) Aiogram"], "answer": "B"}
    ]
}

user_data = {}

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="O'zbek", callback_data="lang_uz"),
        InlineKeyboardButton(text="Русский", callback_data="lang_ru"),
        InlineKeyboardButton(text="English", callback_data="lang_en")
    )
    await message.answer("Tilni tanlang / Choose language / Выберите язык:", reply_markup=builder.as_markup())

@dp.callback_query(lambda c: c.data.startswith("lang_"))
async def select_language(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    lang_code = callback.data.replace("lang_", "")
    user_data[user_id] = {"lang": lang_code, "step": 0, "score": 0}
    await callback.message.answer({
        "uz": "Testni boshlaymiz! Javob variantini tanlang.",
        "ru": "Начинаем тест! Выберите вариант ответа.",
        "en": "Let's start the test! Please select an answer."
    }[lang_code])
    await ask_question(user_id)

async def ask_question(user_id: int):
    lang = user_data[user_id]["lang"]
    step = user_data[user_id]["step"]

    if step >= len(questions[lang]):
        score = user_data[user_id]["score"]
        total = len(questions[lang])
        await bot.send_message(user_id, f"Test tugadi! Sizning natijangiz: {score} / {total}")
        return

    q = questions[lang][step]
    text = q["question"] + "\n" + "\n".join(q["options"])

    builder = InlineKeyboardBuilder()
    for option in q["options"]:
        option_letter = option[0]  # A, B, C
        builder.button(text=option, callback_data=f"answer_{option_letter}")
    builder.adjust(1)

    await bot.send_message(user_id, text, reply_markup=builder.as_markup())

@dp.callback_query(lambda c: c.data.startswith("answer_"))
async def answer_chosen(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    if user_id not in user_data:
        await callback.answer("Iltimos, /start buyrug'ini yuboring.")
        return

    user = user_data[user_id]
    lang = user["lang"]
    step = user["step"]
    user_answer = callback.data[-1]
    correct_answer = questions[lang][step]["answer"]

    if user_answer == correct_answer:
        user["score"] += 1
        await callback.answer("To'g'ri javob!")
    else:
        await callback.answer(f"Noto'g'ri javob! To'g'ri javob: {correct_answer}")

    user["step"] += 1
    await ask_question(user_id)

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot, skip_updates=True))
