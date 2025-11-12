"""TO-DO List dasturi - Tkinter va JSON bilan. CHATGPT tomonidan yaratilgan."""

# import tkinter as tk
# from tkinter import messagebox
# import json
# import os

# # Fayl nomi
# FILE_NAME = "tasks.json"

# # Fayldan vazifalarni yuklash
# def load_tasks():
#     if os.path.exists(FILE_NAME):
#         with open(FILE_NAME, "r") as file:
#             return json.load(file)
#     return []

# # Vazifalarni faylga saqlash
# def save_tasks():
#     with open(FILE_NAME, "w") as file:
#         json.dump(tasks, file, indent=4)

# # Vazifa qo'shish
# def add_task():
#     task_text = entry.get().strip()
#     if task_text:
#         tasks.append({"task": task_text, "done": False})
#         save_tasks()
#         update_listbox()
#         entry.delete(0, tk.END)
#     else:
#         messagebox.showwarning("Xato", "Iltimos, vazifa kiriting!")

# # Vazifani o‘chirish
# def delete_task():
#     try:
#         selected = listbox.curselection()[0]
#         del tasks[selected]
#         save_tasks()
#         update_listbox()
#     except IndexError:
#         messagebox.showwarning("Xato", "Iltimos, o‘chirish uchun vazifani tanlang!")

# # Vazifani “bajarildi” deb belgilash
# def mark_done():
#     try:
#         selected = listbox.curselection()[0]
#         tasks[selected]["done"] = not tasks[selected]["done"]
#         save_tasks()
#         update_listbox()
#     except IndexError:
#         messagebox.showwarning("Xato", "Iltimos, bajarilgan vazifani tanlang!")

# # Vazifalar ro‘yxatini yangilash
# def update_listbox():
#     listbox.delete(0, tk.END)
#     for task in tasks:
#         status = "✅" if task["done"] else "❌"
#         listbox.insert(tk.END, f"{task['task']} {status}")

# # Oynani yopishda saqlash
# def on_close():
#     save_tasks()
#     root.destroy()

# # Asosiy oyna
# root = tk.Tk()
# root.title("📝 Vazifalar ro‘yxati")
# root.geometry("400x450")
# root.resizable(False, False)
# root.configure(bg="#eaf4f4")

# # Vazifalar yuklash
# tasks = load_tasks()

# # Kirish maydoni
# entry = tk.Entry(root, font=("Arial", 14))
# entry.pack(pady=10, padx=10, fill=tk.X)

# # Tugmalar
# button_frame = tk.Frame(root, bg="#eaf4f4")
# button_frame.pack(pady=5)

# tk.Button(button_frame, text="➕ Qo‘shish", command=add_task, width=12, bg="#b3e6b3").grid(row=0, column=0, padx=5)
# tk.Button(button_frame, text="✅ Bajarildi", command=mark_done, width=12, bg="#c2d6f0").grid(row=0, column=1, padx=5)
# tk.Button(button_frame, text="🗑️ O‘chirish", command=delete_task, width=12, bg="#f2b3b3").grid(row=0, column=2, padx=5)

# # Vazifalar ro‘yxati
# listbox = tk.Listbox(root, font=("Arial", 13), height=15, selectbackground="#b3d9ff")
# listbox.pack(padx=10, pady=10, fill=tk.BOTH)

# # Vazifalarni yangilash
# update_listbox()

# # Dastur yopilganda faylni saqlash
# root.protocol("WM_DELETE_WINDOW", on_close)

# # Dastur ishga tushirish
# root.mainloop()



"""TO-DO List dasturi - Tkinter va JSON bilan. O'zim yozgan dasturim."""

# print("=" * 50)
# print("                     TO DO LIST DASTURIGA XUSH KELIBSIZ                    ")
# print("=" * 50)
# import time as t
# tasks = []

# while True:
#     t.sleep(1)
#     print("\nQuyidagilardan birini tanlang:\n1. Vazifa qo'shish.\n2. Vazifani o'chirish.\n3. Vazifalarni ko'rish.\n4. Vazifani 'bajarildi' deb belgilash.\n5. Chiqish.")
#     try:
#         choice = int(input("Tanlovingiz (1-5): "))
#     except ValueError:
#         print("Iltimos raqam kiriting")
#         continue
#     if choice == 5:
#         break


#     elif choice == 1:
#         added_task = input("Vazifangizni kiriting: ")
#         if added_task:
#             tasks.append({'task': added_task, 'done': False})
#         else:
#             print("Vazifa kiriting.")
#         t.sleep(1)
#         print(f"{added_task} vazifasi ro'yxatingizda.")


