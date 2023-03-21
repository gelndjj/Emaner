from tkinter import filedialog, ttk, messagebox
from tkinter import  *
import os, customtkinter, re

root = customtkinter.CTk()

root.geometry('700x500')
root.title('Emaner')
root.resizable(0,0)
customtkinter.set_appearance_mode("light")

def browse():
     global f

     f = filedialog.askdirectory()
     ls_box.delete(0,END)
     for file in os.listdir(f):
        if os.path.isfile(os.path.join(f,file)):
            ls_box.insert(END,f'{file}\n')

def clean_new_entry(event):
     new_entry.delete(0,END)

def clean_old_entry(event):
     old_entry.delete(0,END)

def clean_new_entry_re(event):
     new_entry_re.delete(0,END)

def clean_old_entry_re(event):
     old_entry_re.delete(0,END)

def rename_all_file():
    for file in os.listdir(f):
            current_full_path = f+'/'+file
            current_fname = os.path.basename(current_full_path)
            current_fname_withtout_ext = os.path.splitext(current_fname)[0]
            current_fname_ext = os.path.splitext(current_fname)[1]
            new_fname = current_fname_withtout_ext.replace(new_entry.get(),old_entry.get())
            new_full_path = f+'/'+new_fname+current_fname_ext
            final_fname = os.rename(current_full_path,new_full_path)
    ls_box.delete(0,END)
    for file in os.listdir(f):
        if os.path.isfile(os.path.join(f,file)):
            ls_box.insert(END,f'{file}\n')

def rename_all_file_re():
    number = 0
    pattern = new_entry_re.get()
    re_pattern = f'{pattern}'
    for file in os.listdir(f):
            current_full_path = f+'/'+file
            current_fname = os.path.basename(current_full_path)
            current_fname_withtout_ext = os.path.splitext(current_fname)[0]
            current_fname_ext = os.path.splitext(current_fname)[1]
            new_fname = re.sub(re_pattern,old_entry_re.get(),current_fname_withtout_ext)
            new_full_path = f+'/'+new_fname+' ('+str(number)+')'+current_fname_ext
            final = os.rename(current_full_path,new_full_path)
            number += 1
    ls_box.delete(0,END)
    for file in os.listdir(f):
        if os.path.isfile(os.path.join(f,file)):
            ls_box.insert(END,f'{file}\n')

def rollback():
    pattern = old_entry.get()
    for file in os.listdir(f):
            current_full_path = f+'/'+file
            current_fname = os.path.basename(current_full_path)
            current_fname_withtout_ext = os.path.splitext(current_fname)[0]
            current_fname_ext = os.path.splitext(current_fname)[1]
            new_fname = current_fname_withtout_ext.replace(pattern,new_entry.get())
            new_full_path = f+'/'+new_fname+current_fname_ext
            final_fname = os.rename(current_full_path,new_full_path)
    ls_box.delete(0,END)
    for file in os.listdir(f):
        if os.path.isfile(os.path.join(f,file)):
            ls_box.insert(END,f'{file}\n')

def show_ins():
     re_exp = Toplevel(root)
     re_exp.title('Regular Expressions Examples')
     re_exp.geometry('450x260')
     re_exp.resizable(0,0)

     re_exp_listbox = Listbox(re_exp,
                            width=45,
                            height=15,
                            borderwidth=1,
                            background='#e8e6e6')
     re_exp_listbox.pack()
     re_exp_listbox.insert(END,'. - Matches any single character except newline.\n',
                                '^ - Matches the start of a string.\n',
                                '$ - Matches the end of a string.\n',
                                '* - Matches zero or more occurrences of the previous character or group.\n',
                                '+ - Matches one or more occurrences of the previous character or group.\n',
                                '? - Matches zero or one occurrence of the previous character or group.\n',
                                '{n} - Matches exactly n occurrences of the previous character or group.\n',
                                '{n,} - Matches n or more occurrences of the previous character or group.\n',
                                '{n,m} - Matches at least n and at most m occurrences of the previous character or group.\n',
                                '[abc] - Matches any one of the characters a, b, or c.\n',
                                '[^abc] - Matches any character except a, b, or c.\n',
                                '| - Matches either the expression before or after the vertical bar.\n',
                                '\d - Matches any digit (0-9).\n',
                                '\D - Matches any character that is not a digit.\n',
                                '\w - Matches any word character (a-z, A-Z, 0-9, and underscore).\n',
                                '\W - Matches any character that is not a word character.\n',
                                '\s - Matches any whitespace character (space, tab, newline, etc.).\n',
                                '\S - Matches any non-whitespace character.')

#FRAMES
left_fr = customtkinter.CTkFrame(root,corner_radius=0,fg_color='#3A7FF6',width=300)
left_fr.pack(side=LEFT,fill=Y)
right_fr = customtkinter.CTkFrame(root,corner_radius=0, fg_color='White',width=400)
right_fr.pack(side=RIGHT,fill=Y)

#LABEL FRAME
frame1 = LabelFrame(right_fr, text='One',fg='#5c5b5b', bg='White',relief=GROOVE)
frame1.place(x=30,y=268)

