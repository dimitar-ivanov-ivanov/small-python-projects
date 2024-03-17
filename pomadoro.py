import os
import sys
from threading import Timer
import tkinter as tk
import webbrowser

def message():
    popup = tk.Tk()
    popup.title("Notification")
    label = tk.Label(popup, text="Pomadoro timer is over!")
    label.pack(padx=20, pady=10)
    
    def close():
        popup.destroy() 

    def restart():
        os.execl(sys.executable, sys.executable, *sys.argv)     

        
    button = tk.Button(popup, text="Continue", command=restart)
    button.pack(pady=10)

    button2 = tk.Button(popup, text='Close', command=close)
    button2.pack(pady=11)

    popup.mainloop()

# Delay the notification by 25 minutes
t = Timer(25*60, message)
t.start()