#     elif choice == 2:
#         if tasks:
#             print("Vazifalaringiz:")
#             t.sleep(1)
#             state = ''
#             for num, task in enumerate(tasks,1):
#                 if task['done']:
#                     state = '✅'
#                 else:
#                     state = '❌'
#                 print(f"{num}. {task['task']} {state}.")
#                 t.sleep(1)
#             try:
#                 removed_task = int(input("O'chirmoqchi bo'lgan vazifangizni raqamnini kiriting: "))
#             except ValueError:
#                 print("Iltimos raqam kiriting.")
#                 continue
#             if 1 <= removed_task <= len(tasks):
#                 tasks.remove(tasks[removed_task -1])
#                 t.sleep(1)
#                 print("Vazifa o'chirildi")
#             else:
#                 print("Noto'g'ri raqam kiritldi.")
#         else:
#             print("Avval vazifa kiriting.")


#     elif choice == 3:
#         if not tasks:
#             t.sleep(1)
#             print("Afsuski ro'yxatingiz bo'sh")
#         else:
#             t.sleep(1)
#             print("Vazifalaringiz:")
#             state = ''
#             for num, mission in enumerate(tasks,1):
#                 if mission['done']:
#                     state = '✅'
#                 else:
#                     state = '❌'
#                 print(f"{num}. {mission['task']} {state}.")


#     elif choice == 4:
#         if not tasks:
#             print("Iltimos avval vazifa kiriting.")
#         else:
#             print("Vazifalaringiz:")
#             t.sleep(1)
#             state = ''
#             for num, mission in enumerate(tasks,1):
#                 if mission['done']:
#                     state = '✅'
#                 else:   
#                     state = '❌'                
#                 print(f"{num}. {mission['task']} {state}.")
#             try:
#                 done_task = int(input("Bajarildi deb belgilamoqchi bo'lgan vazifangizni raqamnini kiriting: "))     
#             except ValueError:
#                 print("Iltimos raqam kiriting.")
#                 continue
#             if 1 <= done_task <= len(tasks):
#                 tasks[done_task - 1]['done'] = True
#                 t.sleep(1)
#                 print(f"{tasks[done_task - 1]['task']} vazifasi 'Bajarildi ✅' deb belgilandi.")
#     else:
#         print("Noto'g'ri buyruqni tanladingiz. Iltimos qayta urinib ko'ring.")
# print("Dasturdan foydalanganingiz uchun rahmat! Yana ko'rishguncha!")


"""QR-kod yaratish dasturi"""

# import qrcode
# txt = input("QR code matni yoki URL manzilni kiriting: ").strip()
# filename = input("Saqlash uchun fayl nomini kiriting: ").strip()
# qr = qrcode.QRCode(box_size=10, border=5)
# qr.add_data(txt)
# image = qr.make_image(fill='black', back_color='white')
# image.save(f"{filename}.png")
# print(f"{filename}.png faylga QR codingiz saqlandi.")


""""Valyuta konvertori dasturi"""
# qiymat,valyutasi = map(str, (input("O'zgartirmoqchi bo'lgan summa va uning valyutasini kiriting (masalan: 10000 USD): ").split()))
# change_to = input("Qaysi valyutaga o'zgartirmoqchisiz (USD,EUR,RUBL,SUM): ")
# try:
#     # USD kursi
#     qiymat = float(qiymat)
#     if valyutasi.upper() == 'USD':
#         if change_to.upper() == 'EUR':
#             print(f"{qiymat} USD = {qiymat * 0.93} USD")
#         elif change_to.lower() == 'rubl':
#             print(f"{qiymat} = {qiymat * 80.74} RUBL")
#         elif change_to.lower() == 'sum':
#             print(f"{qiymat} USD = {qiymat * 11350} SUM")
#         elif change_to.lower() == 'usd':
#             print(f"{qiymat} USD = {qiymat} USD")
#         else:
#             print("Afsuski bizda bunday valyuta kursi yo'q.")
#     # / USD kursi

#     # RUBL kursi
#     elif valyutasi.lower() == 'rubl':
#         if change_to.lower() == 'usd':
#             print(f"{qiymat} = {qiymat * 0.012} USD")
#         elif change_to.lower() == 'eur':
#             print(f"{qiymat} RUBL = {qiymat * 0.011} EUR")
#         elif change_to.lower() == 'sum':
#             print(f"{qiymat} RUBL = {qiymat * 150} SUM")
#         elif change_to.lower() == 'rubl':
#             print(f"{qiymat} RUBL = {qiymat} RUBL")
#         else:
#             print("Afsuski bzda bunday valyuta kursi yo'q.")
#     # / RUBL kursi

