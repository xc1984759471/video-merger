# video-merger

将纯视频和纯音频MP4合并为单独的MP4视频

# 脚本功能
通过将仅包含音频的mp4文件和与之相对应的仅包含视频画面的mp4文件合为单个含音视频的mp4文件，适用于视频网站音视频分离下载的视频合成。

**目前本脚本暂只支持纯音视频mp4的转换**

本脚本适用于Windows、Linux和Mac。
![image](https://github.com/xc1984759471/video-merger/assets/53083866/ca4aeb7f-cab0-4af7-8a3a-7e6d924d9a14)
# 依赖关系
[ffmpeg](https://ffmpeg.org/)（**重要**）：用于合并视频的后端程序（需要添加至PATH变量目录中，Linux/Mac可通过apt、yum、pacman、brew等方式安装）

python3

tkinter和subprocess库
# 使用方法
```
python merge-video.py
```
选择要输入的纯视频和纯音频文件，并指定输出路径和文件名，点击“开始转换”，大功告成！
