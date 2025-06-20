import tkinter
from customtkinter import CTk
import os
import customtkinter
from app import handlers, rename_window, sure_window


root = CTk()

customtkinter.set_appearance_mode('Light')
customtkinter.set_default_color_theme('blue')

root.geometry('700x500')
root.resizable(True, True)
root.minsize(700, 500)

root.title('Click Recorder')

root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(5, weight=1)

run_state = 'disabled' if os.path.isdir('../files') is False or os.listdir('../files') == [] else 'enabled'

rec_btn = customtkinter.CTkButton(master=root,
                              width=250,
                              height=50,
                              border_width=0,
                              corner_radius=10,
                              text='Rec.',
                              command=handlers.listen)

rec_btn.place(relx=0.8, rely=0.3, anchor=tkinter.CENTER)

run_btn = customtkinter.CTkButton(master=root,
                              width=250,
                              height=50,
                              border_width=0,
                              corner_radius=10,
                              text='Run',
                              command=handlers.run)

run_btn.place(relx=0.8, rely=0.45, anchor=tkinter.CENTER)

ext_btn = customtkinter.CTkButton(master=root,
                                  width=250,
                                  height=50,
                                  border_width=0,
                                  corner_radius=10,
                                  text='Exit',
                                  command=root.quit,
                                  fg_color='black')

ext_btn.place(relx=0.5, rely=0.90, anchor=tkinter.CENTER)

del_bn = customtkinter.CTkButton(master=root,
                                 width=250,
                                 height=50,
                                 border_width=0,
                                 corner_radius=10,
                                 text='Delete',
                                 command=sure_window.open)

del_bn.place(relx=0.8, rely=0.60, anchor=tkinter.CENTER)

del_all_btn = customtkinter.CTkButton(master=root,
                                      width=250,
                                      height=50,
                                      border_width=0,
                                      corner_radius=10,
                                      text='Delete\nALL files',
                                      command=sure_window.open)

del_all_btn.place(relx=0.8, rely=0.75, anchor=tkinter.CENTER)


rename = customtkinter.CTkButton(master=root,
                                 width=250,
                                 height=50,
                                 border_width=0,
                                 corner_radius=10,
                                 text='Rename',
                                 command=rename_window.open)

rename.place(relx=0.2, rely=0.45, anchor=tkinter.CENTER)


def refresh_combo_box():
    return os.listdir(f'{os.getcwd()}\\files\\')


refresh = customtkinter.CTkButton(master=root,
                                 width=250,
                                 height=50,
                                 border_width=0,
                                 corner_radius=10,
                                 text='Refresh',
                                 command=refresh_combo_box)

refresh.place(relx=0.2, rely=0.75, anchor=tkinter.CENTER)


combobox_var = customtkinter.StringVar(value='Default')
combobox_values = refresh_combo_box()
combobox = customtkinter.CTkComboBox(master=root, values=combobox_values, variable=combobox_var, width=350)
combobox.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)

# logo_img = Image.open('logos\\main_logo.png')
# ctk_img = customtkinter.CTkImage(light_image=logo_img,size=(300, 100))
# label = customtkinter.CTkLabel(master=root, image=ctk_img)
# label.place(relx=0.25, rely=0.02)