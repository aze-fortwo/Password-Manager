#!/usr/bin/python

# ADD ID AND PASSWORD LABEL
# Create dictionnary with name of the site on key an tuple with ID ans password as value


import tkinter as tk
import random

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

	everything = [numeric, symbol, alphMaj, alphMin]

	while i < size:
		if isMaj and isSymb and isInt and isLow:
			char = random.choice(everything[random.choice((0,1,2,3))])

		elif isMaj and isSymb and isInt and not isLow:
			char = random.choice(everything[random.choice((0,1,2))])

		elif isMaj and isSymb and not isInt and not isLow:
			char = random.choice(everything[random.choice((1,2))])

		elif isMaj and not isSymb and not isInt and not isLow:
			char = random.choice(everything[2])

		elif isMaj and isSymb and not isInt and isLow:
			char = random.choice(everything[random.choice((1,2,3))])

		elif isMaj and not isSymb and isInt and isLow:
			char = random.choice(everything[random.choice((0,2,3))])

		elif isMaj and not isSymb and isInt and not isLow:
			char = random.choice(everything[random.choice((0,2))])

		elif not isMaj and isSymb and not isInt and not isLow:
			char = random.choice(everything[1])

		elif not isMaj and not isSymb and isInt and not isLow:
			char = random.choice(everything[0])

		elif not isMaj and isSymb and isInt and not isLow:
			char = random.choice(everything[random.choice((0,1))])

		elif not isMaj and isSymb and isInt and isLow:
			char = random.choice(everything[random.choice((0,1,3))])

		elif not isMaj and not isSymb and isInt and isLow:
			char = random.choice(everything[random.choice((0,3))])

		elif not isMaj and isSymb and not isInt and isLow:
			char = random.choice(everything[random.choice((1,3))])


		else:
			char = random.choice(everything[3])

		password += str(char)
		i += 1

	Entry.delete(0, last=tk.END)
	Entry.insert('insert', password)

app = tk.Tk()
app.title('Password Manager')

displayer = tk.Listbox(app)


# Generate password button
generateButton = tk.Button(app,text="Generate",command = generatePassword)

# Display the created password
Entry = tk.Entry(app, width=10)

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

# Size of the password
passwordLen = [x for x in range(1,21)]
lenVar = tk.IntVar()
lenVar.set(8)
lenOption = tk.OptionMenu(app, lenVar,*passwordLen)


# GRID ZONE
displayer.grid(row=0,column=6,rowspan=3, sticky='NSEW')
Entry.grid(row=0,column=0,columnspan=3,sticky="EW")
generateButton.grid(row=0,column=3, sticky='W')
lenOption.grid(row=1,column=0,sticky='N')
checkMaj.grid(row=2,column=0,sticky='N')
checkLow.grid(row=2, column=1,sticky='N')
checkSymb.grid(row=2,column=2,sticky='N')
checkInt.grid(row=2,column=3,sticky='N')


app.mainloop()
