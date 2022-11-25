import tkinter as tk

window = tk.Tk()

window.rowconfigure(0, minsize=500)
window.geometry("600x300+1000+500")

frame1 = tk.Frame(master=window, width=300, height=200, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()