#     #  EUR kursi
#     elif valyutasi.lower() == 'eur':
#         if change_to.lower() == 'usd':
#             print(f"{qiymat} EUR = {qiymat * 1.08}")
#         elif change_to.lower() == 'sum':
#             print(f"{qiymat} EUR = {qiymat * 12150} SUM")
#         elif change_to.lower() == 'rubl':
#             print(f"{qiymat} EUR = {qiymat * 87.14} RUBL")
#         elif change_to.lower() == 'usd':
#             print(f"{qiymat} EUR = {qiymat} EUR")
#         else:
#             print("Afsuski bizda bunday valyuta kursi mavjud emas.")
#     # / EUR kursi

#     # SUM kursi
#     elif valyutasi.lower() == 'sum':
#         if change_to.lower() == 'rubl':
#             print(f"{qiymat} SUM = {qiymat * 0.0067} RUBL")
#         elif change_to.lower() == 'eur':
#             print(f"{qiymat} SUM = {qiymat * 0.000082} EUR")
#         elif change_to.lower() == 'usd':
#             print(f"{qiymat} SUM = {qiymat * 0.000088} USD")
#         elif change_to.lower() == 'sum':
#             print(f"{qiymat} SUM = {qiymat} SUM")
#         else:
#             print("Afsuski bizda bunday valyuta kursimavjud emas")
#         # / SUM kursi
# except Exception as e:
#     print("Afsuski xato topildi: ", e)


"""Kalkulyator"""

# print("=" * 150)
# print("                                                         Kalkulyator                                                 ")
# print("=" * 150)
# while True:
#     a = int(input("1-son: "))
#     b = int(input("2-son: "))
#     amal = input("Amal('+','-','*','/'): ")
#     if amal == '+':
#         print(a + b)
#         break
#     elif amal == '-':
#         print(a - b)
#         break
#     elif amal == '*':
#         print(a * b)
#         break
#     elif amal == '/':
#         try:
#             javob = a / b
#             print(a / b)
#             break
#         except ZeroDivisionError:
#             print("❌ Sonni nolga bo'lib bo'lmaydi.")
#             continue
#     else:
#         print(f"{amal} amali mavjud emas. Tanlovlar: ('+','-','*','/')")
#         continue


"""Son topish o'yini"""

# import random as r
# import time as t
# numbers = list(range(21))
# guessed_number = r.choice(numbers)
# print("=" * 150)
# print("                                                             Son topish o'yiniga xush kelibsiz.                                           ")
# print("=" * 150)
# input("O'yinni boshlash uchun istalgan tugmani bosing.")
# print("Men 20 gacha son o'ylayapman. Siz topasiz. O'ylayapman....")
# t.sleep(5)
# print("O'yladim.")
# sana = 0
# while True:
#     sana += 1
#     user_guess = int(input("Taxminigiz: "))
#     if user_guess <= 20 and user_guess >= 0:
#         if user_guess == guessed_number:
#             print(f"Siz men o'ylagan sonni {sana} ta urinishda topdingiz.")
#             break
#         else:
#             if user_guess > guessed_number:
#                 print(f"Men o'ylagan son {user_guess} dan kichikroq.")
#             else:
#                 print(f"Men o'ylagan son {user_guess} dan kattaroq.")
#     else:
#         print("Siz belgilangan chegaradan o'tdingiz. Iltimos mos son kiriting.")
#         continue


"""Foydalanuvchiga joriy vaqtni ko'rsatuvchi dastur"""

# input("Joruy vaqtni ko'rish uchun istalgan tugmani bosing: ")
# import datetime as dt
# time = dt.datetime.now()
# print(f"Joriy vaqt: {time.hour}:{time.minute}:{time.second} ")
# date = dt.date.today()
# print(f"Joriy sana: {date.year}-{date.month}-{date.day}")


"""Matnni tahlil qiluvchi dastur"""

# user_txt = input("Matn kiriting: ")
# sozlar_soni = len(user_txt.split())
# harflar_soni = len(user_txt.replace(' ',''))
# matn = user_txt.split()
# uzunliklar = []
# for soz in matn:
#     uzunliklar.append(len(soz))
# print(f"Matndagi eng uzun so'z: {max(matn)} Eng kichik so'z: {min(matn)}")
# if '.' in user_txt or '!' in user_txt or '?' in user_txt:
#     gaplar_soni = user_txt.count('.') + user_txt.count('!') + user_txt.count('?')
#     print(f"Matnda {gaplar_soni} ta gap bor.")
# print(f"Matnda {sozlar_soni} ta so'z va {harflar_soni} ta harf bor.")

