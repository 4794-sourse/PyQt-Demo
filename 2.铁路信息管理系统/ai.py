import tkinter as tk
from tkinter import messagebox
import zhipuai
import re
import time
import pickle

def typing_effect(text_widget, text):
    for char in text:
        text_widget.insert(tk.END, char)
        text_widget.update()
        time.sleep(0.03)

def send_message(event=None):
    api_key = api_entry.get()
    user_input = chat_input.get().strip()
    if api_key and user_input:
        try:
            zhipuai.api_key = api_key
            response_data = zhipuai.model_api.invoke(
                model="chatglm_pro",
                prompt=[{"role": "user", "content": user_input}],
                top_p=0.7,
                temperature=0.9,
            )
            answer = response_data['data']['choices'][0]['content']
            parsed_answer = re.findall(r'\"(.*?)\"', answer)[0]
            parsed_answer = parsed_answer.replace("\\n\\n", "\n").replace("\\n", "\n")
            chat_output.config(state=tk.NORMAL)
            chat_output.insert(tk.END, "我：" + user_input + "\n", 'red')
            typing_effect(chat_output, "AI：" + parsed_answer + "\n")
            chat_output.yview_moveto(1.0)  # 将滚动条移动到文本框底部
            chat_output.config(state=tk.DISABLED)
            chat_input.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("错误", str(e))
    else:
        messagebox.showwarning("提示", "请输入API密钥和对话内容！")

def save_api_key():
    api_key = api_entry.get()
    if api_key:
        with open("api_key.pkl", "wb") as f:
            pickle.dump(api_key, f)
        messagebox.showinfo("提示", "API密钥已保存！")
    else:
        messagebox.showwarning("提示", "请输入API密钥！")

def show_ai_reply(reply):
    chat_output.config(state=tk.NORMAL)
    chat_output.insert(tk.END, "AI：" + reply + "\n", 'green')
    chat_output.yview_moveto(1.0)  # 将滚动条移动到文本框底部
    chat_output.config(state=tk.DISABLED)

window = tk.Tk()
window.title("人工智能智谱AI对话")
window.geometry("1140x447")
window.attributes("-alpha", 0.95)
bg_color = "#f2f2f2"
input_color = "black"
output_color = "green"
window.configure(bg=bg_color)

api_label = tk.Label(window, text="API密钥", bg=bg_color, fg=input_color, font=("Arial", 14, "bold"))
api_label.pack(pady=10)
api_entry = tk.Entry(window, width=50, font=("Arial", 12))
api_entry.pack(pady=5)

save_button = tk.Button(window, text="保存密钥", command=save_api_key, font=("Arial", 12), bg="#2196f3", fg="white")
save_button.pack(pady=5)

try:
    with open("api_key.pkl", "rb") as f:
        api_key = pickle.load(f)
        api_entry.insert(tk.END, api_key)
except FileNotFoundError:
    pass

input_frame = tk.Frame(window, bg=bg_color)
input_frame.pack(pady=10)
chat_input = tk.Entry(input_frame, width=60, font=("Arial", 12), fg='red')
chat_input.pack(side=tk.LEFT)
send_button = tk.Button(input_frame, text="发送", command=send_message, font=("Arial", 12), bg="#2196f3", fg="white")
send_button.pack(side=tk.LEFT, padx=10)

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_output = tk.Text(window, height=10, width=116, font=("Arial", 12), fg=output_color,
                      yscrollcommand=scrollbar.set, wrap=tk.WORD)
chat_output.pack(pady=5)

scrollbar.config(command=chat_output.yview)

window.mainloop()
