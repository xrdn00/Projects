from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import time
import customtkinter

root = Tk()

now = datetime.now()
root.resizable(width=False, height=False)
root.eval('tk::PlaceWindow . center')
root.title('Weather Report')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
app_width = 800
app_height = 500
x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)
root.geometry("{}x{}+{}+{}".format(int(app_width),int(app_height),int(x),int(y)))
#image file

images = [PhotoImage(file = "src/day1.gif"),PhotoImage(file = "src/night1.gif")]

#canvas

global temp
temp = "37°C"
global h,m,s
h = ""
m = ""
s = ""
def confirm_connection():
    pass
    
def connect():
    global temp
    temp = "37°C"
    label1.configure(text =h+ ":" + m + ":" + s+"\nTEMP: {}".format(temp))
    label0 = customtkinter.CTkLabel(canvas,text = "Connecting...      ",text_color = "black")
    label0.place(x=10,y=40)
    def destroy():
        label0.destroy()
    root.after(1000,destroy)
    def connected():
        root.after(1000)
    
        labelc = customtkinter.CTkLabel(canvas,text = "Connected",text_color = "green")
        labelc.place(x=10,y=40)
        def destroy_c():
            labelc.destroy()
        root.after(1000,destroy_c)
        
        
    root.after(1000,connected)
    
    
    
    
    
    


    

def disconnect():
    global temp
    temp = "N/A"
    label1.configure(text =h+ ":" + m + ":" + s+"\nTEMP: {}".format(temp))
    label0 = customtkinter.CTkLabel(canvas,text = "Disconnecting...",text_color = "black")
    label0.place(x=10,y=40)
    def destroy():
        label0.destroy()
    root.after(1000,destroy)
    def dconnected():
        root.after(1000)
    
        labelc = customtkinter.CTkLabel(canvas,text = "Disconnected",text_color = "red")
        labelc.place(x=10,y=40)
        def destroy_c():
            labelc.destroy()
        root.after(1000,destroy_c)
        
        
    root.after(1000,dconnected)
    
    
    
    
def clock():
    global temp
    global h,m,s
    h = time.strftime("%H")
    m = time.strftime("%M")
    s = time.strftime("%S")
        
    label1.configure(text =h+ ":" + m + ":" + s+"\nTEMP: {}".format(temp))
    label1.after(1000,clock)

def humidity():
    global s
    time_s = int(s)
    if time_s <= 20:
        label3.configure(text="LOW", text_color = "green")
    elif time_s > 20:
        label3.configure(text="MEDIUM", text_color = "orange")
    if time_s > 40:
        label3.configure(text="HIGH", text_color = "red")
    root.after(1000,humidity)
        
    
    
    
    
canvas = Canvas(root,width = 800, height = 500,highlightthickness = 0)

label1 = customtkinter.CTkButton(canvas, text = "",width = 100,height=50,corner_radius = 20,text_color = "gold",bg_color = "lightblue")
label1.pack(pady=20)
label1.place(x=350,y=440)
label2 = customtkinter.CTkLabel(canvas,text = "Humidity: ",text_color = "gold",bg_color = "black")
label2.pack(side = "left",anchor = "se",padx = 20)

label3 = customtkinter.CTkLabel(canvas,text = "HIGH",text_color = "red",bg_color = "black")
label3.pack(side = "left",anchor = "sw",padx = 10)
button1 = customtkinter.CTkButton(canvas, text = "Disconnect",width = 90,height=20,corner_radius = 10,text_color = "red",bg_color = "lightblue",fg_color = "white",command = disconnect)
button1.pack(side = "right",anchor = "se",pady=10)
button1.place(x=700,y=470)

label4 = customtkinter.CTkLabel(canvas,text = "Light intensity: LOW",text_color = "green",bg_color = "white")
label4.place(x=10,y=10)

button2 = customtkinter.CTkButton(canvas, text = "Connect",width = 90,height=20,corner_radius = 10,text_color = "green",bg_color = "lightblue",fg_color = "white",command = connect)
button2.pack(side = "right",anchor = "se",pady = 10)
button2.place(x=700,y=440)

button3 = customtkinter.CTkButton(canvas, text = "Weather Device Status:",width = 100,height=20,corner_radius = 10,text_color = "green",bg_color = "lightblue",fg_color = "white")
button3.pack(side = "left",anchor = "nw",padx=0)
button3.place(x=10,y=440)
clock()

humidity()
canvas.pack(fill=BOTH, expand = True)
#image inside canvas



def next1():
    
    global h,m,s
    time_h = int(h)
    time_m = int(m)
    time_s = int(s)

    if time_s <= 30:
        canvas.create_image(0,0, image=images[0],anchor = 'nw')
    elif time_s >= 30:
        canvas.create_image(0,0, image=images[1],anchor = 'nw')
        
        
    root.after(1000,next1)
next1()
        

#icon
icon = PhotoImage(file = 'icon.png')
root.iconphoto(False, icon)
#icon
icon = PhotoImage(file = 'icon.png')
root.iconphoto(False, icon)


    




root.mainloop()


