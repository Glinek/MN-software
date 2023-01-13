import requests, customtkinter as ctk, random, shutil, socket, os, platform, distro, psutil
from datetime import datetime, date
from tkinter import *

#---------------------STRINGS---------------------
color = "#127d90"

#------------------INITIAL SETUP-------------------
ctk.set_appearance_mode("Dark")
root=ctk.CTk()
root.geometry("1000x600")
root.title("MentalDefibrilator")
root.attributes('-alpha')
root.resizable(width=False, height=False)

#-------------------BACKGROUND---------------------
bg1 = ctk.CTkLabel(master=root, width=220, text=None,
height=600, fg_color="#333333")
bg1.place(x=0,y=0)

#--------------------SWITCHES---------------------
switch_var1 = ctk.StringVar(value="on")
def switch_update():
    if switch_var1.get() == "off":
        refresh = 20000000000
    else:
        refresh = 5000
    return refresh
switch_1 = ctk.CTkSwitch(master=root, text="Refresh", command=switch_update,
variable=switch_var1, onvalue="on", offvalue="off", bg_color="#333333", progress_color=color)
switch_1.place(x=10, y=170)

#-----------------------TIME-----------------------
def update_time():
    time = datetime.now().strftime("%c")
    time_label=ctk.CTkLabel(master=bg1, width=200, text=time, 
    height=30, corner_radius=7, fg_color=color)
    time_label.place(x=10, y=10)
    root.after(1000, update_time)
update_time()

#-----------------------WTTR-----------------------
#blue background
wttr_bg = ctk.CTkLabel(master=root, text="WTTR", fg_color="#333333", 
width=210, height=180, corner_radius=7,)
wttr_bg.place(x=230, y=10)

#open .txt and read city
try:
    def update_wttr():
        f1 = open("settings.txt", "r", encoding="utf8")
        data1 = f1.readlines()
        cityy = str(data1[0])
        city = cityy.rstrip()
        url = 'https://wttr.in/' + city + '?format=Weather: %C+%c\n+Temperatue: %t (%f)\n+Wind: '
        url += '%w\n+Precipitation: %p\n+Pressure: %P\n+Time_zone: %Z\n'
        res = requests.get(url)
        f1.close()
        #display wttr
        wttr=ctk.CTkLabel(master=wttr_bg,text=(city+"\n"+res.text), width=200, 
        height=130, corner_radius=7, fg_color="#333333")
        wttr.place(x=5, y=5)
        root.after(1000, update_wttr)
except:
    wttr_ni=ctk.CTkLabel(master=wttr_bg,text=("No internet connection"), width=200, 
    height=130, corner_radius=7, fg_color="#333333")
    wttr_ni.place(x=5, y=5)

#wttr entry point
wttr_in = ctk.CTkEntry(master=wttr_bg,width=130, height=30, corner_radius=7, 
placeholder_text="City", fg_color=("#333333"), border_color=("#333333"))
wttr_in.place(x=5, y=145)

#def for button
def city():
    city_in = wttr_in.get()
    f2 = open("settings.txt", "r", encoding="utf8")
    data2 = f2.readlines()
    data2[0] = city_in + "\n"
    f2.close()
    f2 = open("settings.txt", "w", encoding="utf8")
    f2.writelines(data2)
    f2.close()
    update_wttr()

#wttr button
wttr_button = ctk.CTkButton(master=wttr_bg, width=60, height=30, 
text="Change", command=city, fg_color=color, hover_color="#333333")
wttr_button.place(x=145,y=145)

#----------------------REMINDER-------------------
#reminder background
remind_bg = ctk.CTkLabel(master=root,text=None, fg_color="#333333", 
width=210, height=80, corner_radius=7)
remind_bg.place(x=230, y=210)

#date and remind entry
reminder_in_date = ctk.CTkEntry(master=remind_bg,width=130, height=30, corner_radius=7, 
placeholder_text="date", fg_color="#333333", border_color="#333333")
reminder_in_date .place(x=5, y=45)

reminder_in_remind = ctk.CTkEntry(master=remind_bg,width=200, height=30, corner_radius=7, 
placeholder_text="remind", fg_color="#333333", border_color="#333333")
reminder_in_remind .place(x=5, y=5)

#def to save
def reminder_save():
    f_write = open("reminder.txt", "a", encoding="utf8")
    datee = reminder_in_date.get()
    thing = reminder_in_remind.get()
    f_write.write("@" + datee + "  " + thing + "\n")
    f_write.close()

#button
reminder_button = ctk.CTkButton(master=remind_bg, width=60, height=30, 
text="Save", command=reminder_save, fg_color=color, hover_color="#333333")
reminder_button.place(x=145,y=45)

