import tkinter as gui

root = gui.Tk()
root.title("Profit Track")

def dataPull():
    if label.winfo_ismapped():
        seebtn['text'] = 'Return'
        label.grid_forget()
        column1.grid(row=5)
    else:
        seebtn['text']= 'View receipts'
        column1.grid_forget()
        label.grid()
        
        

transactions = []
description = []
amount_sales = []

def newWindow():
    if label.winfo_ismapped():
        addbtn['text'] = 'Return'
        exitbtn.grid_forget()
        label.grid_forget()
        seebtn.grid_forget()
    else:
        addbtn['text'] = 'Add a new item to database'
        exitbtn.grid()
        seebtn.grid()
        label.grid(row=0)


exitbtn = gui.Button(master=root, text="Exit", command=root.destroy,width=200,height=1)
exitbtn.grid(row=1, column=0)

addbtn = gui.Button(master=root,text="Add a new item to databse",command=newWindow,width=200,height=1)
addbtn.grid(row=2)

label = gui.Label(master=root, text ='Choose an action...')
label.grid(row=0)

seebtn=gui.Button(master=root, text="View reciepts",command=dataPull, width=200)
seebtn.grid(row=3)

indexof=1
        
for line in open(r'C:\Users\hayde\Documents\GitHubReps\businesscal\Quarter 1 2020 purchases.txt','r'):
    try:
        trans_attrs = line.split(",")
        trans_type = trans_attrs[0]
        transactions.append(trans_type)
        descrip = trans_attrs[1]
        description.append(descrip)
        amount = float(trans_attrs[2])
        amount_sales.append(amount)
    except IndexError:
        pass
column1=gui.Listbox(master=root)
for transaction in transactions:
    if transaction == 1:
        column1.insert(indexof,'Purchase')
    else:
        column1.insert(indexof,'Sale')
    indexof=indexof+1
     


root.mainloop()