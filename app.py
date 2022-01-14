from tkinter import *
from custom_database import *
from PIL import Image, ImageTk
import time
tk= Tk()
tk.title('Carpentry Application')
x='1920'
y='1080'
tk.geometry(x+"x"+y+"+10+20")
name=None
password=None
startup=True
other=None
other1=None
other2=None
other3=None #Encypt/Decrypt Password
#If a button is called, it is displayed on the screen.
class buttons:
    def create_user(anchor=None, side=None):
        e1 = Button(tk, text='Create User', command=options.create_user, bg=button_color, foreground=text_color, font=text_font)
        e1.config(height=button_height, width=button_width)
        e1.place(x=((int(x))/2)-330, y=300)
    def remove_user(anchor=None, side=None):
        e2 = Button(tk, text='Remove User', command=options.remove_user, bg=button_color, foreground=text_color, font=text_font)
        e2.config(height=button_height, width=button_width)
        e2.place(x=((int(x))/2)-330, y=400)
    def change_password(anchor=None, side=None):
        global x, y
        e3 = Button(tk, text='Change Password', command=options.create_password, bg=button_color, foreground=text_color, font=text_font)
        e3.config(height=button_height, width=button_width)
        e3.place(x=((int(x))/2)-330, y=800)
    def logout(anchor=None, side=None, y=700):
        e4 = Button(tk, text='Logout', command=options.logout, bg=button_color, foreground=text_color, font=text_font)
        e4.config(height=button_height, width=button_width)
        e4.place(x=((int(x))/2)-330, y=y)
    def save(anchor=None, side=None):
        e5 = Button(tk, text='Save', command=options.save, bg=button_color, foreground=text_color, font=text_font)
        e5.config(height=button_height, width=button_width)
        e5.place(x=((int(x))/2)-330, y=500)
    def optimize(anchor=None, side=None):
        e6 = Button(tk, text='Optimize', command=options.optimize, bg=button_color, foreground=text_color, font=text_font)
        e6.config(height=button_height, width=button_width)
        e6.place(x=((int(x))/2)-330, y=600)
    def add_tool(anchor=None, side=None):
        e7 = Button(tk, text="Add Tool",command=options.add_tool, bg=button_color, foreground=text_color, font=text_font)
        e7.config(height=button_height, width=button_width)
        e7.place(x=((int(x))/2)-330, y=0)
    def remove_tool(anchor=None, side=None):
        e8 = Button(tk, text='Remove Tool', command=options.remove_tool, bg=button_color, foreground=text_color, font=text_font)
        e8.config(height=button_height, width=button_width)
        e8.place(x=((int(x))/2)-330, y=100)
    def show_tools(anchor=None, side=None):
        e9 = Button(tk, text='Show tools', command=options.show_tools, bg=button_color, foreground=text_color, font=text_font)
        e9.config(height=button_height, width=button_width)
        e9.place(x=((int(x))/2)-330, y=200)
    def clear_history(anchor=None, side=None):
        e10 = Button(tk, text='Clear History', command=options.clear_history, bg=button_color, foreground=text_color, font=text_font)
        e10.config(height=button_width, width=button_width)
        e10.place(x=0, y=0)
    def signout_item(anchor=None, side=None):
        e11 = Button(tk, text='Signout item', command=options.signout_item, bg=button_color, foreground=text_color, font=text_font)
        e11.config(height=button_height, width=button_width)
        e11.place(x=((int(x))/2)-330, y=100)
    def signin_item(anchor=None, side=None):
        e12 = Button(tk, text='Signin item', command=options.signin_item, bg=button_color, foreground=text_color, font=text_font)
        e12.config(height=button_height, width=button_width)
        e12.place(x=((int(x))/2)-330, y=0)
    def backup():
        e13 = Button(tk, text='Backup', command=options.backup, bg=button_color, foreground=text_color, font=text_font)
        e13.config(height=button_width, width=button_width)
        e13.pack(side=LEFT)
