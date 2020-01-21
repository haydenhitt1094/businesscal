import tkinter as gui
import sqlite3
import os as system
from time import sleep

sourceloc = system.path.dirname(system.path.abspath(__file__))
packagespath = sourceloc +str(r'\salesdata.db')
system.chdir(sourceloc)

root = gui.Tk()
root.title("Profit Track")
root.geometry("500x500")

def getData():
    mastercolumn.delete(0,gui.END)
    #mastercolumn = gui.Listbox(master=root,width=100)
    conn = sqlite3.connect(packagespath)
    curs = conn.cursor()
    curs.execute("SELECT * FROM sales")
    data = curs.fetchall()

    profit = None
    profit = 0

    for i in range(len(data)):
        band = data[i]
        transtypedb = band[0]
        itemtypedb = band[1]
        costdb = band[2]
        if transtypedb == str('Purchase'):
            profit = profit - float(costdb)
        elif transtypedb == str('Sale'):
            profit = profit + float(costdb)
        else:
            pass
        mastercolumn.insert(i,"{0:-^50}{1:-^50}${2:-<20}".format(transtypedb,itemtypedb,costdb))
    profitis = "Total Profit:"
    mastercolumn.insert(i+1,"{} ${}".format(profitis,profit))
    conn.close()



def dataPull():
    if label.winfo_ismapped():
        seebtn['text'] = 'Return'
        getData()
        
        label.grid_forget()
        exitbtn.grid_forget()
        addbtn.grid_forget()
        mastercolumn.grid(row=0,column=0)
        seebtn.grid()

    else:
        seebtn['text']= 'View receipts'
        mastercolumn.grid_forget()
        seebtn.grid(row=1)
        label.grid(row=0)
        exitbtn.grid(row=3)
        addbtn.grid(row=2)

        
     
def Submit():
    transadd = addtype.get()
    itemtypenew = additemtype.get()
    newcost = addcost.get()
    if transadd == '' or itemtypenew == '' or newcost == '':
        errorlabel.grid(column=0,row=6)
        errorlabel.grid_forget()
    else:
        addconn = sqlite3.connect(packagespath)
        addcurs = addconn.cursor()
        a = addtype.get()
        b = additemtype.get()
        c = addcost.get()
        add_tuple = tuple((str(a),str(b),str(c)))
        addcurs.execute('INSERT INTO sales VALUES (?,?,?)',add_tuple)
        addconn.commit()
        addcurs.close()
        errorlabel.grid_forget()
        successlabel.grid(column=0,row=5)
        

        
    
def newWindow():
    if label.winfo_ismapped():
        addbtn['text'] = 'Return'
        successlabel.grid_forget()
        exitbtn.grid_forget()
        label.grid_forget()
        addbtn.grid(row=5,column=1,columnspan=2)
        seebtn.grid_forget()
        additemsubmit.grid(column=1,row=4)
        addtype.grid(column=1,row=3)
        addcost.grid(column=1,row=1)
        additemtype.grid(column=1,row=2)
        labelt.grid(row=3,column=0)
        labelc.grid(row=1,column=0)
        labeld.grid(row=2,column=0)
        
    else:
        addbtn['text'] = 'Add a new item to database'
        exitbtn.grid()
        seebtn.grid()
        label.grid(row=0)
        labelc.grid_forget()
        labeld.grid_forget()
        labelt.grid_forget()
        addtype.grid_forget()
        addcost.grid_forget()
        additemtype.grid_forget()
        additemsubmit.grid_forget()
        successlabel.grid_forget()
        addbtn.grid(row=1,column=0)


#Formatting
exitbtn = gui.Button(master=root, text="Exit", command=root.destroy,width=50,height=1)
exitbtn.grid(row=3, column=0)

addbtn = gui.Button(master=root,text="Add a new item to databse",command=newWindow,width=50,height=1)
addbtn.grid(row=2)

label = gui.Label(master=root, text ='Choose an action...')
label.grid(row=0)

seebtn=gui.Button(master=root, text="View reciepts",command=dataPull, width=50)
seebtn.grid(row=1)


addtype = gui.Entry(master=root,width=50)
additemtype = gui.Entry(master=root,width=50)
addcost = gui.Entry(master=root,width=50)

labelt = gui.Label(master=root,text="Transaction type:")
labelc = gui.Label(master=root,text="Item Cost:")
labeld = gui.Label(master=root,text="Item Description:")

additemsubmit=gui.Button(master=root,command=Submit,text="Submit",width=50)

errorlabel = gui.Label(master=root, text="Error invalid input")
successlabel = gui.Label(master=root,text="Success") 

mastercolumn = gui.Listbox(master=root,width=100)



#Copyright 2020 Fungal Functions Technology Corp.
root.mainloop()