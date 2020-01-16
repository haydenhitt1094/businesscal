transactions = []
description = []
amount_sales = []
receipt_list = []

def BuildReceipt(descrip,index):
    newdes = descrip.title()
    newamount = amount_sales[i]
    if transactions[i] == str('1'):
        typeof = 'Business Expense'
    else:
        typeof = 'Raw Sale Revenue'
    recepit = "\n----------------------------\n{}\n${}\n{}\n---------------------".format(newdes,newamount,typeof)
    return recepit
    

with open("H:\\company stuff\Quarter 1 2020 purchases.txt") as file:
    for line in file:
        line=line.strip()
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
file.close()


profit = 0 


for i in range(len(transactions)):
    try:
        page = BuildReceipt(description[i],i)
        print(page)
    except IndexError:
        pass
    if transactions[i] == str('1'):
        profit = profit - amount_sales[i]
    elif transactions[i] == str('0'):
        profit = profit + amount_sales[i]
    else:
        pass


print("\n\n\nProfit Total: ${}".format(profit))


#Copyright 2020 Fungal Functions Technology Corp.
