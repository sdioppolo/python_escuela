from tkinter import *
from tkinter import ttk

myApp = Tk()
myApp.title(" Program ")                         
myApp.geometry("200x200")


tree = ttk.Treeview(myApp,height=25)
tree['show'] = 'headings'

sbv = ttk.Scrollbar(myApp, orient="vertical", command=tree.yview)
sbv.grid(row=1,column=1,sticky="NS",pady=5)

tree.configure(yscrollcommand=sbv.set)

sbh = ttk.Scrollbar(myApp, orient="horizontal", command=tree.xview)
sbh.grid(row=2,column=0,sticky="WE",pady=5)

tree.configure(xscrollcommand=sbh.set)

tree["columns"]=("1","2","3")

tree.column("1", width=50)
tree.column("2", width=50)
tree.column("3", width=50)

tree.heading("1", text="Col 1")
tree.heading("2", text="Col 2")
tree.heading("3", text="Col 3")

tree.insert("", "end", values=("a",),)
tree.insert("", "end", values=("b",), tag='gray')
tree.insert("", "end", values=("c",),)
tree.insert("", "end", values=("d",), tag='gray')
tree.tag_configure('gray', background='#cccccc')

tree.grid(row=1,column=0,padx=5,pady=5)

myApp.mainloop()
