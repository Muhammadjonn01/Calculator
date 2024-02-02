import tkinter
import math

def click(val):
    e = entry.get()
    ans = ' '
    try:
        if val == 'C':
            e = e[0:len(e) - 1]
            entry.delete(0, 'end')
            entry.insert(0, e)
            return
        elif val == 'CE':
            entry.delete(0, 'end')
        elif val == '√':
            ans = math.sqrt(eval(e))
        elif val == 'π':
            ans = math.pi
        elif val == 'cos0':
            ans = math.cos(math.radians(eval(e)))
        elif val == 'sin0':
            ans = math.sin(math.radians(eval(e)))
        elif val == 'tan0':
            ans = math.tan(math.radians(eval(e)))
        elif val == '2π':
            ans = 2 * math.pi
        elif val == 'cosh':
            ans = math.cosh(eval(e))
        elif val == 'sinh':
            ans = math.sinh(eval(e))
        elif val == 'tanh':
            ans = math.tanh(eval(e))
        elif val == chr(8731):
            ans = eval(e) ** (1/3)
        elif val == 'x\u02b8':
            entry.insert('end', '**')
            return
        elif val == 'x\u00B3':
            ans = eval(e) ** 3
        elif val == 'x\u00B2':
            ans = eval(e) ** 2
        elif val == 'ln':
            ans = math.log2(eval(e))
        elif val == 'deg':
            ans = math.degrees(eval(e))
        elif val == 'rad':
            ans = math.radians(eval(e))
        elif val == 'e':
            ans = math.e
        elif val == 'lag10':
            ans = math.log10(eval(e))
        elif val == 'x!':
            ans = math.factorial(eval(e))
        elif val == chr(247):
            entry.insert('end', '/')
            return
        elif val == '=':
            ans = eval(e)
        else:
            entry.insert('end', val)
            return
        entry.delete(0, 'end')
        entry.insert(0, ans)
    except SyntaxError:
        pass


root = tkinter.Tk()
root.title('Calculator')
root.geometry('680x486+100+100')
root.config(bg='black')

entry = tkinter.Entry(root, font=('arial', 20, 'bold'),
                      bg='black', fg='white', bd=10, width=30)
entry.grid(row=0, column=0, columnspan=8)

button_list = ['C', 'CE', '√', '+', 'π', 'cos0', 'tan0', 'sin0',
               '1', '2', '3', '-', '2π', 'cosh', 'tanh', 'sinh', '4', '5',
               '6', "*", chr(8731), 'x\u02b8', 'x\u00B3', 'x\u00B2', '7',
               '8', '9', chr(247), 'ln', 'deg', 'rad', 'e', '0', '.', '%',
               '=', 'log10', '(', ')', 'x!']
r = 1
c = 0

for i in button_list:
    button = tkinter.Button(root, width=5, height=2, bd=2, text=i,
                            bg='black', fg='white', font=('arial', 18, 'bold'),
                            command=lambda button=i: click(button))
    button.grid(row=r, column=c, pady=1)
    c += 1
    if c > 7:
        r += 1
        c = 0

root.mainloop()