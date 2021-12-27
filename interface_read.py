import tkinter as tk
import pymongo
import pprint
import pandas as pd

from tkinter import *
from pymongo import MongoClient
from pandas import DataFrame

######## Connect to database ############
client = MongoClient(host="localhost", port=27017)
database = client['cooker']
collection = database["read"]

######## Create query function ############
def read_query():
    myCursor = collection.find({})
    #cols = [["_id","title","cook_time","desc"]]
    df =pd.DataFrame(list(myCursor))
    
    top = Toplevel()
    top.title("Read_table")
    top.geometry('640x480')
    lbl = Label(top, text =df)
    lbl.pack()

######## Create insert function ############
def read_insert():
    new_record = [
        {"id" : id.get(),
         "timestamp" : timestamp.get(),
         "uid" : uid.get(),
         "aid" : aid.get(),
         "readTimeLength" : readTimeLength.get(),
         "agreeOrNot" : agreeOrNot.get(),
         "commentOrNot" : commentOrNot.get(),
         "shareOrNot" : shareOrNot.get(),
         "commentDetail" : commentDetail.get(), 
         "region" : region.get(),
        }
    ]
    x = collection.insert_one(new_record)

######## Create update function ############
def read_update():
    new_record = [
        {"id" : id.get(),
         "timestamp" : timestamp.get(),
         "uid" : uid.get(),
         "aid" : aid.get(),
         "readTimeLength" : readTimeLength.get(),
         "agreeOrNot" : agreeOrNot.get(),
         "commentOrNot" : commentOrNot.get(),
         "shareOrNot" : shareOrNot.get(),
         "commentDetail" : commentDetail.get(), 
         "region" : region.get(),
        }
    ]
    x = collection.update_one(new_record)
    
######## Create delete function ############
def read_delete():
    new_record = [
        {"id" : id.get(),
         "timestamp" : timestamp.get(),
         "uid" : uid.get(),
         "aid" : aid.get(),
         "readTimeLength" : readTimeLength.get(),
         "agreeOrNot" : agreeOrNot.get(),
         "commentOrNot" : commentOrNot.get(),
         "shareOrNot" : shareOrNot.get(),
         "commentDetail" : commentDetail.get(), 
         "region" : region.get(),
        }
    ]
    x = collection.delete_one(new_record)

######## Create main window ############
window = tk.Tk()
window.geometry('640x480')
window.title('Read Table')

######### Create user query button ############
query_button = tk.Button(window, text = "Query", command = read_query)
query_button.grid(row=14,column=0,ipadx=10,pady=10,padx=10)

######### Create user insert button ############
id = tk.Entry(window, width = 30)
id.grid(row=0,column=1)
timestamp = tk.Entry(window, width = 30)
timestamp.grid(row=1,column=1)
uid = tk.Entry(window, width = 30)
uid.grid(row=2,column=1)
aid = tk.Entry(window, width = 30)
aid.grid(row=3,column=1)
readTimeLength = tk.Entry(window, width = 30)
readTimeLength.grid(row=4,column=1)
agreeOrNot = tk.Entry(window, width = 30)
agreeOrNot.grid(row=5,column=1)
commentOrNot = tk.Entry(window, width = 30)
commentOrNot.grid(row=6,column=1)
shareOrNot = tk.Entry(window, width = 30)
shareOrNot.grid(row=7,column=1)
commentDetail = tk.Entry(window, width = 30)
commentDetail.grid(row=8,column=1)
region = tk.Entry(window, width = 30)
region.grid(row=9,column=1)


id_label = tk.Label(window, text = "id:")
id_label.grid(row=0,column=0)
timestamp_label = tk.Label(window, text = "timestamp:")
timestamp_label.grid(row=1,column=0)

uid_label = tk.Label(window, text = "uid:")
uid_label.grid(row=2,column=0)
aid_label = tk.Label(window, text = "aid:")
aid_label.grid(row=3,column=0)
readTimeLength_label = tk.Label(window, text = "readTimeLength:")
readTimeLength_label.grid(row=4,column=0)
agreeOrNot_label = tk.Label(window, text = "agreeOrNot:")
agreeOrNot_label.grid(row=5,column=0)
commentOrNot_label = tk.Label(window, text = "commentOrNot:")
commentOrNot_label.grid(row=6,column=0)
shareOrNot_label = tk.Label(window, text = "shareOrNot:")
shareOrNot_label.grid(row=7,column=0)
commentDetail_label = tk.Label(window, text = "commentDetail:")
commentDetail_label.grid(row=8,column=0)
region_label = tk.Label(window, text = "region:")
region_label.grid(row=9,column=0)

insert_button = tk.Button(window, text = "Insert", command = read_insert)
insert_button.grid(row=14,column=1,ipadx=10,pady=10,padx=10)

######### Create user update button ############
update_button = tk.Button(window, text = "Update", command = read_update)
update_button.grid(row=14,column=2,ipadx=10,pady=10,padx=10)

######### Create user delete button ############
delete_button = tk.Button(window, text = "Delete", command = read_delete)
delete_button.grid(row=14,column=3,ipadx=10,pady=10,padx=10)

window.mainloop()