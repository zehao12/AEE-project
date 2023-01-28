#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import messagebox

import ttkbootstrap as tkbs
from PIL import ImageTk, Image


class Change():
    global r, c
    global r1, c1

    def __init__(self):
        root = Tk()  # Create body window.
        root.title('Row and column transpose')  # Define the name of the form.
        root.geometry('700x500')  # Defining the initial size of the form.
        root.maxsize(1200, 1200)  # Setting the maximum size the window can display.
        label1 = Label(root, text="Input the number of rows and columns for matrix 1:", bg='Aquamarine')
        label1.grid(row=0, column=0)  # side,bg,fg,width=20,height=20,justify="right"，font=("微软雅黑",20)
        E_var1 = StringVar()
        entry1 = Entry(root, textvariable=E_var1)
        entry1.grid(row=0, column=1)

        def Getcr():
            global r, c
            r, c = map(int, E_var1.get().split())
            text1.insert(END, f'Number of input rows{r}，Number of input columns{c}。\n')

        button1 = Button(root, text="Ensure", bg='Aquamarine', command=Getcr)
        button1.grid(row=0, column=2)
        label2 = Label(root, text="Input the content of matrix 1:", bg='Aquamarine')
        label2.grid(row=1, column=0)  # side,bg,fg,width=20,height=20,justify="right"，font=("微软雅黑",20)
        E_var2 = StringVar()
        entry2 = Entry(root, textvariable=E_var2)
        entry2.grid(row=1, column=1)

        def change():
            global r, c
            excel = E_var2.get()
            text1.insert(END, 'Input matrix:\n')
            excel = excel.split()
            excel = [excel[i:i + c] for i in range(0, len(excel), c)]
            for i in range(r):
                for j in range(c):
                    text1.insert(END, excel[i][j] + ' ')
                text1.insert(END, '\n')
            New_excel = [['' for j in range(0, r)] for i in range(0, c)]
            text1.insert(END, 'Transpose matrix format 1:\n')
            for i in range(c):
                for j in range(r):
                    New_excel[i][j] = excel[j][i]
                    text1.insert(END, New_excel[i][j] + ' ')
                text1.insert(END, '\n')
            New_excel = [j for i in New_excel for j in i]
            New_excel = ' '.join(New_excel)
            text1.insert(END, 'Transpose matrix format 2:' + '\n' + New_excel + '\n')

        button2 = Button(root, text="Row and column transpose", bg='Aquamarine', command=change)
        button2.grid(row=1, column=2)
        label3 = Label(root, text="Input the number of rows and columns for matrix 2:", bg='Aquamarine')
        label3.grid(row=2, column=0)  # side,bg,fg,width=20,height=20,justify="right"，font=("微软雅黑",20)
        E_var3 = StringVar()
        entry3 = Entry(root, textvariable=E_var3)
        entry3.grid(row=2, column=1)

        def Getcr1():
            global r1, c1
            r1, c1 = map(int, E_var3.get().split())
            text1.insert(END, f'Number of input rows{r1}，Number of input columns{c1}。\n')

        button3 = Button(root, text="Ensure", bg='Aquamarine', command=Getcr1)
        button3.grid(row=2, column=2)
        label4 = Label(root, text="Input the content of matrix 2:", bg='Aquamarine')
        label4.grid(row=3, column=0)  # side,bg,fg,width=20,height=20,justify="right"，font=("微软雅黑",20)
        E_var4 = StringVar()
        entry4 = Entry(root, textvariable=E_var4)
        entry4.grid(row=3, column=1)

        def count1():
            global r, c, r1, c1
            excel = E_var2.get()
            text1.insert(END, 'Input matrix 1:\n')
            excel = excel.split()
            excel = [excel[i:i + c] for i in range(0, len(excel), c)]
            for i in range(r):
                for j in range(c):
                    text1.insert(END, excel[i][j] + ' ')
                text1.insert(END, '\n')
            excel1 = E_var4.get()
            text1.insert(END, 'Input matrix 2:\n')
            excel1 = excel1.split()
            excel1 = [excel1[i:i + c] for i in range(0, len(excel1), c)]
            for i in range(r1):
                for j in range(c1):
                    text1.insert(END, excel1[i][j] + ' ')
                text1.insert(END, '\n')
            sum_excel = [[str((int(excel[i][j]) + int(excel1[i][j]))) for j in range(c)] for i in range(r)]
            text1.insert(END, 'Result of matrix addition：:\n')
            for i in range(r):
                for j in range(c):
                    text1.insert(END, sum_excel[i][j] + ' ')
                text1.insert(END, '\n')

        def count2():
            global r, c, r1, c1
            excel = E_var2.get()
            text1.insert(END, 'Input matrix 1:\n')
            excel = excel.split()
            excel = [excel[i:i + c] for i in range(0, len(excel), c)]
            for i in range(r):
                for j in range(c):
                    text1.insert(END, excel[i][j] + ' ')
                text1.insert(END, '\n')
            excel1 = E_var4.get()
            text1.insert(END, 'Input matrix 2:\n')
            excel1 = excel1.split()
            excel1 = [excel1[i:i + c1] for i in range(0, len(excel1), c1)]
            for i in range(r1):
                for j in range(c1):
                    text1.insert(END, excel1[i][j] + ' ')
                text1.insert(END, '\n')
            mul_excel = [[0 for j in range(c1)] for i in range(r)]
            for i in range(r):
                for j in range(c1):
                    for k in range(c):
                        mul_excel[i][j] += int(excel[i][k]) * int(excel1[k][j])
            text1.insert(END, 'Result of matrix multiplication：:\n')
            for i in range(r):
                for j in range(c1):
                    text1.insert(END, str(mul_excel[i][j]) + ' ')
                text1.insert(END, '\n')

        button5 = Button(root, text="Matrix addition", bg='Aquamarine', command=count1)
        button5.grid(row=3, column=2)
        button6 = Button(root, text="Matrix multiplication", bg='Aquamarine', command=count2)
        button6.grid(row=3, column=3)
        text1 = Text(root, state="normal", width=80, heigh=40)
        text1.grid(row=4, columnspan=10)
        root.mainloop()