#reminder out
f_read = open("reminder.txt","r",encoding="utf8")
try:
    for sth in f_read:
        if sth.startswith("@"):
            check = sth[1:11]
            date_now = date.today().strftime("%d-%m-%Y")
            if check == date_now:
                dc_thing = sth[11:]
                reminder_out_text = (dc_thing.lstrip()).rstrip()
    reminder_out = ctk.CTkLabel(master=bg1, text="Today:\n"+reminder_out_text, width=200, 
    height=60, corner_radius=7, fg_color=color)
    reminder_out.place(x=10, y=50)
    f_read.close()
except:
    reminder_out = ctk.CTkLabel(master=bg1, text="Today:\nnothing for today", width=200, 
    height=60, corner_radius=7, fg_color=color)
    reminder_out.place(x=10, y=50)

#------------------RANDOM WORDS--------------------
#words
WORDS = ("Have a nice day", "Always be creative", "100% not orginal", 
"This code is a mess", "MINECRAFT <3",  "Miau", "Started in: was never tested",
"Cyberdeck.cafe", "test 01", "tested on Kali linux", "Everything is wrong", 
"Don't trust me", "Safe to use on plane", "?", "hi", "Servus!", "Siemka", "hola",
"Why by Sabrina Carpenter", "made within 24h", "made by Glinek", "Mikołów", 
"Your data is not safe", "Pipipikpimi", "Kingpin", "i/o", "Absolutely Not")
word = random.choice(WORDS)

#ctk
words = ctk.CTkLabel(master=bg1, text=word, 
fg_color=color, width=200, height=30, corner_radius=7)
words.place(x=10, y=560)

#----------------------STATS-----------------------
#bytes to GB
total, used, free = shutil.disk_usage(__file__)
ff = round(free /1024**3)
tt = round(total /1024**3)
uu = round(used /1024**3)

#getting strings
stats1 = "Architecture: " + str(platform.architecture()[0]) + "\nSystem: " + str(platform.system()) + "\nDistro: " + str(distro.name())
stats2 = "\nUser: " + str(os.getlogin()) + "\nIP: " + socket.gethostbyname(socket.gethostname())
disk_space = "Total:" + str(tt) + "\n Used: " + str(uu) + " GB\n Free: "+ str(ff) +"GB"
ram_percent = psutil.virtual_memory()[2]
speed = psutil.net_io_counters(pernic=False)
speed_send = round(speed[2]/1024, 2)
speed_precv = round(speed[3]/1024, 2)

#ctk
bg_stats = ctk.CTkLabel(master=root, text=None, fg_color="#333333", 
width=240, height=100, corner_radius=7)
bg_stats.place(x=230, y=310)
stats = ctk.CTkLabel(master=bg_stats, text=stats1 +stats2, 
fg_color=("#333333"), width=120, height=90, corner_radius=7)
stats.place(x=5, y=5)
disk = ctk.CTkLabel(master=bg_stats, text="Disk space\n" + disk_space,
fg_color=("#333333"), width=100, height=90, corner_radius=7)
disk.place(x=135, y=5)

#movable stats
def update_stats():
    #ram
    ref = int(switch_update())
    ram_percent = psutil.virtual_memory()[2]
    ram = ram_percent*2.3
    ram1 = ctk.CTkLabel(master=root, text="RAM %\n",
    fg_color=("#333333"), width=240, height=40, corner_radius=7)
    ram1.place(x=230, y=420)
    ram2 = ctk.CTkLabel(master=ram1, text=None,
    fg_color=color, width=ram, height=10, corner_radius=7)
    ram2.place(x=5, y=20)

    #sent speed
    speed = psutil.net_io_counters(pernic=False)
    speed_send = round(speed[2]/1024**2, 2)
    
    io1 = ctk.CTkLabel(master=root, text="Upload Mb/s\n",
    fg_color=("#333333"), width=240, height=40, corner_radius=7)
    io1.place(x=230, y=470)
    io = round(speed_send / 230 *10+20)
    io2 = ctk.CTkLabel(master=io1, text=None,
    fg_color=color, width=io, height=10, corner_radius=7)
    io2.place(x=5, y=20)

    #download speed
    speed_precv = round(speed[3]/1024**2, 2)
    ii1 = ctk.CTkLabel(master=root, text="Download Mb/s\n",
    fg_color=("#333333"), width=240, height=40, corner_radius=7)
    ii1.place(x=230, y=520)
    ii = round(speed_precv /230 *10+20)
    ii2 = ctk.CTkLabel(master=ii1, text=None,
    fg_color=color, width=ii, height=10, corner_radius=7)
    ii2.place(x=5, y=20)
    root.after(ref, update_stats)
update_stats()

root.mainloop()
