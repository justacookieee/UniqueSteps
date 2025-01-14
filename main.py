import os
from tkinter import *
from tkinter import ttk
from UniqueSteps import UniqueSteps
from dotenv import load_dotenv

### Setup
root = Tk()
root.title("Unique Steps")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
### /Setup

### Variables
url1 = StringVar()
url2 = StringVar()
name1 = StringVar()
name2 = StringVar()
sequence_type = StringVar()
output_sequences = StringVar()
### /Variables

### Functions
def get_sequences(*args):
    load_dotenv()
    urls = [url1.get(), url2.get()]
    names = [name1.get(), name2.get()]
    a = UniqueSteps(urls, names)
    username = os.getenv('OTTR_USERNAME')
    password = os.getenv('OTTR_PASS')
    a.login(username, password)
    temp = sequence_type.get()
    a.get_sequences(0)
    a.get_sequences(1)
    a.close_driver()
    print('Passed:')
    print(a.passed)
    print('Failed:')
    print(a.failed)
    print('Not Applicable:')
    print(a.na)
    print("Not Executed")
    print(a.ne)
    print("In Progress")
    print(a.ip)

### /Functions

### Logic
main_frame = ttk.Frame(root, padding="3 3 12 12")
main_frame.grid(column=0, row=0, sticky=(N,S,E,W))

url1_frame = ttk.Frame(main_frame)
url1_frame.grid(column=1, row=1, sticky=(N,S,E,W))

url2_frame = ttk.Frame(main_frame)
url2_frame.grid(column=1, row=2, sticky=(N,S,E,W))

ttk.Label(main_frame, text="First URL: ").grid(column=0, row=1, sticky=W)
ttk.Label(main_frame, text="Second URL: ").grid(column=0, row=2, sticky=W)

url1.set('https://ottr.opentext.com/test_run/execute/14267484')
url1_input = ttk.Entry(url1_frame, width=50, textvariable=url1)
url1_input.grid(column=1, row=0, sticky=W)
name1.set('London')
ttk.Entry(url1_frame, textvariable=name1).grid(column=0, row=0, sticky=W)
url2.set('https://ottr.opentext.com/test_run/execute/14267538')
url2_input = ttk.Entry(url2_frame, width=50, textvariable=url2)
url2_input.grid(column=1, row=0, sticky=W)
name2.set('Singapore')
ttk.Entry(url2_frame, textvariable=name2).grid(column=0, row=0, sticky=W)

radio_frame = ttk.Frame(main_frame)
radio_frame.grid(column=1,row=3, sticky=(N,S,E,W))

failed = ttk.Radiobutton(radio_frame, text='Failed', variable=sequence_type, value='f')
passed = ttk.Radiobutton(radio_frame, text='Passed', variable=sequence_type, value='p')
in_progress = ttk.Radiobutton(radio_frame, text='In Progress', variable=sequence_type, value='ip')
not_applicable = ttk.Radiobutton(radio_frame, text='NA', variable=sequence_type, value='na')
sequence_type.set('f')

failed.grid(column=0,row=0, sticky=W)
passed.grid(column=1,row=0, sticky=W)
in_progress.grid(column=2,row=0, sticky=W)
not_applicable.grid(column=3,row=0, sticky=W)


ttk.Button(main_frame, text='Enter', command=get_sequences).grid(column=1, row=4, sticky=(N,S,E,W))
### /Logic

### Run root
root.mainloop()
### /Run root
