import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

# 定义合并音视频的函数
def merge_audio_video():
    # 获取文件路径
    video_path = entry_video.get()
    audio_path = entry_audio.get()
    output_path = entry_output.get()

    # 检查文件路径是否已选择
    if not all([video_path, audio_path, output_path]):
        messagebox.showerror("错误", "请先选择所有文件。")
        return

    # 确保输出文件有正确的扩展名
    if not output_path.lower().endswith('.mp4'):
        output_path += '.mp4'

    try:
        # 执行ffmpeg命令合并音视频
        subprocess.run([
            'ffmpeg', '-y', '-i', audio_path, '-i', video_path, 
            '-c:v', 'copy', '-c:a', 'copy', output_path
        ], check=True)
        messagebox.showinfo("完成", "音视频合并完成！")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("错误", f"合并过程中发生错误: {e}")

# 文件选择的回调函数
def choose_file(entry, file_type):
    file_path = filedialog.askopenfilename(title=f"选择{file_type}文件", filetypes=[("MP4 files", "*.mp4")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

# 文件另存为的回调函数
def choose_output_file(entry):
    file_path = filedialog.asksaveasfilename(title="另存为", filetypes=[("MP4 files", "*.mp4")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

# 初始化Tkinter窗口
root = tk.Tk()
root.title("音视频合并工具")

# 创建输入框和按钮
entry_video = tk.Entry(root, width=50)
entry_audio = tk.Entry(root, width=50)
entry_output = tk.Entry(root, width=50)

video_button = tk.Button(root, text="浏览", command=lambda: choose_file(entry_video, "视频"))
audio_button = tk.Button(root, text="浏览", command=lambda: choose_file(entry_audio, "音频"))
output_button = tk.Button(root, text="另存为", command=lambda: choose_output_file(entry_output))

# 创建文本标签
video_label = tk.Label(root, text="输入视频(仅含画面):")
audio_label = tk.Label(root, text="输入音频(仅含音频):")
output_label = tk.Label(root, text="输出视频(合并后):")

# 使用grid布局管理器放置组件
video_label.grid(row=0, column=0, sticky="e")
entry_video.grid(row=0, column=1, padx=10, pady=5)
video_button.grid(row=0, column=2, padx=10, pady=5)

audio_label.grid(row=1, column=0, sticky="e")
entry_audio.grid(row=1, column=1, padx=10, pady=5)
audio_button.grid(row=1, column=2, padx=10, pady=5)

output_label.grid(row=2, column=0, sticky="e")
entry_output.grid(row=2, column=1, padx=10, pady=5)
output_button.grid(row=2, column=2, padx=10, pady=5)

# 创建开始转换的按钮并布局
btn_merge = tk.Button(root, text="开始转换", command=merge_audio_video)
btn_merge.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# 设置窗口的初始大小
root.geometry("+400+250")
root.mainloop()