#LABELS
title_lbl = customtkinter.CTkLabel(left_fr,
                                   text="Welcome to Emaner",
                                    fg_color="#3A7FF6",
                                    text_color='white',
                                    justify="left",
                                    font=("Arial-BoldMT", int(20.0)))
title_lbl.place(x=20.0, y=80.0)

text_lbl = customtkinter.CTkLabel(left_fr,
                                  text="Enamer renames your files \n"
                                        "according to your will.\n" 
                                        "Simply type the text\n"
                                        "you want to change and click\n"
                                        "on Rename.\n\n"
    
                                        "Regular Expression can be\n"
                                        "also used to rename.\n"
                                        "Click on the button below\n"
                                        "to see examples",
                                    fg_color="#3A7FF6",
                                    text_color='White',
                                    justify="left",
                                    font=("Georgia", int(15.0)))
text_lbl.place(x=20.0, y=160.0)

warning_lbl = customtkinter.CTkLabel(left_fr,
                                     text='BE CAREFUL renaming by using RE.\n'
                                     'BE SURE the file you are renaming won\'t have\n'
                                     'the same name than others.\n'
                                     'Otherwise, the file WILL BE DELETED.',
                                     fg_color='#3A7FF6',
                                     text_color='White',
                                     justify='center')
warning_lbl.place(x=20,y=420)

#ENTRY BOXES
new_entry = customtkinter.CTkEntry(right_fr,
                                      width=120,
                                      height=30,
                                      border_width=1,
                                      corner_radius=1,
                                      fg_color='#e8e6e6',
                                      border_color='Black',
                                      text_color='Black')
new_entry.place(x=30,y=315)
new_entry.insert(0,'New string')

new_entry_re = customtkinter.CTkEntry(right_fr,
                                      width=120,
                                      height=30,
                                      border_width=1,
                                      corner_radius=1,
                                      fg_color='#e8e6e6',
                                      border_color='Black',
                                      text_color='Black')
new_entry_re.place(x=30,y=423)
new_entry_re.insert(0,'New string RE')


old_entry = customtkinter.CTkEntry(right_fr,
                                   width=120,
                                   height=30,
                                   border_width=1,
                                   corner_radius=1,
                                   fg_color='#e8e6e6',
                                   border_color='Black',
                                   text_color='Black',
                                   )
old_entry.place(x=165,y=315)
old_entry.insert(0,'Old string')

old_entry_re = customtkinter.CTkEntry(right_fr,
                                   width=120,
                                   height=30,
                                   border_width=1,
                                   corner_radius=1,
                                   fg_color='#e8e6e6',
                                   border_color='Black',
                                   text_color='Black',
                                   )
old_entry_re.place(x=165,y=423)
old_entry_re.insert(0,'Old string RE')

#BUTTONS
btn_browse = customtkinter.CTkButton(right_fr,
                                     text='Browse Files',
                                     width=180,
                                     height=30,
                                     fg_color='#3A7FF6',
                                     text_color='White',
                                     border_color='Black',
                                     border_width=2,
                                     command=browse)
btn_browse.place(x=120,y=30)

btn_rename = customtkinter.CTkButton(right_fr,
                                     text='Rename',
                                     width=150,
                                     height=30,
                                     fg_color='#3A7FF6',
                                     text_color='White',
                                     border_color='Black',
                                     border_width=2,
                                     command=rename_all_file)
btn_rename.place(x=30,y=268)
btn_rename_re = customtkinter.CTkButton(right_fr,
                                     text='Rename using Regular Expression',
                                     width=180,
                                     height=30,
                                     fg_color='Red',
                                     text_color='White',
                                     border_color='Black',
                                     border_width=2,
                                     command=rename_all_file_re)
btn_rename_re.place(x=30,y=375)

btn_rollback = customtkinter.CTkButton(right_fr,
                                     text='Rollback',
                                     width=70,
                                     height=30,
                                     fg_color='#3A7FF6',
                                     text_color='White',
                                     border_color='Black',
                                     border_width=2,
                                     command=rollback)
btn_rollback.place(x=305,y=268)
btn_rollback_re = customtkinter.CTkButton(right_fr,
                                     text='Quit',
                                     width=70,
                                     height=30,
                                     fg_color='#3A7FF6',
                                     text_color='White',
                                     border_color='Black',
                                     border_width=2,
                                     command=lambda:root.destroy())
btn_rollback_re.place(x=305,y=375)

btn_reg_instructions = customtkinter.CTkButton(left_fr,
                                               text='Regular Exp. Examples',
                                               width=50,
                                               height=30,
                                               fg_color='#3A7FF6',
                                               text_color='White',
                                               border_color='Black',
                                               border_width=1,
                                               command=show_ins)
btn_reg_instructions.place(x=20,y=340)

#LISTBOX
ls_box = Listbox(right_fr,
                width=38,
                height=10,
                borderwidth=1,
                background='#e8e6e6'
                )

ls_box.place(x=30,y=80)
     
#BINDING
new_entry.bind("<FocusIn>",clean_new_entry)
old_entry.bind("<FocusIn>",clean_old_entry)
new_entry_re.bind("<FocusIn>",clean_new_entry_re)
old_entry_re.bind("<FocusIn>",clean_old_entry_re)


root.mainloop()