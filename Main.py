import sys
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

try:
    import tkinter.ttk as ttk
    py3 = False
except ImportError:
    import ttk
    py3 = True

import mainGUI_support as main_gui_support
import os.path
import Home as home

def start_gui():
    '''Starting point when the module is the main routine.'''
    global val, root, top
    global program_location
    program_call = sys.argv[0]
    program_location = os.path.split(program_call)[0]
    root = tk.Tk()
    top = Toplevel1(root)
    main_gui_support.init(root, top)
    root.mainloop()

w = None

def create_toplevel(root, *args, **kwargs):
    '''Starting point when the module is imported by another program.'''
    global w, w_win, rt
    global program_location
    program_call = sys.argv[0]
    program_location = os.path.split(program_call)[0]
    rt = root
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    main_gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_toplevel():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):

        def dataset_1(event):
            top.destroy()
            home.start_gui("small")

        def dataset_2(event):
            top.destroy()
            home.start_gui("large")

        def exit_application(event):
            import os
            os._exit(0)

        background_color = '#d9d9d9'
        foreground_color = '#000000'
        component_color = '#d9d9d9'
        ana_1_color = '#d9d9d9'
        ana_2_color = '#ececec'
        font_16 = "-family Constantia -size 40 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font_18 = "-family {Sitka Small} -size 15 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"

        window_width = 1000
        window_height = 650
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)
        top.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))
        top.title("Accident Detection System")
        top.configure(background="#ffffff")

        self.label_1 = tk.Label(top)
        self.label_1.place(relx=0.3, rely=0.01, height=250, width=350)
        self.label_1.configure(background="#ffffff")
        self.label_1.configure(disabledforeground="#a3a3a3")
        self.label_1.configure(foreground="#000000")
        photo_location = os.path.join(program_location, "Images/icon.png")
        self.image_0 = tk.PhotoImage(file=photo_location)
        self.label_1.configure(image=self.image_0)
        self.label_1.configure(text='''Label''')

        self.label_2 = tk.Label(top)
        self.label_2.place(relx=0.0, rely=0.35, height=88, width=1000)
        self.label_2.configure(background="#ffffff")
        self.label_2.configure(disabledforeground="#a3a3a3")
        self.label_2.configure(font=font_16)
        self.label_2.configure(foreground="#2365e8")
        self.label_2.configure(text='''Accident & Animal Detection System''')
        self.label_2.configure(width=659)

        self.frame_1 = tk.Frame(top)
        self.frame_1.place(relx=0.03, rely=0.535, relheight=0.402, relwidth=0.94)
        self.frame_1.configure(relief='groove')
        self.frame_1.configure(borderwidth="7")
        self.frame_1.configure(relief="groove")
        self.frame_1.configure(background="#ffffff")
        self.frame_1.configure(width=955)

        self.btn_image_1 = tk.Label(self.frame_1)
        self.btn_image_1.place(relx=0.1, rely=0.110, height=176, width=172)
        self.btn_image_1.configure(activebackground="#f9f9f9")
        self.btn_image_1.configure(activeforeground="black")
        self.btn_image_1.configure(background="#ffffff")
        self.btn_image_1.configure(disabledforeground="#a3a3a3")
        self.btn_image_1.configure(foreground="#000000")
        self.btn_image_1.configure(highlightbackground="#d9d9d9")
        self.btn_image_1.configure(highlightcolor="black")
        photo_location = os.path.join(program_location, "Images/images icon.png")
        self.image_3 = tk.PhotoImage(file=photo_location)
        self.btn_image_1.configure(image=self.image_3)
        self.btn_image_1.configure(text='''Label''')
        self.btn_image_1.configure(width=172)
        self.btn_image_1.bind('<Button-1>', dataset_1)

        self.label_3_61 = tk.Label(self.frame_1)
        self.label_3_61.place(relx=0.1, rely=0.784, height=36, width=200)
        self.label_3_61.configure(activebackground="#f9f9f9")
        self.label_3_61.configure(activeforeground="black")
        self.label_3_61.configure(background="#ffffff")
        self.label_3_61.configure(disabledforeground="#a3a3a3")
        self.label_3_61.configure(font=font_18)
        self.label_3_61.configure(foreground="#061104")
        self.label_3_61.configure(highlightbackground="#d9d9d9")
        self.label_3_61.configure(highlightcolor="#000000")
        self.label_3_61.configure(text='''YOLO V8 (Small)''')
        self.label_3_61.configure(width=142)

        self.label_3_5 = tk.Label(self.frame_1)
        self.label_3_5.place(relx=0.42, rely=0.784, height=26, width=200)
        self.label_3_5.configure(activebackground="#f9f9f9")
        self.label_3_5.configure(activeforeground="black")
        self.label_3_5.configure(background="#ffffff")
        self.label_3_5.configure(disabledforeground="#a3a3a3")
        self.label_3_5.configure(font=font_18)
        self.label_3_5.configure(foreground="#061104")
        self.label_3_5.configure(highlightbackground="#d9d9d9")
        self.label_3_5.configure(highlightcolor="#000000")
        self.label_3_5.configure(text='''YOLO V8 (Large)''')
        self.label_3_5.configure(width=142)

        self.btn_webcam = tk.Label(self.frame_1)
        self.btn_webcam.place(relx=0.45, rely=0.157, height=154, width=154)
        self.btn_webcam.configure(background="#ffffff")
        self.btn_webcam.configure(disabledforeground="#a3a3a3")
        self.btn_webcam.configure(foreground="#000000")
        photo_location = os.path.join(program_location, "Images/webcam icon.png")
        self.image_1 = tk.PhotoImage(file=photo_location)
        self.btn_webcam.configure(image=self.image_1)
        self.btn_webcam.configure(text='''Label''')
        self.btn_webcam.bind('<Button-1>', dataset_2)

        self.btn_exit = tk.Label(self.frame_1)
        self.btn_exit.place(relx=0.822, rely=0.100, height=186, width=150)
        self.btn_exit.configure(activebackground="#f9f9f9")
        self.btn_exit.configure(activeforeground="black")
        self.btn_exit.configure(background="#ffffff")
        self.btn_exit.configure(disabledforeground="#a3a3a3")
        self.btn_exit.configure(foreground="#000000")
        self.btn_exit.configure(highlightbackground="#d9d9d9")
        self.btn_exit.configure(highlightcolor="black")
        photo_location = os.path.join(program_location, "Images/ExitIcon.png")
        self.image_4 = tk.PhotoImage(file=photo_location)
        self.btn_exit.configure(image=self.image_4)
        self.btn_exit.configure(text='''Label''')
        self.btn_exit.configure(width=162)
        self.btn_exit.bind('<Button-1>', exit_application)

        self.label_3_6 = tk.Label(self.frame_1)
        self.label_3_6.place(relx=0.832, rely=0.784, height=26, width=130)
        self.label_3_6.configure(activebackground="#f9f9f9")
        self.label_3_6.configure(activeforeground="black")
        self.label_3_6.configure(background="#ffffff")
        self.label_3_6.configure(disabledforeground="#a3a3a3")
        self.label_3_6.configure(font=font_18)
        self.label_3_6.configure(foreground="#061104")
        self.label_3_6.configure(highlightbackground="#d9d9d9")
        self.label_3_6.configure(highlightcolor="#000000")
        self.label_3_6.configure(text='''Exit''')
        self.label_3_6.configure(width=142)
