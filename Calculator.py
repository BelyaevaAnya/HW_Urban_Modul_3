import tkinter as tk
num1, num2 = 0, 0
def set_global_params():
    global num1, num2
    num1 = int(number1_entery.get())
    num2 = int(number2_entery.get())
    answer.delete(0, 'end')
def add():
    set_global_params()
    res = num1 + num2
    answer.insert(0, res)

def mult():
    set_global_params()
    res = num1 * num2
    answer.insert(0, res)

def minus():
    set_global_params()
    res = num1 - num2
    answer.insert(0, res)
def div():
    set_global_params()
    res = num1 * num2
    answer.insert(0, res)

window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x350")
window.resizable(False, False)
button_add = tk.Button(window, text = '+', width= 5, height=5, command = add)
button_add.place(x=20, y=120)
button_minus = tk.Button(window, text = '-', width= 5, height=5, command = minus)
button_minus.place(x=70, y=120)
button_mult = tk.Button(window, text = 'x', width= 5, height=5, command= mult)
button_mult.place(x=120, y=120)
button_div = tk.Button(window, text = '/', width= 5, height=5, command= div)
button_div.place(x=170, y=120)
number1_entery = tk.Entry(window, width= 50)
number1_entery.place(x = 20, y = 40)
number2_entery = tk.Entry(window, width= 50)
number2_entery.place(x = 20, y = 90)
answer = tk.Entry(window, width= 50)
answer.place(x = 20, y = 240)
number1 = tk.Label(window, text='Введите первое число:')
number1.place(x = 20, y = 15)
number2 = tk.Label(window, text='Введите второе число:')
number2.place(x = 20, y = 60)
number3 = tk.Label(window, text='Ответ:')
number3.place(x = 20, y = 210)
window.mainloop()