class options:
    def backup():
        global other3
        backup.clear_all()
        backup.create(random_name=True, password=other3)
    def clear_history():
        history.clear()
    def show_tools():
        clear()
        e1 = Label(tk, text='Check terminal for info.', bg=button_color, foreground=text_color)
        e1.config(height=button_height, width=button_width+5)
        e1.pack()
        e2 = Button(tk, text='Back', command=send, bg=button_color, foreground=text_color)
        e2.config(height=button_height, width=button_width)
        e2.pack()
        data_base.edit.app.show_tools(data_base='tools')
    def signout_item():
        global other, other1
        clear()
        e1 = Label(tk, text='Barcode', bg=button_color, foreground=text_color)
        e1.config(height=button_height, width=button_width)
        e1.pack()
        other = Entry(tk)
        other.config(background=entry_background_color, fg=entry_text_color)
        other.pack()
        e2 = Label(tk, text='Your Name', bg=button_color, foreground=text_color)
        e2.config(height=button_height, width=button_width)
        e2.pack()
        other1 = Entry(tk)
        other1.config(background=entry_background_color, fg=entry_text_color)
        other1.pack()
        e3 = Button(tk, text='Submit', command=options.signout_item_next, bg=button_color, foreground=text_color)
        e3.pack()
        e5 = Button(tk, text='Back', command=send, bg=button_color, foreground=text_color)
        e5.pack()
        Tk.update_idletasks(tk)
    def signout_item_next():
        global other, other1
        list1=[other.get(), other1.get()]
        data_base.edit.add_item(data_base='logs', item_to_add=list1)
        clear()
        save.all()
        send()
    def signin_item():
        global other
        clear()
        #Remove item by barcode Not name.
        e1 = Label(tk, text='Barcode', bg=button_color, foreground=text_color)
        e1.config(height=button_height, width=button_width)
        e1.pack()
        other = Entry(tk)
        other.config(background=entry_background_color, fg=entry_text_color)
        other.pack()
        e2 = Button(tk, text='Submit', command=options.signin_item_next, bg=button_color, foreground=text_color)
        e2.config(height=button_height, width=button_width)
        e2.pack()
        e5 = Button(tk, text='Back', command=send, bg=button_color, foreground=text_color)
        e5.config(height=button_height, width=button_width)
        e5.pack()
        Tk.update_idletasks(tk)
    def signin_item_next():
        global other
        data_base.edit.app.remove_item(data_base='logs', barcode=other.get())
        clear()
        save.all()
        send()
    def remove_tool():
        global other
        clear()
        e1 = Label(tk, text='Item name')
        e1.pack()
        other = Entry(tk)
        other.config(background=entry_background_color, fg=entry_text_color)
        other.pack()
        e2 = Button(tk, text='Submit', command=options.remove_tool_next)
        e2.pack()
        e5 = Button(tk, text='Back', command=send)
        e5.pack()
        Tk.update_idletasks(tk)
    def remove_tool_next():
        global other
        name=other.get()
        if profanityFilter.filter(name)==0:
            data_base.edit.app.remove_row(data_base='tools', name=name)
        clear()
        send()
    def add_tool():
        clear()
        global other, other1
        e1 = Label(tk, text='Item name')
        e1.pack()
        other = Entry(tk)
        other.config(background=entry_background_color, fg=entry_text_color)
        other.pack()
        e2 = Label(tk, text='Binary')
        e2.pack()
        other1 = Entry(tk)
        other1.config(background=entry_background_color, fg=entry_text_color)
        other1.pack()
        e3 = Button(tk, text='Submit', command=options.add_tool_next)
        e3.pack()
        e5 = Button(tk, text='Back', command=send)
        e5.pack()
        Tk.update_idletasks(tk)
    def add_tool_next():
        global other, other1
        name = other.get()
        id = other1.get()
        if profanityFilter.filter(name)==0 and profanityFilter.filter(id)==0:
            data_base.edit.add_row(data_base='tools', new_row=[str(name),str(id)], split=False)
        clear()
        send()
    def create_password():
        global other
        clear()
        e1 = Label(tk, text='New password')
        e1.pack()
        other = Entry(tk)
        other.config(background=entry_background_color, fg=entry_text_color)
        other.pack()
        e3 = Button(tk, text='Submit',command=options.create_password_next)
        e3.pack()
        e5 = Button(tk, text='Back', command=send)
        e5.pack()
        Tk.update_idletasks(tk)
    def create_password_next():
        global other
        passw=other.get()
        get.new_hash(passw=passw, normal=True)
        send()
    def logout():
        users.logout()
        clear()
        login()
    def create_user():
        clear()
        global other, other1, other2
        e1 = Label(tk, text='New user')
        e1.pack()
        other = Entry(tk)
        other.config(background=entry_background_color, fg=entry_text_color)
        other.pack()
        e2 = Label(tk, text='Password')
        e2.pack()
        other1 = Entry(tk)
        other1.config(background=entry_background_color, fg=entry_text_color)
        other1.pack()
        e3 = Label(tk, text='Permission')
        e3.pack()
        other2 = Entry(tk)
        other2.config(background=entry_background_color, fg=entry_text_color)
        other2.pack()
        e4 = Button(tk, text='Submit', command=options.create_user_next)
        e4.pack()
        e5 = Button(tk, text='Back', command=send)
        e5.pack()
        Tk.update_idletasks(tk)
    def create_user_next():
        global other, other1, other2
        name=other.get()
        password=other1.get()
        permission=other2.get()
        if profanityFilter.filter(name)==0 and profanityFilter.filter(password)==0 and profanityFilter.filter(permission)==0:
            users.create(new_user=name.lower(), new_password=password, new_permission=permission.lower())
        other, other1, other2 = None, None, None
        send()
    def remove_user():
        clear()
        e1 = Label(tk, text='User')
        e1.pack()
        global other
        other = Entry(tk)
        other.config(background=entry_background_color, fg=entry_text_color)
        other.pack()
        e2 = Button(tk, text='Submit', command=options.remove_user_next)
        e2.pack()
        e5 = Button(tk, text='Back', command=send)
        e5.pack()
        Tk.update_idletasks(tk)
    def remove_user_next():
        global other
        user=other.get()
        user1, permission=users.return_login_cred()
        if user1 != user and profanityFilter.filter(user)==0:
            users.remove(user=user)
        clear()
        send()
    def save():
        save.all()
    def optimize():
        optimize.run(save_optimizations=True)
        clear()
        login()