# Help documentation.
def help():
    helpText = Toplevel(root)
    helpText.geometry(f"{Width}x{Height}")
    helpS = """
    Input form of matrix:

    Enter a line of characters with ; separate, representing rows of the matrix.
    Each row is separated by a space to represent the columns of the matrix.

    
    For example:
    1 2 3 ; 4 5 6;7 8 9
    Represented by the following matrix:
    [1 2 3
    4 5 6
    7 8 9]
    
    This matrix calculator can calculate:
    1 Matrix addation
    2 Matrix multiplication
    3 Matrix dot product
    4 Inverse of matrix
    The output is presented as matrix
    
    Please do not use Chinese semicolons, please use all English or numbers in the text box.

    """

    L = Label(helpText, text=helpS, font=font_sty_Zh)
    L.grid(row=0, column=0)


# Matrix addition
def add():
    text.config(state=NORMAL)
    text.delete(0.0, END)
    Astr = Mat1.get()
    Bstr = Mat2.get()
    try:
        while 1:
            try:
                if Astr.rindex(';') == len(Astr) - 1:
                    Astr = Astr[:-1]
                else:
                    break
            except:
                break
        Astr = Astr.split(';')
        Bstr = Bstr.split(';')
        A = list(map(lambda x: list(map(lambda t: int(t), x.split())), Astr))
        B = list(map(lambda x: list(map(lambda t: int(t), x.split())), Bstr))
    except:
        messagebox.showinfo('Warning', 'Matrix parsing error, please enter as formatted')
    C = list(map(lambda x, y: list(map(lambda a, b: a + b, x, y)), A, B))

    strA = "Matrix A is:\n"
    for it in A:
        for item in it:
            strA += str(item) + " "
        strA += "\n"
    strB = "Matrix B is:\n"
    for it in B:
        for item in it:
            strB += str(item) + " "
        strB += "\n"
    strC = "Matrix C is:\n"
    for it in C:
        for item in it:
            strC += str(item) + " "
        strC += "\n"
    text.insert(0.0, strA)
    text.insert(END, strB)
    text.insert(END, strC)
    # Change the state of the text box, set it to read-only.
    text.config(state=DISABLED)

