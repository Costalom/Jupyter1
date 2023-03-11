import requests
from bs4 import BeautifulSoup
from tkinter import *
import tkinter as tk

# Создаем окно верхнего уровня
window = Tk()
window.geometry("400x100")
window.title('Раздела примеров сайта библиотеки Seaborn')

# Добавление кнопки закрытия окна
btnClosePopup = tk.Button(window, text="Закрыть", bg='#990000', fg='white', font=('Helvetica', 10, 'bold'), command=window.destroy)
btnClosePopup.place(x=280, y=50, width=110, height=30)

# Парсим html данные 
url = "https://seaborn.pydata.org/examples/index.html"
response = requests.get(url)

# Отображаем html данные в читаемый вид
soup = BeautifulSoup(response.content, 'html.parser')
#~print(soup)
#~print(soup.prettify())

# Поиск необходимых данных 
lst = soup.find_all('p')

# Обработчик нажатия кнопки
def process_button():
    for item in lst:
        print(clean_item(str(item)))
        
    popup_window(lst)

    
# Функция удаления лишних элементов из списка
def clean_item(my_item):
    position = my_item.find('</p')
    return my_item[3:position]

#~print("")

# Запрос отображения списка
def popup_window(lst):
    window = tk.Toplevel()
    window.geometry("500x500")
    window.title("Результат")

    # Добавление окна вывода текста
    txtOutput = tk.Text(window, font=('Courier New', 10, 'bold'))
    txtOutput.place(x=15, y=115, width=470, height=300)

     # Сформировать строку с данными
    output_str = ""
    for item in lst:
        output_str += clean_item(str(item)) + "\n"

    # Вывод строки в окне
    txtOutput.insert(END, output_str)


# Создание кнопки
button = tk.Button(window, text="Парсинг данных", font=('Helvetica', 10, 'bold'), command=process_button)
button.place(x=10, y=50, width=110, height=30)

window.mainloop()
