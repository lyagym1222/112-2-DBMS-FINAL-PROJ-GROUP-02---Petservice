# 簡介
這是一個資料庫管理課程的期末小組專案，我們的組別建構了一個寵物主人與保母的媒合平台，並讓寵物保母能供提供「寄養」及「遛狗/貓」兩種服務，而雙方也都能看到彼此過去的評價與在每次的服務中評價彼此。

# 使用說明
* 主程式的運行為 run.py 這個檔案
* 在首次執行前，請先在 mysql 建立名為「petservice」的schema後
* 在終端機進入python並依序輸入：
1. from backend import db
2. from backend import app
3. app.app_context().push()
4. db.create_all()

# 以下是本專案的組員名單
1. 109405053 李亞駿
2. 109303073 陳姿妤
3. 109304040 黃育心
4. 109305072 朱耀宇
5. 109304019 周佳萱