# Matrix multiplication，using lists and loops.
def mul():
    text.config(state=NORMAL)
    text.delete(0.0, END)
    Astr = Mat1.get()
    Bstr = Mat2.get()
    try:
        while 1:
            try:
                if Astr.rindex(';') == len(Astr) - 1:
                    Astr = Astr[:-1]
                else:
                    break
            except:
                break
        Astr = Astr.split(';')
        Bstr = Bstr.split(';')
        A = list(map(lambda x: list(map(lambda t: int(t), x.split())), Astr))
        B = list(map(lambda x: list(map(lambda t: int(t), x.split())), Bstr))
    except:
        messagebox.showinfo('Warning', 'Matrix parsing error, please enter as formatted')
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                C[i][j] += A[i][k] * B[k][j]

    strA = "Matrix A is:\n"
    for it in A:
        for item in it:
            strA += str(item) + " "
        strA += "\n"
    strB = "Matrix B is:\n"
    for it in B:
        for item in it:
            strB += str(item) + " "
        strB += "\n"
    strC = "Matrix C is:\n"
    for it in C:
        for item in it:
            strC += str(item) + " "
        strC += "\n"
    text.insert(0.0, strA)
    text.insert(END, strB)
    text.insert(END, strC)
    # Change the state of the text box, set it to read-only.
    text.config(state=DISABLED)

# Matrix dot product
def dot():
    text.config(state=NORMAL)
    text.delete(0.0, END)
    Astr = Mat1.get()
    Bstr = Mat2.get()
    try:
        while 1:
            try:
                if Astr.rindex(';') == len(Astr) - 1:
                    Astr = Astr[:-1]
                else:
                    break
            except:
                break
        Astr = Astr.split(';')
        Bstr = Bstr.split(';')
        A = list(map(lambda x: list(map(lambda t: int(t), x.split())), Astr))
        B = list(map(lambda x: list(map(lambda t: int(t), x.split())), Bstr))
    except:
        messagebox.showinfo('Warning', 'Matrix parsing error, please enter as formatted')
    C = list(map(lambda x, y: list(map(lambda a, b: a * b, x, y)), A, B))

    strA = "Matrix A is:\n"
    for it in A:
        for item in it:
            strA += str(item) + " "
        strA += "\n"
    strB = "Matrix B is:\n"
    for it in B:
        for item in it:
            strB += str(item) + " "
        strB += "\n"
    strC = "Matrix C is:\n"
    for it in C:
        for item in it:
            strC += str(item) + " "
        strC += "\n"
    text.insert(0.0, strA)
    text.insert(END, strB)
    text.insert(END, strC)
    # Change the state of the text box, set it to read-only.
    text.config(state=DISABLED)

# Getting the comatrix of the matrix
def submatrix(A, i, j):
    # The comatrix of the entries in row i and column j of matrix A.
    m, n = len(A), len(A[0])
    C = [[A[x][y] for y in range(n) if y != j] for x in range(m) if x != i]  # List derivation.
    return C

# Getting the determinant of the matrix.
def detofmatrix(A):
    m = len(A)  # Number of matrix rows.
    n = len(A[0])  # Number of matrix columns.
    if (m == 1 and n == 1):
        return A[0][0]
    else:
        value = 0
        for j in range(n):
            value += ((-1) ** (j + 2)) * A[0][j] * detofmatrix(submatrix(A, 0, j))
        return value

# Numerically handles the inverse of a matrix.
def Ni(A):
    m = len(A)  # Number of matrix rows.
    n = len(A[0])  # Number of matrix columns.
    C = [[0] * n for _ in range(m)]
    d = detofmatrix(A)
    for i in range(m):
        for j in range(n):
            C[i][j] = ((-1) ** (i + j + 2)) * detofmatrix(submatrix(A, j, i))
            C[i][j] = C[i][j] / d
    return C

