from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
root = Tk()
root.title("Блокнот стажёра - Миронова Руслана")
root.geometry("600x700")

main_menu=Menu(root)



#функция для словариков на темы
def chenge_theme(theme):
    text_fild['bg']=view_colors[theme]['text_bg']
    text_fild['fg']=view_colors[theme]['text_fg']
    text_fild['insertbackground']=view_colors[theme]['coursor']
    text_fild['selectbackground']=view_colors[theme]['select_bg']
#функция для словариков на шрифты
def chenge_fonts(fonts_in_def):
    text_fild['font']=fonts[fonts_in_def]['font']

#функция для выхода
def notepad_exit():
    answer = messagebox.askokcancel('Выход','Вы точно хотите выйти?')
    if answer:
        root.destroy()
#функция для открытия файла
def open_file():
    file_path=filedialog.askopenfilename(title='Выбор файла',filetypes=(('текстовые документы (*.txt)','*.txt'),('Все файлы','*.*')))
    if file_path:
        text_fild.delete('1.0',END)
        text_fild.insert('1.0',open(file_path,encoding='utf-8').read())
#функция для сохранить
def save_file():
    file_path=filedialog.asksaveasfilename(filetypes=(('текстовые документы (*.txt)','*.txt'),('Все файлы','*.*')))
    f=open(file_path,'w',encoding='utf-8')
    text = text_fild.get('1.0',END)
    f.write(text)
    f.close()
#фаил
file_menu=Menu(main_menu,tearoff=0)
file_menu.add_command(label='Открыть',command=open_file)
file_menu.add_command(label='Сохранить',command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Закрыть',command=notepad_exit)

root.config(menu=file_menu)


#вид
view_menu=Menu(main_menu,tearoff=0)
#здесь будут меняться темы и шрифт
view_menu_sub=Menu(view_menu,tearoff=0)
font_menu_sub=Menu(view_menu,tearoff=0)
view_menu_sub.add_command(label="Тёмная",command=lambda:chenge_theme('dark'))#через лямбда - функцию подключаем функцию со связанной темой из словарика
view_menu_sub.add_command(label="Светлая",command=lambda:chenge_theme('light'))
view_menu.add_cascade(label='Тема',menu=view_menu_sub)

####
font_menu_sub.add_command(label='Arial',command=lambda:chenge_fonts('Arial'))
font_menu_sub.add_command(label='Comic Sans MS',command=lambda:chenge_fonts('CSMS'))
font_menu_sub.add_command(label='Times New Roman',command=lambda:chenge_fonts('TNR'))
view_menu.add_cascade(label='Шрифт',menu=font_menu_sub)
root.config(menu=view_menu)



#Добавление списков меню
main_menu.add_cascade(label='файл',menu=file_menu)
main_menu.add_cascade(label='Вид',menu=view_menu)

root.config(menu=main_menu)#экземплятор меню присваиваем к опции меню через имя экземплятора

f_text=Frame(root)
f_text.pack(fill=BOTH,expand=1)
#словарик во вьюшке
view_colors ={
    'dark':{
        'text_bg':'black','text_fg':'lime','coursor':'brown','select_bg':"#8D917A"
    },
    'light':{
        'text_bg':'white','text_fg':'black','coursor':'#A5A5A5','select_bg':"#FAEEDD"
    }
}

fonts ={
    'Arial':{
        'font': 'Arial 11 bold'
    },
    'CSMS':{#его кортежем подадим
        'font': ('Comic Sans MS',14,'bold')
    },
    'TNR':{
        'font': ('Times New Roman',14,'bold')
    }
}#осталось добавить функции (или методы) смотри сверху
text_fild=Text(f_text,
               bg='black',#тёмная тема
               fg='lime',
               padx=10,#отступы от краёв окна
               pady=10,
               wrap=WORD,#перенос строк
               insertbackground="brown",#курсор
               selectbackground="#8D917A",#выделение текста
               spacing3=10,#абзац
               width=30,
               font='Arial 11 bold')#ширина текста (под скролбар настраивал)
text_fild.pack(fill=BOTH,expand=1,side=LEFT)


scroll=Scrollbar(f_text,command=text_fild.yview)#скролбар с готовым методом 
scroll.pack(side=LEFT,fill=Y)#
text_fild.config(yscrollcommand=scroll.set)#Если не видно - расширь блокнот, когда откроешь

root.mainloop()
