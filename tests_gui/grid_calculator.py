from tkinter import *


def buttonPlusClick():
    # Übernahme der Daten
    zahl1 = int(entryZahl1.get())
    zahl2 = int(entryZahl2.get())
    # Verarbeitung der Daten
    ergebnis = zahl1 + zahl2
    # Anzeige der Daten
    labelErgebnis.config(text=str(ergebnis))


def buttonMinusClick():
    # Übernahme der Daten
    zahl1 = int(entryZahl1.get())
    zahl2 = int(entryZahl2.get())
    # Verarbeitung der Daten
    ergebnis = zahl1 - zahl2
    # Anzeige der Daten
    labelErgebnis.config(text=str(ergebnis))


def buttonMalClick():
    # Übernahme der Daten
    zahl1 = int(entryZahl1.get())
    zahl2 = int(entryZahl2.get())
    # Verarbeitung der Daten
    ergebnis = zahl1 * zahl2
    # Anzeige der Daten
    labelErgebnis.config(text=str(ergebnis))


def buttonDurchClick():
    # Übernahme der Daten
    zahl1 = int(entryZahl1.get())
    zahl2 = int(entryZahl2.get())
    # Verarbeitung der Daten
    ergebnis = zahl1 // zahl2
    # Anzeige der Daten
    labelErgebnis.config(text=str(ergebnis))


def buttonRestClick():
    # Übernahme der Daten
    zahl1 = int(entryZahl1.get())
    zahl2 = int(entryZahl2.get())
    # Verarbeitung der Daten
    ergebnis = zahl1 % zahl2
    # Anzeige der Daten
    labelErgebnis.config(text=str(ergebnis))


# Fenster
tkFenster = Tk()
tkFenster.title('Rechner')

# Label mit Aufschrift Zahl 1
labelZahl1 = Label(master=tkFenster, bg='#FFCFC9', text='Zahl 1')
labelZahl1.grid(row=0, column=0, padx='5', pady='5', sticky='ew')

# Entry für Zahl 1
entryZahl1 = Entry(master=tkFenster, bg='white', width='8')
entryZahl1.grid(row=0, column=1, padx='5', pady='5', sticky='ew')

# Label mit Aufschrift Zahl 2
labelZahl2 = Label(master=tkFenster, bg='#FFCFC9', text='Zahl 2')
labelZahl2.grid(row=2, column=0, padx='5', pady='5', sticky='ew')

# Entry für Zahl 2
entryZahl2 = Entry(master=tkFenster, bg='white', width='8')
entryZahl2.grid(row=2, column=1, padx='5', pady='5', sticky='ew')

# Button zum Addieren
buttonPlus = Button(master=tkFenster, text='+', width='2', bg='#FBD975', command=buttonPlusClick)
buttonPlus.grid(row=0, column=2, padx='5', pady='5')

# Button zum Subtrahieren
buttonMinus = Button(master=tkFenster, text='-', width='2', bg='#FBD975', command=buttonMinusClick)
buttonMinus.grid(row=1, column=2, padx='5', pady='5')

# Button zum Multiplizieren
buttonMal = Button(master=tkFenster, text='*', width='2', bg='#FBD975', command=buttonMalClick)
buttonMal.grid(row=2, column=2, padx='5', pady='5')

# Button zum Dividieren ohne Rest
buttonDurch = Button(master=tkFenster, text=':', width='2', bg='#FBD975', command=buttonDurchClick)
buttonDurch.grid(row=3, column=2, padx='5', pady='5')

# Button zum Rest bei der Division
buttonRest = Button(master=tkFenster, text='%', width='2', bg='#FBD975', command=buttonRestClick)
buttonRest.grid(row=4, column=2, padx='5', pady='5')

# Label mit Aufschrift Ergebnis
labelAufschriftErgebnis = Label(master=tkFenster, bg='#D5E88F', text='Ergebnis')
labelAufschriftErgebnis.grid(row=4, column=0, padx='5', pady='5', sticky='ew')

# Label für das Ergebnis
labelErgebnis = Label(master=tkFenster, bg='gray', width='8', text='')
labelErgebnis.grid(row=4, column=1, padx='5', pady='5', sticky='ew')

# Aktivierung des Fensters
tkFenster.mainloop()