# The realization of matrix inverse method in GUI interface.
def getNi():
    text.config(state=NORMAL)
    text.delete(0.0, END)
    Astr = Mat1.get()
    Bstr = Mat2.get()
    try:
        while 1:
            try:
                if Astr.rindex(';') == len(Astr) - 1:
                    Astr = Astr[:-1]
                else:
                    break
            except:
                break
        Astr = Astr.split(';')
        Bstr = Bstr.split(';')
        A = list(map(lambda x: list(map(lambda t: int(t), x.split())), Astr))
        B = list(map(lambda x: list(map(lambda t: int(t), x.split())), Bstr))
    except:
        messagebox.showinfo('Warning', 'Matrix parsing error, please enter as formatted')
    strA = "Matrix A is:\n"
    for it in A:
        for item in it:
            strA += str(item) + " "
        strA += "\n"
    strC = "Inverse of matrix A is:\n"
    C = Ni(A)
    for it in C:
        for item in it:
            strC += str(item) + " "
        strC += "\n"
    text.insert(0.0, strA)
    text.insert(END, strC)
    text.config(state=DISABLED)
    pass


if __name__ == '__main__':
    def getImage(imgpath, width, height):
        img = Image.open(imgpath)
        img.resize((width, height))
        return ImageTk.PhotoImage(img)
    # Set global font properties.
    font_title_Zh = ("幼圆", 23)
    font_title_En = ("Consolas", 20)
    font_sty_Zh = ("楷体", 16)
    font_sty_Zh2 = ("楷体", 10)
    # Style the GUI interface to get an instantiation window instead of TK().
    style = tkbs.Style(theme='sandstone')
    root = style.master  # Instantiate TK.
    # Get the maximum screen size and lay the foundation for setting relative positions later.
    screenSize = root.maxsize()
    Width, Height, rows = 600, 500, 10
    root.geometry(f"{Width}x{Height}+{screenSize[0] // 2 - 250}+{screenSize[1] // 2 - 200}")
    # Sets whether to stretch the x - and Y-axis window size.
    root.resizable(1, 1)
    root.title("Matrix Calculator")
    
    canvas = Canvas(root, width=Width, height=Height, bd=0, highlightcolor="red", highlightthickness=1)
    canvas.grid(row=1, column=1)

    title = Label(root, text='Matrix Calculator', font=font_title_Zh, height=2)
    canvas.create_window(Width / 2, Height / rows * 1, window=title)
    # Match interface components, headings, input fields, buttons, etc.
    L1 = Label(root, text='Input matrix A', font=font_sty_Zh)
    L2 = Label(root, text='Input matrix B', font=font_sty_Zh)
    canvas.create_window(Width / 4 + 20, Height / rows * 3, window=L1)
    canvas.create_window(Width / 4 + 20, Height / rows * 4, window=L2)
    Mat1 = StringVar()
    Mat2 = StringVar()
    E1 = Entry(root, textvariable=Mat1, font=font_sty_Zh, bg='Ivory')
    E2 = Entry(root, textvariable=Mat2, font=font_sty_Zh, bg='Ivory')
    canvas.create_window(Width / 4 * 3 - 20, Height / rows * 3, window=E1)
    canvas.create_window(Width / 4 * 3 - 20, Height / rows * 4, window=E2)

    B1 = Button(root, text='Matrix addition', font=font_sty_Zh, command=add)
    B2 = Button(root, text='Matrix multiplication', font=font_sty_Zh, command=mul)
    B3 = Button(root, text='Matrix dot product', font=font_sty_Zh, command=dot)
    B4 = Button(root, text='Inverse of matrix', font=font_sty_Zh, command=getNi)
    B5 = Button(root, text='Help documentation', font=font_sty_Zh, command=help)

    canvas.create_window(Width / 4 + 20, Height / rows * 5 + 20, window=B1)
    canvas.create_window(Width / 4 + 20, Height / rows * 6 + 20, window=B2)
    canvas.create_window(Width / 4 + 20, Height / rows * 7 + 20, window=B3)
    canvas.create_window(Width / 4 + 20, Height / rows * 8 + 20, window=B4)
    canvas.create_window(Width / 4 + 20, Height / rows * 9 + 20, window=B5)

    text = Text(canvas, width=int((Width / 3 + 20) / font_sty_Zh2[1]),
                height=int((Height / rows * 3 - 20) / font_sty_Zh2[1]), font=font_sty_Zh2)
    canvas.create_window(Width / 4 * 3 - 20, Height / rows * 7, window=text)

    root.mainloop()


# In[ ]:




