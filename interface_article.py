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
collection = database["article"]

######## Create query function ############
def article_query():
    myCursor = collection.find({})
    #cols = [["_id","title","cook_time","desc"]]
    df =pd.DataFrame(list(myCursor))
    
    top = Toplevel()
    top.title("Article_table")
    top.geometry('640x480')
    lbl = Label(top, text =df)
    lbl.pack()

######## Create insert function ############
def article_insert():
    new_record = [
        {"id" : id.get(),
         "timestamp" : timestamp.get(),
         "aid" : aid.get(),
         "title" : title.get(),
         "category" : category.get(),
         "abstract" : abstract.get(),
         "articleTags" : articleTags.get(),
         "authors" : authors.get(), 
         "language" : language.get(),
        }
    ]
    x = collection.insert_one(new_record)

######## Create update function ############
def article_update():
    new_record = [
        {"id" : id.get(),
         "timestamp" : timestamp.get(),
         "aid" : aid.get(),
         "title" : title.get(),
         "category" : category.get(),
         "abstract" : abstract.get(),
         "articleTags" : articleTags.get(),
         "authors" : authors.get(), 
         "language" : language.get(),
        }
    ]
    x = collection.update_one(new_record)
    
######## Create delete function ############
def article_delete():
    new_record = [
        {"id" : id.get(),
         "timestamp" : timestamp.get(),
         "aid" : aid.get(),
         "title" : title.get(),
         "category" : category.get(),
         "abstract" : abstract.get(),
         "articleTags" : articleTags.get(),
         "authors" : authors.get(), 
         "language" : language.get(),
        }
    ]
    x = collection.delete_one(new_record)

######## Create main window ############
window = tk.Tk()
window.geometry('640x480')
window.title('Article Table')

######### Create user query button ############
query_button = tk.Button(window, text = "Query", command = article_query)
query_button.grid(row=14,column=0,ipadx=10,pady=10,padx=10)

######### Create user insert button ############
id = tk.Entry(window, width = 30)
id.grid(row=0,column=1)
timestamp = tk.Entry(window, width = 30)
timestamp.grid(row=1,column=1)
aid = tk.Entry(window, width = 30)
aid.grid(row=2,column=1)
title = tk.Entry(window, width = 30)
title.grid(row=3,column=1)
category = tk.Entry(window, width = 30)
category.grid(row=4,column=1)
abstract = tk.Entry(window, width = 30)
abstract.grid(row=5,column=1)
articleTags = tk.Entry(window, width = 30)
articleTags.grid(row=6,column=1)
authors = tk.Entry(window, width = 30)
authors.grid(row=7,column=1)
language = tk.Entry(window, width = 30)
language.grid(row=8,column=1)


id_label = tk.Label(window, text = "id:")
id_label.grid(row=0,column=0)
timestamp_label = tk.Label(window, text = "timestamp:")
timestamp_label.grid(row=1,column=0)
aid_label = tk.Label(window, text = "aid:")
aid_label.grid(row=2,column=0)
title_label = tk.Label(window, text = "title:")
title_label.grid(row=3,column=0)
category_label = tk.Label(window, text = "category:")
category_label.grid(row=4,column=0)
abstract_label = tk.Label(window, text = "abstract:")
abstract_label.grid(row=5,column=0)
articleTags_label = tk.Label(window, text = "articleTags:")
articleTags_label.grid(row=6,column=0)
authors_label = tk.Label(window, text = "authors:")
authors_label.grid(row=7,column=0)
language_label = tk.Label(window, text = "language:")
language_label.grid(row=9,column=0)

insert_button = tk.Button(window, text = "Insert", command = article_insert)
insert_button.grid(row=14,column=1,ipadx=10,pady=10,padx=10)

######### Create user update button ############
update_button = tk.Button(window, text = "Update", command = article_update)
update_button.grid(row=14,column=2,ipadx=10,pady=10,padx=10)

######### Create user delete button ############
delete_button = tk.Button(window, text = "Delete", command = article_delete)
delete_button.grid(row=14,column=3,ipadx=10,pady=10,padx=10)

window.mainloop()