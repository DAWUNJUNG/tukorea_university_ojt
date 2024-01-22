import time
import datetime
import webbrowser

# 1 시간마다 임의의 노트북 열기
for i in range(12):
    # 기본 브라우저를 사용하기 위해 주석처리
    # browse = webbrowser.get("chrome")
    webbrowser.open("https://colab.research.google.com/drive/1AqCStbFlwTQyB2SJ5YE8kmPRNJJ5LYNk#scrollTo=EYamT5F-fwby")
    print(i, datetime.datetime.today())
    time.sleep(60*60)
