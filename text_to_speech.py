from gtts import gTTS
import os

# 輸入你想要說的文字
text = "這是一個測試。"

# 將文字轉換成語音
tts = gTTS(text, lang='zh-tw')

# 儲存語音檔案
tts.save("output.mp3")

# 播放語音
os.system("aplay output.mp3")
