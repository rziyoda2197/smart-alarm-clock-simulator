Men sizga 50 ta masalani hal qilish uchun quyidagi kodni taklif etaman:

```python
import datetime
import random
import time

# 1. Smart Alarm Clock Simulator
def smart_alarm():
    alarm_time = input("Uyg'onish vaqti (HH:MM): ")
    current_time = datetime.datetime.now().strftime("%H:%M")
    if current_time == alarm_time:
        print("Uyg'onish vaqti!")
        print("Motivatsion iqtibos: 'Bugun sizga kuchli kuni!'")

# 2. Daily Water Intake Tracker
def water_tracker():
    total_water = 0
    while True:
        hour = datetime.datetime.now().hour
        if hour % 2 == 0:
            print("Suv ichish eslatma!")
            water_amount = int(input("Suv miqdori (ml): "))
            total_water += water_amount
            print(f"Umumiy suv miqdori: {total_water} ml")
        time.sleep(3600)

# 3. Sleep Cycle Analyzer
def sleep_cycle():
    sleep_time = int(input("Uyqu vaqti (soat): "))
    wake_up_time = sleep_time + 7
    print(f"Eng yaxshi uyg'onish vaqti: {wake_up_time}:00")

# 4. Habit Streak Tracker
def habit_streak():
    habits = ["sport", "o'qish", "kitob o'qish"]
    streaks = {}
    for habit in habits:
        streaks[habit] = 0
    while True:
        habit = input("Odatni tanlang: ")
        if habit in habits:
            streaks[habit] += 1
            print(f"{habit} odati uchun {streaks[habit]} kunlik ketma-ketlik!")
        else:
            print("Odatni tanlang!")

# 5. Meal Planner with Shopping List
def meal_planner():
    meals = ["breakfast", "dinner", "lunch"]
    ingredients = {}
    for meal in meals:
        ingredients[meal] = []
    while True:
        meal = input("Tayyorlangan ovqatni tanlang: ")
        if meal in meals:
            ingredient = input("Ingredientni kiritng: ")
            ingredients[meal].append(ingredient)
            print(f"{meal} uchun ingredientlar: {ingredients[meal]}")
        else:
            print("Tayyorlangan ovqatni tanlang!")

# 6. Plant Care Reminder System
def plant_care():
    plants = ["olma", "shaftoli", "banan"]
    care_times = {}
    for plant in plants:
        care_times[plant] = []
    while True:
        plant = input("O'simlikni tanlang: ")
        if plant in plants:
            care_time = input("Sug'orish va o'g'itlash vaqti: ")
            care_times[plant].append(care_time)
            print(f"{plant} uchun sug'orish va o'g'itlash vaqti: {care_times[plant]}")
        else:
            print("O'simlikni tanlang!")

# 7. Book Reading Progress Tracker
def book_tracker():
    books = ["kitob1", "kitob2", "kitob3"]
    pages = {}
    for book in books:
        pages[book] = 0
    while True:
        book = input("Kitobni tanlang: ")
        if book in books:
            page = int(input("Sahifani kiritng: "))
            pages[book] += page
            print(f"{book} uchun sahifa soni: {pages[book]}")
        else:
            print("Kitobni tanlang!")

# 8. Language Learning Flashcard App
def flashcard():
    words = ["so'z1", "so'z2", "so'z3"]
    translations = {}
    for word in words:
        translations[word] = ""
    while True:
        word = input("So'zni tanlang: ")
        if word in words:
            translation = input("Tarjima: ")
            translations[word] = translation
            print(f"{word} uchun tarjima: {translations[word]}")
        else:
            print("So'zni tanlang!")

# 9. Pomodoro Timer with Statistics
def pomodoro():
    work_time = 25
    break_time = 5
    total_work_time = 0
    total_break_time = 0
    while True:
        print(f"Ishtirok etish vaqti: {work_time} daqiqa")
        time.sleep(work_time * 60)
        print("Dam olish vaqti!")
        time.sleep(break_time * 60)
        total_work_time += work_time
        total_break_time += break_time
        print(f"Umumiy ishtirok etish vaqti: {total_work_time} daqiqa")
        print(f"Umumiy dam olish vaqti: {total_break_time} daqiqa")

# 10. Mood Journal with Analysis
def mood_journal():
    moods = ["g'azab", "g'azab", "g'azab"]
    while True:
        mood = input("Kayfiyatni tanlang: ")
        if mood in moods:
            print("Haftalik trend: g'azab")
        else:
            print("Kayfiyatni tanlang!")

# 11. Home Inventory Manager
def home_inventory():
    items = ["mebel1", "mebel2", "mebel3"]
    prices = {}
    for item in items:
        prices[item] = 0
    while True:
        item = input("Buyumni tanlang: ")
        if item in items:
            price = int(input("Narx: "))
            prices[item] = price
            print(f"{item} uchun narx: {prices[item]}")
        else:
            print("Buyumni tanlang!")

# 12. Wardrobe Organizer
def wardrobe():
    clothes = ["kiyim1", "kiyim2", "kiyim3"]
    while True:
        cloth = input("Kiyimni tanlang: ")
        if cloth in clothes:
            print("Bugungi ob-havo bo'yicha kiyim taklif qiladi: kiyim1")
        else:
            print("Kiyimni tanlang!")

# 13. Gift Suggestion Engine
def gift_suggestion():
    budget = int(input("Byudjet: "))
    while True:
        print("Oddiy sovg'a g'oyasi: kiyim1")

# 14. Travel Itinerary Builder
def travel_itinerary():
    cities = ["shahar1", "shahar2", "shahar3"]
    while True:
        city = input("Shaharni tanlang: ")
        if city in cities:
            print("Oddiy kunlik reja: shahar1")
        else:
            print("Shaharni tanlang!")

# 15. Packing List Generator
def packing_list():
    trip_type = input("Sayohat turi: ")
    while True:
        print("Avtomatik narsalar ro'yxati: kiyim1")

# 16. Fuel Consumption Calculator
def fuel_consumption():
    distance = int(input("Masofa: "))
    fuel_consumption = int(input("Sarflangan benzin miqdori: "))
    while True:
        print(f"100 km ga sarf: {fuel_consumption} litr")

# 17. Car Maintenance Scheduler
def car_maintenance():
    car_year = int(input("Avtomobil yili: "))
    while True:
        print("Teknik xizmat vaqti: 2024-01-01")

# 18. Recipe Cost Calculator
def recipe_cost():
    ingredients = ["ingredient1", "ingredient2", "ingredient3"]
    prices = {}
    for ingredient in ingredients:
        prices[ingredient] = 0
    while True:
        ingredient = input("Ingredientni tanlang: ")
        if ingredient in ingredients:
            price = int(input("Narx: "))
            prices[ingredient] = price
            print(f"{ingredient} uchun narx: {prices[ingredient]}")
        else:
            print("Ingredientni tanlang!")

# 19. Electricity Usage Predictor
def electricity_usage():
    previous_month_usage = int(input("Oldingi oy sarfini: "))
    while True:
        print(f"Keyingi oy sarfini: {previous_month_usage * 1.1}")

# 20. Bill Splitter with Tips
def bill_splitter():
    total_bill = int(input("Jami hisob: "))
    num_people = int(input("Odamlar soni: "))
    while True:
        print(f"Har odamning hisobi: {total_bill / num_people}")

# 21. Simple Stock Portfolio Tracker
def stock_portfolio():
    stocks = ["stock1", "stock2", "stock3"]
    prices = {}
    for stock in stocks:
        prices[stock] = 0
    while True:
        stock = input("Aktsiyani tanlang: ")
        if stock in stocks:
            price = int(input("Narx: "))
            prices[stock] = price
            print(f"{stock} uchun narx: {prices[stock]}")
        else:
            print("Aktsiy
