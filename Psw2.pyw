#!/usr/bin/python

# ADD ID AND PASSWORD LABEL
# Create dictionnary with name of the site on key an tuple with ID ans password as value


import tkinter as tk
import random
import json
import pyperclip


global passwordDic

with open("save.json",'r') as f:
	passwordDic = json.loads(f.read())



# Return new password in Entry
def generatePassword():
	size = lenVar.get()
	isMaj = majVar.get()
	isLow = lowVar.get()
	isSymb = symbVar.get()
	isInt = intVar.get()

	i = 0
	password = str()
	char = ""
	numeric = [chr(x) for x in range(48,57)]
	alphMaj = [chr(x) for x in range(65,90)]
	alphMin = [chr(x) for x in range(97,122)]
	symbol = [chr(x) for x in range(33,47)]
	# Possible char contains in tab inside everything
	everything = []
	
	# What do we use to make the password
	if not isMaj and not isInt and not isSymb:
		everything.append(alphMin)

	if isMaj:
		everything.append(alphMaj)

	if isLow:
		everything.append(alphMin)

	if isInt:
		everything.append(numeric)
		
	if isSymb:
		everything.append(symbol)


	everySize = len(everything) -1
	while i < size:
		# Choose tab related to Checkbutton option
		typeOfChar = everything[random.randint(0,everySize)]
		# Get size of this tab
		typeOfCharSize = len(typeOfChar) -1
		# Choose one of the tab's char
		char = typeOfChar[random.randint(0,typeOfCharSize)]
		# Add it to password
		password += str(char)
		i += 1

	Entry.delete(0, last=tk.END)
	Entry.insert('insert', password)

def save_modification(dic):
	with open("save.json",'w+') as jsave:
		jsave.write(json.dumps(dic))

def add_to_list():
	global IDentry, password, newWindow
	# Get listbox ID name
	name = IDentry.get()

	# Save ID and Password in dic
	passwordDic[name] = password

	# Display name on listbox
	displayer.insert(tk.END, name)

	save_modification(passwordDic)

	# Close this window
	newWindow.destroy()

def save_password():
	global IDentry, password, newWindow
	newWindow = tk.Toplevel()
	newWindow.geometry("160x27+300+300")
	newWindow.title('Add new password')

	password = Entry.get()
	IDentry = tk.Entry(newWindow, width=20)

	addButton = tk.Button(newWindow, text='Add', command = add_to_list)

	IDentry.grid(row=0,column=0, sticky='W')
	addButton.grid(row=0,column=1,sticky='W')


def get_password(event):
	Entry.delete(0, last=tk.END)
	Entry.insert('insert', passwordDic[displayer.get(displayer.curselection())])

def del_display():
	passwordDic.pop(displayer.get(displayer.curselection()), None)
	displayer.delete(displayer.curselection())
	save_modification(passwordDic)

app = tk.Tk()
app.title('Password Manager')
app.geometry("550x150+250+250")

# ID Display
displayer = tk.Listbox(app, width=50, height=9)
displayer.bind("<<ListboxSelect>>", get_password)

for keys in passwordDic.keys():
	displayer.insert(tk.END, keys)

# Generate password button
generateButton = tk.Button(app,text="Generate",command = generatePassword)

# Display the created password
Entry = tk.Entry(app, width=10)

# Delete listbox entry and password
dltButton = tk.Button(app, text='delete', command = del_display)

# Copy to clipBoard
copyButton = tk.Button(app,text="copy", command=lambda:pyperclip.copy(Entry.get()))

# Size of the password
passwordLen = [x for x in range(1,21)]
lenVar = tk.IntVar()
lenVar.set(8)
lenOption = tk.OptionMenu(app, lenVar,*passwordLen)

# Password contain uppercase ?
majVar =  tk.IntVar()
majVar.set(0)
checkMaj = tk.Checkbutton(app, text = 'Maj', variable=majVar)

# Password contain lowercase ?
lowVar = tk.IntVar()
lowVar.set(0)
checkLow = tk.Checkbutton(app, text='Min', variable=lowVar)

# Password contain symbol ?
symbVar = tk.IntVar()
symbVar.set(0)
checkSymb = tk.Checkbutton(app, text='Symbol', variable=symbVar)

# Password contain integer ?
intVar = tk.IntVar()
intVar.set(0)
checkInt = tk.Checkbutton(app, text='Number', variable=intVar)

# Save password in list
savePassword = tk.Button(app, text='save', command=save_password)

# GRID ZONE
displayer.grid(row=0,column=6,rowspan=3, sticky='NS')
Entry.grid(row=0,column=0,columnspan=3,sticky="EW")
generateButton.grid(row=0,column=3, sticky='W')
lenOption.grid(row=0,column=4,sticky='W')

savePassword.grid(row=1,column=0, sticky='W')
dltButton.grid(row=1,column=1, sticky="W")
copyButton.grid(row=1,column=2, sticky="W")

checkMaj.grid(row=2,column=0,sticky='N')
checkLow.grid(row=2, column=1,sticky='N')
checkSymb.grid(row=2,column=2,sticky='N')
checkInt.grid(row=2,column=3,sticky='N')

app.mainloop()
