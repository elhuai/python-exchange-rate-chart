import requests
import openpyxl
from openpyxl.chart import LineChart, Reference


#抓取台銀資料
url = 'https://rate.bot.com.tw/xrt/flcsv/0/L3M/USD'   
datas = requests.get(url)   # 爬取網址內容
datas.encoding = 'utf-8'    # 調整回應訊息編碼為 utf-8，避免編碼不同造成亂碼
rt = datas.text             # 以文字模式讀取內容
#print(rt)
rts = rt.split('\n')       # 使用「換行」將內容拆分成串列

sale_rate = []
for daily in rts:              # 讀取串列的每個項目
    try:                             # 使用 try 避開最後一行的空白行
        daily_data = daily.split(',')          
        #print(daily_data)
        sale_rate.append([daily_data[0],daily_data[13]])

    except:
      break

print(sale_rate)
#匯入excel檔案
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "美金現金賣出" 

for row in sale_rate:
       ws.append(row)

#繪製圖表

chart = LineChart()                 # 長條圖
chart.title = '美金匯率'        # 圖表標題
chart.y_axis.title = '匯率'      # y軸標題
chart.x_axis.title = '日期'         # x軸標題

data = Reference(ws, min_col=1 ,max_col=2, min_row=2,
                 max_row=ws.max_row)  

chart.add_data(data, titles_from_data=True)  # 建立圖表
xtitle = Reference(ws, min_col=1, min_row=1)
chart.set_categories(xtitle)              
ws.add_chart(chart, 'C1')      

wb.save("匯率及時更新.xlsx") 