#Call to clear the screen.
def clear():
    for widget in tk.winfo_children():
        widget.destroy()

#Sends logged in users to correct area depending on permissions.
def send():
    try:
        os.remove('hash.txt')
    except:
        pass
    name, perm= users.return_login_cred()
    if perm == "admin":
        admin_screen()
    if perm == "teacher":
        teacher_screen()
    if perm == "student":
        student_screen()

#If permission is student
def student_screen():
    clear()
    print('Student Screen')
    buttons.signout_item()
    buttons.signin_item()
    buttons.logout(y=200)

#If permission is teacher
def teacher_screen():
    global other3
    #backup.clear_all()
    #backup.create(random_name=True, password=other3)
    clear()
    buttons.add_tool()
    buttons.remove_tool()
    buttons.show_tools()
    buttons.create_user()
    buttons.remove_user()
    buttons.logout(y=500)

#If permission is admin
def admin_screen():
    global other3
    #backup.clear_all()
    #backup.create(random_name=True, password=other3)
    clear()
    print('Admin Screen.')
    buttons.change_password()
    buttons.add_tool()
    buttons.remove_tool()
    buttons.show_tools()
    buttons.create_user()
    buttons.remove_user()
    buttons.save()
    buttons.optimize()
    buttons.logout()
    buttons.clear_history()
    buttons.backup()

#Ask the database if the entered credentials are correct.
def ask():
    global name, password, startup
    user=name.get()
    pass_w=password.get()
    if users.login_request(user=user.lower(), password=pass_w) == True and profanityFilter.filter(str(name))==0 and profanityFilter.filter(str(pass_w))==0:
        print('Login Success!')
        try:
            backup.clear_all()
        except:
            pass
        try:
            backup.create(random_name=True, password=pass_w, hide=True)
        except:
            pass
        u, p = users.return_login_cred()
        if p == "admin" or p=="teacher":
            if startup==True:
                ask_encrypt_password()
            else:
                backup.clear_all()
                backup.create(random_name=True, password=other3)
                send()
        else:
            send()
    else:
        clear()
        print('Incorrect Password Attempt')
        history.create_history(user=user, usage='Login Failed', add_desc=True, desc='Incorrect Password', manual_record=True)
        login(wrong=True)

