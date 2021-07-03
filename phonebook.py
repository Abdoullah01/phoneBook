from tkinter import *
from os import chdir
from tkinter import messagebox

chdir('e://Phonebook_project')


#functions

def lecture():
    file = open('repertoire.txt', 'r')
    line = file.readline()
    i = 0
    while line != "":
        textbox.insert(1.0, line)
        line = file.readline()
        i = i + 1
    textbox.insert(END, "Il y a"+" "+str(i)+" "+"contact(s) dans votre répertoire")
    textbox.grid(columnspan=3, padx=20, pady=20)
    file.close() 


def afiche():
    Frame1.grid(padx=15,pady=15, columnspan=3)
      


def ecriture():
    try:
        file = open('repertoire.txt', 'a')
        nom = entree_name_var.get()
        prenom = entree_last_name_var.get()
        numero = entree_contact_var.get()
        ligne = nom + " " + prenom + " : " + numero + "\n" 
        file.write(ligne)
        file.close()
        notif.config(text="Contact enregistré avec succès", fg='green')
    except:
        notif.config(text="Contact non enregistré", fg="red")


def affiche1():
    Frame2.grid(padx=15,pady=15, columnspan=3)
 
    
def recherche():
    file = open('repertoire.txt', 'r')
    nom = entree_search_name_var.get()
    lines = file.readlines()
    for line in lines:
        if nom in line:
            textbox1.insert(1.0, line)
            break       
    for line in lines:
        if nom not in line:
            textbox1.insert(1.0, "Inconnu")
            break
    file.close()
    textbox1.grid(columnspan=3, padx=20, pady=20)

def affiche2():
    Frame3.grid(padx=15,pady=15, columnspan=3)


def supprimer():
    try:
        file = open('repertoire.txt', 'r')
        name = entree_delete_name_var.get()
        lines = file.readlines()
        for line in lines:
            if line != name:
                file = open('repertoire.txt', 'w')
                file.write(line)
        notif1.config(text="Contact supprimé avec succès", fg='green')
    except:
        notif1.config(text="Contact non enregistré", fg="red")
        
    file.close()
   

 
def reset():
    entree_name_var.set('')
    entree_last_name_var.set('')
    entree_contact_var.set('')
	
    
    
# interface grafique
fen = Tk()
cnv = Canvas(fen, width=600, height=250)
cnv.grid(columnspan =3, rowspan =3)
label = Label(fen, text="Répertoire téléphonique", font="arial 20")
label.grid(columnspan=3, row=0, column=0)

btn = Button(fen,text='Quitter', command=fen.quit, bg="red", width=20, height=2)
btn.grid(row=3, column=1)
btn1 = Button(fen,text='Ajouter un Contact', bg="#6B69D6", width=20,height=2 , command=afiche)
btn1.grid(row=1, column=0, sticky=W)
btn2 = Button(fen,text='Afficher le répertoire', bg="#6B69D6", width=20, height=2, command=lecture)
btn2.grid(row=2, column=0, sticky=W)
btn3 = Button(fen,text='Rechercher un Contact', bg="#6B69D6", width=20, height=2, command=affiche1)
btn3.grid(row=1, column=2, sticky=E)
btn4 = Button(fen,text='Supprimer un Contact', bg="#6B69D6", width=20, height=2, command=affiche2 )
btn4.grid(row=2, column=2, sticky=E)

textbox = Text(fen, height=10, width=50)



Frame1 = LabelFrame(fen,text="Enregistrer un Contact")

Inside_Frame1 = Frame(Frame1)
Inside_Frame1.grid(row=0,column=0,padx=15,pady=15)


label_name = Label(Inside_Frame1,text="Nom")
label_name.grid(row=0,column=0,padx=5,pady=5)
entree_name_var = StringVar()



E_name = Entry(Inside_Frame1,width=30, textvariable=entree_name_var)
E_name.grid(row=0,column=1,padx=5,pady=5)

label_last_name= Label(Inside_Frame1,text="Prénoms")
label_last_name.grid(row=1,column=0,padx=5,pady=5)
entree_last_name_var = StringVar()


E_last_name = Entry(Inside_Frame1,width=30,textvariable=entree_last_name_var)
E_last_name.grid(row=1,column=1,padx=5,pady=5)

label_contact= Label(Inside_Frame1,text="Numéro")
label_contact.grid(row=2,column=0,padx=5,pady=5)
entree_contact_var = StringVar()


E_contact = Entry(Inside_Frame1,width=30,textvariable=entree_contact_var)
E_contact.grid(row=2,column=1,padx=5,pady=5)

save_button = Button(Frame1,text="Enregistrer",width=15,bg="#6B69D6",fg="#FFFFFF", command=ecriture)
save_button.grid(columnspan=3, padx=5,pady=5)

save_button = Button(Frame1,text="Reset",width=15,bg="#6B69D6",fg="#FFFFFF", command=reset)
save_button.grid(columnspan=3, padx=5,pady=5)

notif = Label(Frame1, font = ('Calibri',12) )
notif.grid()

textbox1 = Text(fen, height=10, width=50)

Frame2 = LabelFrame(fen,text="Rechercher un Contact")

Rech_Frame = Frame(Frame2)
Rech_Frame.grid(row=0,column=0,padx=15,pady=15)

search_name = Label(Rech_Frame,text="Entrez un nom")
search_name.grid(row=0,column=0,padx=5,pady=5)
entree_search_name_var = StringVar()

R_name = Entry(Rech_Frame,width=30, textvariable=entree_search_name_var)
R_name.grid(row=0,column=1,padx=5,pady=5)

search_button = Button(Frame2,text="Rechercher",width=15,bg="#6B69D6",fg="#FFFFFF", command=recherche)
search_button.grid(columnspan=3, padx=5,pady=5)

Frame3 = LabelFrame(fen,text="Rechercher un Contact")

delete_Frame = Frame(Frame3)
delete_Frame.grid(row=0,column=0,padx=15,pady=15)

delete_name = Label(delete_Frame,text="Entrez un nom")
delete_name.grid(row=0,column=0,padx=5,pady=5)
entree_delete_name_var = StringVar()

D_name = Entry(delete_Frame,width=30, textvariable=entree_delete_name_var)
D_name.grid(row=0,column=1,padx=5,pady=5)

delete_button = Button(Frame3,text="Supprimer",width=15,bg="red",fg="#FFFFFF", command=supprimer)
delete_button.grid(columnspan=3, padx=5,pady=5)

notif1 = Label(Frame3, font = ('Calibri',12) )
notif1.grid()



fen.mainloop()