#Inventory (Sport Equipments)
from tkinter import *

Inventory = {"Ball" : {"brand" : "Adidas", "price" : "400", "stock" : "2"}}

def create_item (name, brand, price, stock):
    Inventory[name] = {'brand' : brand, 'price': price, 'stock' : stock}
    result_label.config (text = f"Item {name} created with brand {brand}, price {price}, and stock {stock}")

def read_item (name, brand, price, stock):
    if name in Inventory:
        for name, details in Inventory.items ():
            result_label.config (text = f"Item: {name}\nBrand: {Inventory [name]['brand']}\nPrice: {Inventory [name]['price']}\nStock: {Inventory [name]['stock']}")
    else:
        result_label.config (text = f"Item is not found in inventory.")

def update_item (name, stock, price):
    if name in Inventory:
       Inventory[name]['stock'] += stock
    if name in Inventory:
       Inventory[name]['price'] += price
       result_label.config (text = f"Updated stock for {name}. New stock: {Inventory [name] ['stock']}\nUpdated price for {name}. New price: {Inventory [name]['price']}")
    else:
        result_label.config (text = f"Item {name} not found in inventory.")

def delete_item (name):
    if name in Inventory:
        del Inventory [name]
        result_label.config (text = f"Item{name} has been deleted from inventory.")
    else:
        result_label.config(text = f"Item {name} is not found in inventory.")

#GUI
def create_item_gui ():
    name = Item_name_entry.get ()
    brand = Brand_entry.get ()
    try:
        price = float (Price_entry.get())
        stock = int (Stock_entry.get())
        create_item (name, brand, price, stock)
    except ValueError:
        result_label.config (text = "Please enter valid price and stock values.")

def read_item_gui ():
    name = Item_name_entry.get ()
    brand = Brand_entry.get ()
    try:
        price = float (Price_entry.get())
        stock = int (Stock_entry.get())
        read_item (name, brand, price, stock)
    except ValueError:
        result_label.config (text = "Please enter valid price and stock values.")

def update_item_gui ():
    name = Item_name_entry.get ()
    try:
        stock = int (Stock_entry.get())
        price = float (Price_entry.get())
        update_item (name, stock, price)
    except ValueError:
        result_label.config (text = "Please enter a valid stock and price value.")

def delete_item_gui ():
    Item_name_entry.delete (0, END )
    Brand_entry.delete (0, END)
    Price_entry.delete (0, END)
    Stock_entry.delete (0, END)
    result_label.config (text = f"Item has been deleted")

#Main Window
root = Tk ()
root.title ("Sport Equipments")

#Widgets
Item_name_label = Label (root, text = "Item Name:")
Item_name_label.grid (row =0, column =0)
Item_name_entry = Entry (root)
Item_name_entry.grid (row =0, column =1 )

Brand_label = Label (root, text = "Brand:")
Brand_label.grid (row =1, column =0 )
Brand_entry = Entry (root)
Brand_entry.grid (row =1, column =1)

Price_label = Label (root, text = "Price:")
Price_label.grid (row =2, column =0)
Price_entry = Entry (root)
Price_entry.grid (row =2, column =1)

Stock_label = Label (root, text = "Stock:")
Stock_label.grid (row =3, column =0)
Stock_entry = Entry (root)
Stock_entry.grid (row =3, column =1)

#Result display
result_label = Label (root, text = "", fg = "Purple")
result_label.grid (row =6, column =0, columnspan =2)

#Buttons
create_button = Button (root, text = "Create Item", command = create_item_gui)
create_button.grid (row =4, column = 0)

read_button = Button (root, text = "Read Item", command = read_item_gui )
read_button.grid (row = 4, column =1)

update_button = Button (root, text = "Update Item", command = update_item_gui )
update_button.grid (row =5, column =0)

delete_button = Button (root, text = "Delete Item", command = delete_item_gui)
delete_button.grid (row =5, column =1)

#Start Main Loop
root.mainloop()