#Ask for the encyption password to allow for auto backups.
def ask_encrypt_password(wrong=False): 
    if os.path.exists('hash.aes')==1:
        print('Hash file found')
        global other3
        other3=None
        clear()
        e1=Label(tk, text='Enter Encrypt/Decrypt Password', width=23)
        e1.pack()
        other3=Entry(tk)
        other3.config(background=entry_background_color, fg=entry_text_color)
        other3.pack()
        e3=Button(tk, text='Submit', command=ask_encrypt_password_next)
        e3.pack()
        if wrong==True:
            e4=Label(tk, text='Incorrect Password', width=20)
            e4.pack()
        Tk.update_idletasks(tk)
    else:
        print('Could not find hash. Asking user to create one.')
        clear()
        create_encryption_password()
def ask_encrypt_password_next():
    global other3, startup
    other3=other3.get()
    clear()
    if check.encyption_password(other3)==1:
        startup=False
        send()
    else:
        history.create_history('Unknown User', 'Incorrect Encryption Password', manual_record=True)
        ask_encrypt_password(wrong=True)

#Display a screen that allows the user to login.
def login(wrong=False):
    clear()
    global name, password
    e2 = Label(tk, text='Username: ')
    e2.pack()
    name = Entry(tk, highlightbackground='Black')
    name.config(background=entry_background_color, fg=entry_text_color)
    name.pack()
    e4 = Label(tk, text='Password: ')
    e4.pack()
    password = Entry(tk, show='*')
    password.config(background=entry_background_color, fg=entry_text_color, highlightbackground='Black')
    password.pack()
    e1 = Button(tk, text='Login', command=ask, highlightthickness=0, bd=0, borderwidth=0)
    e1.pack()
    e5 = Button(tk, text='Exit', command=exit_app, width=20, highlightthickness=0, bd=0, borderwidth=0)
    e5.config(width=7)
    e5.pack()
    if wrong==True:
        e6=Label(tk, text='Incorrect Password', width=20)
        e6.pack()
    Tk.update_idletasks(tk)

#Exit application
def exit_app():
    global other
    clear()
    e1 = Label(tk, text='Password')
    e1.pack()
    other = Entry(tk, show='*')
    other.config(background=entry_background_color, fg=entry_text_color)
    other.pack()
    e3 = Button(tk, text='Submit',command=exit_app_next)
    e3.pack()
    e4 = Button(tk, text='Back', command=login)
    e4.pack()
    Tk.update_idletasks(tk)
def exit_app_next():
    global other
    pass_w=other.get()
    if encrypt.all(password=pass_w) == 1:
        clear()
        login()
    else:
        exit()

#Decrypt app
def open_app():
    if show_background==True:
        label1 = Label(
            tk,
        )
        label1.place(x=0,y=540)
    global other
    clear()
    e1 = Label(tk, text='Password')
    e1.pack()
    other = Entry(tk, show='*')
    other.config(background=entry_background_color, fg=entry_text_color)
    other.pack()
    e3 = Button(tk, text='Submit', command=open_app_next)
    e3.pack()
def open_app_next():
    global other
    pass_w=other.get()
    if decrypt.all(password=pass_w) == 1:
        clear()
        open_app()
    else:
        clear()
        exit()

#If encryption password(s) don't exist, ask them to make one.
def create_encryption_password():
    global other
    e1=Label(tk, text='Enter new Encryption Password', width=22)
    e1.pack()
    other=Entry(tk)
    other.config(background=entry_background_color, fg=entry_text_color)
    other.pack()
    Tk.update_idletasks(tk)
    e2=Button(tk, text='Submit', command=create_encryption_password_next)
    e2.pack()
def create_encryption_password_next():
    global other
    try:
        get.new_hash(normal=True, passw=str(other.get())) #Makes a new hash
        send()
    except:
        print("Something happen in create_encryption_password")
        clear()
        try:
            os.remove('hash.txt')
        except:
            pass
        create_encryption_password()
tk.config(bg=bg_color)
#Check if the save file is encrypted. If so, ask user for the decrypt password.
if os.path.exists('history.aes')==True or os.path.exists('data_save.aes'):
    open_app()
else:
    login()
tk.mainloop()
