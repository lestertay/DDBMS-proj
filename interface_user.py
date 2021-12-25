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
collection = database["recipes"]

######## Create query function ############
def user_query():
    myCursor = collection.find({})
    #cols = [["_id","title","cook_time","desc"]]
    df =pd.DataFrame(list(myCursor))
    
    top = Toplevel()
    top.title("User_table")
    top.geometry('640x480')
    lbl = Label(top, text =df)
    lbl.pack()

######## Create insert function ############
def user_insert():
    new_record = [
        {"id" : id.get(),
         "timestamp" : timestamp.get(),
         "uid" : uid.get(),
         "name" : name.get(),
         "gender" : gender.get(),
         "email" : email.get(),
         "phone" : phone.get(),
         "dept" : dept.get(), 
         "grade" : grade.get(),
         "language" : language.get(),
         "region" : region.get(),
         "role" : role.get(),
         "preferTags" : preferTags.get(),
         "obtainedCredits" : obtainedCredits.get() 
        }
    ]
    x = collection.insert_one(new_record)

######## Create update function ############
def user_update():
    new_record = [
        {"id" : id.get(),
         "timestamp" : timestamp.get(),
         "uid" : uid.get(),
         "name" : name.get(),
         "gender" : gender.get(),
         "email" : email.get(),
         "phone" : phone.get(),
         "dept" : dept.get(), 
         "grade" : grade.get(),
         "language" : language.get(),
         "region" : region.get(),
         "role" : role.get(),
         "preferTags" : preferTags.get(),
         "obtainedCredits" : obtainedCredits.get() 
        }
    ]
    x = collection.update_one(new_record)
    
######## Create delete function ############
def user_delete():
    new_record = [
        {"id" : id.get(),
         "timestamp" : timestamp.get(),
         "uid" : uid.get(),
         "name" : name.get(),
         "gender" : gender.get(),
         "email" : email.get(),
         "phone" : phone.get(),
         "dept" : dept.get(), 
         "grade" : grade.get(),
         "language" : language.get(),
         "region" : region.get(),
         "role" : role.get(),
         "preferTags" : preferTags.get(),
         "obtainedCredits" : obtainedCredits.get() 
        }
    ]
    x = collection.delete_one(new_record)

######## Create main window ############
window = tk.Tk()
window.geometry('640x480')
window.title('User Table')

######### Create user query button ############
user_button = tk.Button(window, text = "Query", command = user_query)
user_button.grid(row=14,column=0,ipadx=10,pady=10,padx=10)

######### Create user insert button ############
id = tk.Entry(window, width = 30)
id.grid(row=0,column=1)
timestamp = tk.Entry(window, width = 30)
timestamp.grid(row=1,column=1)
uid = tk.Entry(window, width = 30)
uid.grid(row=2,column=1)
name = tk.Entry(window, width = 30)
name.grid(row=3,column=1)
gender = tk.Entry(window, width = 30)
gender.grid(row=4,column=1)
email = tk.Entry(window, width = 30)
email.grid(row=5,column=1)
phone = tk.Entry(window, width = 30)
phone.grid(row=6,column=1)
dept = tk.Entry(window, width = 30)
dept.grid(row=7,column=1)
grade = tk.Entry(window, width = 30)
grade.grid(row=8,column=1)
language = tk.Entry(window, width = 30)
language.grid(row=9,column=1)
region = tk.Entry(window, width = 30)
region.grid(row=10,column=1)
role = tk.Entry(window, width = 30)
role.grid(row=11,column=1)
preferTags = tk.Entry(window, width = 30)
preferTags.grid(row=12,column=1)
obtainedCredits = tk.Entry(window, width = 30)
obtainedCredits.grid(row=13,column=1)

id_label = tk.Label(window, text = "id:")
id_label.grid(row=0,column=0)
timestamp_label = tk.Label(window, text = "timestamp:")
timestamp_label.grid(row=1,column=0)
uid_label = tk.Label(window, text = "uid:")
uid_label.grid(row=2,column=0)
name_label = tk.Label(window, text = "name:")
name_label.grid(row=3,column=0)
gender_label = tk.Label(window, text = "gender:")
gender_label.grid(row=4,column=0)
email_label = tk.Label(window, text = "email:")
email_label.grid(row=5,column=0)
phone_label = tk.Label(window, text = "phone:")
phone_label.grid(row=6,column=0)
dept_label = tk.Label(window, text = "dept:")
dept_label.grid(row=7,column=0)
grade_label = tk.Label(window, text = "grade:")
grade_label.grid(row=8,column=0)
language_label = tk.Label(window, text = "language:")
language_label.grid(row=9,column=0)
region_label = tk.Label(window, text = "region:")
region_label.grid(row=10,column=0)
role_label = tk.Label(window, text = "role:")
role_label.grid(row=11,column=0)
preferTags_label = tk.Label(window, text = "preferTags:")
preferTags_label.grid(row=12,column=0)
obtainedCredits_label = tk.Label(window, text = "obtainedCredits:")
obtainedCredits_label.grid(row=13,column=0)

insert_button = tk.Button(window, text = "Insert", command = user_insert)
insert_button.grid(row=14,column=1,ipadx=10,pady=10,padx=10)

######### Create user update button ############
user_button = tk.Button(window, text = "Update", command = user_update)
user_button.grid(row=14,column=2,ipadx=10,pady=10,padx=10)

######### Create user delete button ############
user_button = tk.Button(window, text = "Delete", command = user_delete)
user_button.grid(row=14,column=3,ipadx=10,pady=10,padx=10)

window.mainloop()