"""Word guess o'yini"""
"""Foydalanuvchi harf kiritadi va agar harf so'zda bo'lsa, u harfni ko'rsatadi. Foydalanuvchi so'zni to'g'ri topguncha davom etadi."""
# import random as r
# sozlar = ['python','hayot','kompyuter','noutbuk','dunyo','maktab','futbol','basketboll']
# word_guess = r.choice(sozlar)
# print("=" * 150)
# print("                                                         Word Guess O'yiniga Xush Kelibsiz!                                                ")
# print("=" * 150)
# print("Men bir so'z o'yladim. Siz harf kiritasiz va agar harf so'zda bo'lsa, u harfni ko'rsataman. So'zni to'g'ri topguncha davom eting.")
# hidden_word = '_' * len(word_guess)
# while True:
#     print(f"Men {hidden_word} so'zini o'yladim. Siz uni toping")
#     harflar = []
#     topilgan = []
#     take_letter = input("Harf kiriting: ").lower()
#     if len(take_letter) != 1 or not take_letter.isalpha():
#         print("Iltimos bitta harf kiriting.")
#         continue
#     harflar.append(take_letter)

#     if take_letter in harflar:
#         print(f"Siz avval {take_letter} harfini kiritgansiz. Boshqa harf kiriting.")
#         continue
#     if take_letter in word_guess:
#         print(f"Siz {take_letter} harfini topdingiz!")
#         for index, harflar in enumerate(word_guess): # index va harflar o'zgaruvchilariga word_guess dagi harflarni ajratib beradi
#             if take_letter == harflar: # agar foydalanuvchi kiritgan harf word_guess dagi harfga teng bo'lsa
#                 topilgan.append(index) # topilgan ro'yxatiga index qo'shadi
#         hidden_word = list(hidden_word)
#         for index in topilgan:
#             hidden_word[index] = take_letter
#         hidden_word = ''.join(hidden_word)
#         if hidden_word == word_guess:
#             print(f"Tabriklaymiz, Siz so'zni topdingiz. So'zimiz {word_guess} edi.")
#             break
#     else:
#         print(f"Uzr, {take_letter} harfi so'zda mavjud emas.")

        # hidden_word  = hidden_word.replace('_', take_letter)
        # if hidden_word == take_letter:
        #     print(f"Tabriklaymiz, Siz so'zni topdingiz. So'zimis {word_guess} edi.")
        #     break
        # else:
        #     print(f"Bunday harf mavjud emas. Qayta urinib ko'ring. Sizning shu paytgacha kiritgan harflaringiz: {harflar}.")



import time  # Import time
tasks = []

# 1. Upload task function

def upload_task():
        tim = time.ctime()
        new_task = input("Input a new task: ").strip()
        if new_task:
                tasks.append({'task':new_task,'done': False,'time': tim})
        else:
                print("Please, type any task")

# 2. Show tasks function

def show_tasks():
        if tasks:
                for num, work in enumerate(tasks,1):
                        state = ''
                        if work['done'] == False:
                                state = '❌'
                        else:
                                state = '✅'
                        print(f"{num}. {work['task']}. Time: {work['time']}. Is done: {state}")
        else:
                print("Your task list is empty.")

def remove_task():
        if not tasks:
                print("No tasks to remove. Adda a task before remove.")
        else:
                show_tasks()
                try:
                        removed_task = int(input("Input your task number you want to remove it."))
                except ValueError:
                        print("Please type a number.")
                        
                if 1 <= removed_task <=len (tasks):
                        tasks.remove(tasks[removed_task - 1])
                else:
                        print("Please, type a suit number")


def mark_task():
        if tasks:
                show_tasks()
                try:
                        marked_task = int(input("Type the number of task you will mark it: "))
                except:
                        print("Type a number")
                
                if 1 <= marked_task <= len(tasks):
                        state = tasks[marked_task - 1]
                        if state.get('done') is False:
                                state['done'] = True
                                print("Your task marked")
                        else:
                                print("You marked this task before")
                else:
                        print("Type a suitable number")
        else:
                print("Your tasks list is empty")

while True:
        print(f"\nChoose one choice.\n1. Add a task\n2. See the tasks\n3. Remove task\n4. Mark the task\n5. Exit")
        try:
                choice = int(input("Your choice is: "))
        except:
                print("Please type a number")
                continue
        if choice == 1:
                upload_task()
        elif choice == 2:
                show_tasks()
        elif choice == 3:
                remove_task()
        elif choice == 4:
                mark_task()
        elif choice == 5:
                break
        else:
                print("Unfortunately, there isn't such kind of choice.")
