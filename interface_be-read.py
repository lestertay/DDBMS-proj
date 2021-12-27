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
collection = database["be-read"]

######## Create query function ############
def beread_query():
    myCursor = collection.find({})
    #cols = [["_id","title","cook_time","desc"]]
    df =pd.DataFrame(list(myCursor))
    
    top = Toplevel()
    top.title("Be-read_table")
    top.geometry('640x480')
    lbl = Label(top, text =df)
    lbl.pack()

######## Create insert function ############
def beread_insert():
    new_record = [
        {"id" : id.get(),
         "timestamp" : timestamp.get(),
         "aid" : aid.get(),
         "category" : category.get(),
         "readNum" : readNum.get(),
         "readUidList" : readUidList.get(),
         "commentNum" : commentNum.get(),
         "commentUidList" : commentUidList.get(), 
         "agreeNum" : agreeNum.get(),
         "shareNum" : shareNum.get(),
         "shareUidList" : shareUidList.get(), 
        }
    ]
    x = collection.insert_one(new_record)

######## Create update function ############
def beread_update():
    new_record = [
        {"id" : id.get(),
         "timestamp" : timestamp.get(),
         "aid" : aid.get(),
         "category" : category.get(),
         "readNum" : readNum.get(),
         "readUidList" : readUidList.get(),
         "commentNum" : commentNum.get(),
         "commentUidList" : commentUidList.get(), 
         "agreeNum" : agreeNum.get(),
         "shareNum" : shareNum.get(),
         "shareUidList" : shareUidList.get(), 
        }
    ]
    x = collection.update_one(new_record)
    
######## Create delete function ############
def beread_delete():
    new_record = [
        {"id" : id.get(),
         "timestamp" : timestamp.get(),
         "aid" : aid.get(),
         "category" : category.get(),
         "readNum" : readNum.get(),
         "readUidList" : readUidList.get(),
         "commentNum" : commentNum.get(),
         "commentUidList" : commentUidList.get(), 
         "agreeNum" : agreeNum.get(),
         "shareNum" : shareNum.get(),
         "shareUidList" : shareUidList.get(), 
        }
    ]
    x = collection.delete_one(new_record)

######## Create main window ############
window = tk.Tk()
window.geometry('640x480')
window.title('Be-read Table')

######### Create user query button ############
query_button = tk.Button(window, text = "Query", command = beread_query)
query_button.grid(row=14,column=0,ipadx=10,pady=10,padx=10)

######### Create user insert button ############
id = tk.Entry(window, width = 30)
id.grid(row=0,column=1)
timestamp = tk.Entry(window, width = 30)
timestamp.grid(row=1,column=1)
aid = tk.Entry(window, width = 30)
aid.grid(row=2,column=1)
category = tk.Entry(window, width = 30)
category.grid(row=3,column=1)
readNum = tk.Entry(window, width = 30)
readNum.grid(row=4,column=1)
readUidList = tk.Entry(window, width = 30)
readUidList.grid(row=5,column=1)
commentNum = tk.Entry(window, width = 30)
commentNum.grid(row=6,column=1)
commentUidList = tk.Entry(window, width = 30)
commentUidList.grid(row=7,column=1)
agreeNum = tk.Entry(window, width = 30)
agreeNum.grid(row=8,column=1)
shareNum = tk.Entry(window, width = 30)
shareNum.grid(row=9,column=1)
shareUidList = tk.Entry(window, width = 30)
shareUidList.grid(row=10,column=1)


id_label = tk.Label(window, text = "id:")
id_label.grid(row=0,column=0)
timestamp_label = tk.Label(window, text = "timestamp:")
timestamp_label.grid(row=1,column=0)
aid_label = tk.Label(window, text = "aid:")
aid_label.grid(row=2,column=0)
category_label = tk.Label(window, text = "category:")
category_label.grid(row=3,column=0)
readNum_label = tk.Label(window, text = "readNum:")
readNum_label.grid(row=4,column=0)
readUidList_label = tk.Label(window, text = "readUidList:")
readUidList_label.grid(row=5,column=0)
commentNum_label = tk.Label(window, text = "commentNum:")
commentNum_label.grid(row=6,column=0)
commentUidList_label = tk.Label(window, text = "commentUidList:")
commentUidList_label.grid(row=7,column=0)
agreeNum_label = tk.Label(window, text = "agreeNum:")
agreeNum_label.grid(row=8,column=0)
shareNum_label = tk.Label(window, text = "shareNum:")
shareNum_label.grid(row=9,column=0)
shareUidList_label = tk.Label(window, text = "shareUidList:")
shareUidList_label.grid(row=10,column=0)

insert_button = tk.Button(window, text = "Insert", command = beread_insert)
insert_button.grid(row=14,column=1,ipadx=10,pady=10,padx=10)

######### Create user update button ############
update_button = tk.Button(window, text = "Update", command = beread_update)
update_button.grid(row=14,column=2,ipadx=10,pady=10,padx=10)

######### Create user delete button ############
delete_button = tk.Button(window, text = "Delete", command = beread_delete)
delete_button.grid(row=14,column=3,ipadx=10,pady=10,padx=10)

window.mainloop()