import requests
from datetime import datetime
from tkinter import *
import webbrowser
def weather_press ():
    webbrowser.open("https://weather.com/weather/today/l/cb9a4442e9bf7da0ece89bd21a5161210e79cccc0ec2647b3565977e7a278c31")
weather_data = requests.get(
    f"https://api.open-meteo.com/v1/forecast?latitude=22.99&longitude=120.21&hourly=temperature_2m,rain&daily=sunset,rain_sum&current_weather=true&timeformat=unixtime&forecast_days=1&timezone=Asia%2FSingapore")
weather_tem =weather_data.json()["current_weather"]["temperature"]
weather_windsp =weather_data.json()["current_weather"]["windspeed"]
weather_maxtem = max(weather_data.json()["hourly"]["temperature_2m"])
weather_mintem = min(weather_data.json()["hourly"]["temperature_2m"])
timestamp = weather_data.json()["daily"]["time"][0]
date_str = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
win = Tk()
weather_img = PhotoImage(file=r'C:\Users\user\OneDrive\桌面\weather app\img\weather.png')
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x = screen_width - 350
y = screen_height - 200
win.title("weather app")
win.geometry(f"350x150+1186+730")
win.resizable(0,0)

maxtem = Label(text="最高溫:")
maxtem.config(bg="orange")
maxtem.grid(row=0,column=0)
maxtem_lab = Label(text=weather_maxtem)
maxtem_lab.config(bg="orange")
maxtem_lab.grid(row=0,column=1)

mintem = Label(text="最低溫:")
mintem.config(bg="lightblue")
mintem.grid(row=1,column=0)
mintem_lab = Label(text=weather_mintem)
mintem_lab.config(bg="lightblue")
mintem_lab.grid(row=1,column=1)

tem = Label(text="現溫度:")
tem.config(bg="yellow")
tem.grid(row=2,column=0)
tem_lab = Label(text= weather_tem)
tem_lab.config(bg="yellow")
tem_lab.grid(row=2,column=1)

weather_btn = Button(text="weather")
weather_btn.config(image=weather_img)
weather_btn.place(anchor=CENTER,x=200,y=70,width=200,height=100)
weather_btn.config(command=weather_press)

date_lab= Label(text=date_str)
date_lab.config(bg="skyblue")
date_lab.place(anchor=CENTER,x=305,y=140)

print(weather_windsp)
win.mainloop()