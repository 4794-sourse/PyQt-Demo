import os
import tkinter as tk
from tkinter import filedialog, font
import win32api
import win32con
import time
import json
from concurrent.futures import ThreadPoolExecutor

exenlist = []

def open_app(app_dir):
    os.startfile(app_dir)

def select_program():
    program_dir = filedialog.askopenfilename()
    if program_dir:
        exenlist.append(program_dir)
        program_listbox.insert(tk.END, program_dir)

def save_config():
    config = {"exenlist": exenlist}
    with open("config.json", "w") as f:
        json.dump(config, f)
    win32api.MessageBox(0, "配置已保存", "保存配置", win32con.MB_OK)

def delete_config():
    global exenlist
    exenlist = []
    program_listbox.delete(0, tk.END)
    if os.path.exists("config.json"):
        os.remove("config.json")
        win32api.MessageBox(0, "配置已删除", "删除配置", win32con.MB_OK)
    else:
        win32api.MessageBox(0, "未找到配置文件", "删除配置", win32con.MB_OK)

def load_config():
    global exenlist
    if os.path.exists("config.json"):
        try:
            with open("config.json", "r") as f:
                config = json.load(f)
                exenlist = config.get("exenlist", [])
            for program_dir in exenlist:
                program_listbox.insert(tk.END, program_dir)
        except FileNotFoundError:
            pass
    else:
        win32api.MessageBox(0, "未找到配置文件", "加载配置", win32con.MB_OK)

def start_programs():
    with ThreadPoolExecutor(max_workers=4) as executor:
        for program_dir in exenlist:
            executor.submit(open_app, program_dir)
    print("程序启动器---微信公众号:蓝胖子之家")
    logsys = win32api.MessageBox(0, "已全部启动完成....", "提示", win32con.MB_OK)

# 创建GUI窗口
window = tk.Tk()
window.title("本地智能-程序启动器")
window.geometry("500x600")
window.configure(background='#F5F5F5')

# 设置字体
font_style = font.Font(family="Arial", size=12)

# 创建顶部标签
top_label = tk.Label(window, text="程序启动器", font=("Arial", 20, "bold"), bg="#F5F5F5", fg="#333333")
top_label.pack(pady=20)

# 创建选择程序按钮
select_button = tk.Button(window, text="选择程序", command=select_program, font=font_style, padx=20, pady=10, bg='#ADD8E6', activebackground='#87CEFA')
select_button.pack(pady=10)

# 创建程序列表框
program_listbox = tk.Listbox(window, font=font_style, width=50, height=10, bg='#F0F0F0', fg='#333333', selectbackground='#ADD8E6', selectforeground='#333333')
program_listbox.pack(pady=10)

# 创建按钮框架
button_frame = tk.Frame(window, bg='#F5F5F5')
button_frame.pack(pady=20)

# 创建保存配置按钮
save_button = tk.Button(button_frame, text="保存配置", command=save_config, font=font_style, padx=20, pady=10, bg='#90EE90', activebackground='#98FB98')
save_button.grid(row=0, column=0, padx=10)

# 创建删除配置按钮
delete_button = tk.Button(button_frame, text="删除配置", command=delete_config, font=font_style, padx=20, pady=10, bg='#FF6347', activebackground='#FF7F50')
delete_button.grid(row=0, column=1, padx=10)

# 创建加载配置按钮
load_button = tk.Button(button_frame, text="加载配置", command=load_config, font=font_style, padx=20, pady=10, bg='#FFFF00', activebackground='#FFFF66')
load_button.grid(row=0, column=2, padx=10)

# 创建启动程序按钮
start_button = tk.Button(window, text="一键启动", command=start_programs, font=("Arial", 16, "bold"), padx=30, pady=15, bg='#00FA9A', activebackground='#00FF7F')
start_button.pack(pady=20)

# 运行GUI窗口
window.mainloop()