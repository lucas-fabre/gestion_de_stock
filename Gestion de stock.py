import mysql.connector
from tkinter import *
from tkinter import ttk

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "R00t",
    database = "boutique"
    )
cursor = db.cursor()


##---Définition de la fenêtre---##
fenetre = Tk()
fenetre.geometry('660x350')
fenetre.title('Gestion de stock')

##---Définition globale de la liste---##
#Texte de liste.
label1 = Label(fenetre, text = "Produits en stock:")

#Emplacement du texte de liste.
label1.grid(row = 0, column = 0)


#Visualisation treeview
columns = ('ID', 'Nom', 'Description', 'Prix', 'Quantité', 'Id catégorie')
tree = ttk.Treeview(fenetre, height=5, columns=columns, show='headings')
tree.grid(row=1, column=0, sticky='news')

#Attributs des colonnes
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor=CENTER)

#Récupération des infos.
cursor.execute("SELECT * FROM produit")
data =cursor.fetchall()

for i in data:
    tree.insert("", END, values=i)

cursor.close()

#Scrollbar
sb = Scrollbar(fenetre, orient=VERTICAL, command=tree.yview)
sb.grid(row=1, column=1, sticky='ns')
tree.config(yscrollcommand=sb.set)
##---Fin définition globale de la liste---##


##---Définition global de la boite, des labels et des entrées---##
tableau = Frame(fenetre)
ajtnom = Entry(tableau)
ajtdescr = Entry(tableau)
ajtprix = Entry(tableau)
ajtqnt = Entry(tableau)
ajtid_cat = Entry(tableau)

#Labels "Ajouter produit".
ajttxtnom = Label(tableau, text = "Nom:")
ajttxtdescr = Label(tableau, text = "Description:")
ajttxtprix = Label(tableau, text = "Prix:")
ajttxtqnt = Label(tableau, text = "Quantité:")
ajttxtid_cat = Label(tableau, text = "Id catégorie:")


#Entrée "Supprimer un produit".
sprid = Entry(tableau)

#Label "Supprimer produit".
sprtxtid = Label(tableau, text = "Id objet \nà supprimer:")

#Entrées "Modifier un produit".
mdfnom = Entry(tableau)
mdfdescr = Entry(tableau)
mdfprix = Entry(tableau)
mdfqnt = Entry(tableau)
mdfid_cat = Entry(tableau)
mdfid = Entry(tableau)

#Labels "Modifier un produit".
mdftxtid = Label(tableau, text = "Id de l'objet \nà modifier")
mdftxtnom = Label(tableau, text = "Nom à modifier:")
mdftxtdescription = Label(tableau, text = "Description à modifier:")
mdftxtprix = Label(tableau, text = "Prix à modifier:")
mdftxtquantite = Label(tableau, text = "Quantité à modifier:")
mdftxtId_Categorie = Label(tableau, text = "Id catégorie à modifier:")

#Emplacements des labels et des entrées "Ajouter un produit".
ajttxtnom.grid(row = 1, column = 0)
ajttxtdescr.grid(row = 2, column = 0)
ajttxtprix.grid(row = 3, column = 0)
ajttxtqnt.grid(row = 4, column = 0)
ajttxtid_cat.grid(row = 5, column = 0)

ajtnom.grid(row = 1, column = 1)
ajtdescr.grid(row = 2, column = 1)
ajtprix.grid(row = 3, column = 1)
ajtqnt.grid(row = 4, column = 1)
ajtid_cat.grid(row = 5, column = 1)

#Emplacements du label et de l'entrée "Supprimer un produit".
sprtxtid.grid(row = 1, column = 2)
sprid.grid(row = 1, column = 3)

#Emplacements des labels et des entrées "Modifier un produit".
mdftxtid.grid(row = 1, column = 4)
mdftxtnom.grid(row = 2, column = 4)
mdftxtdescription.grid(row = 3, column = 4)
mdftxtprix.grid(row = 4, column = 4)
mdftxtquantite.grid(row = 5, column = 4)
mdftxtId_Categorie.grid(row = 6, column = 4)

mdfid.grid(row = 1, column = 5)
mdfnom.grid(row = 2, column = 5)
mdfdescr.grid(row = 3, column = 5)
mdfprix.grid(row = 4, column = 5)
mdfqnt.grid(row = 5, column = 5)
mdfid_cat.grid(row = 6, column = 5)
##---Fin définition global des labels et des entrées---##

##---Définition global des fonctions "Ajouter", "Supprimer", "Modifier"---##
#Fonction ajoutant un produit lors du clic sur le bouton.
def soumettre_ajout():
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "R00t",
        database = "boutique"
        )
    cursor = db.cursor()
    
    nom = ajtnom.get()
    description = ajtdescr.get()
    prix = ajtprix.get()
    quantite = ajtqnt.get()
    id_categorie = ajtid_cat.get()

    cursor.execute(f"INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES ('{nom}', '{description}', {prix}, {quantite}, {id_categorie});")
    
    db.commit()
    #Fonction permettant de supprimer les valeurs rentrées pour en rajouter de nouvelles plus rapidement. 
    ajtnom.delete(0, END)
    ajtdescr.delete(0, END)
    ajtprix.delete(0, END)
    ajtqnt.delete(0, END)
    ajtid_cat.delete(0, END)

    #Actualise le tableau en supprimant les anciennes valeurs pour ajouter la nouvelle en plus des anciennes valeurs. 
    for item in tree.get_children():
        tree.delete(item)
      
    cursor.execute("SELECT * FROM produit")
    data =cursor.fetchall()

    for i in data:
        tree.insert("", END, values=i)

    cursor.close()

    

#Fonction supprimant un produit lors du renseignant l'id puis en appuyant sur le bouton.
def soumettre_suppr():

    cursor = db.cursor()

    supprimer = sprid.get()

    cursor.execute(f"DELETE FROM produit where id = {supprimer};")
    
    db.commit()
    #Fonction permettant de supprimer la valeur rentrée pour en rajouter une nouvelle plus rapidement.
    sprid.delete(0, END)
    
    #Actualise le tableau en supprimant les anciennes valeurs pour ajouter la nouvelle en plus des anciennes valeurs. 
    for item in tree.get_children():
        tree.delete(item)
      
    cursor.execute("SELECT * FROM produit")
    data =cursor.fetchall()

    for i in data:
        tree.insert("", END, values=i)

    cursor.close()

#Fonction modifiant un produit lors du renseignement de l'id, les nouvelles valeurs et en appuyant sur le bouton.
def soumettre_modifier():

    cursor = db.cursor()
    
    id = mdfid.get()
    nom = mdfnom.get()
    description = mdfdescr.get()
    prix = mdfprix.get()
    quantite = mdfqnt.get()
    id_categorie = mdfid_cat.get()

    cursor.execute(f"update produit set nom = '{nom}', description = '{description}', prix = {prix}, quantite = {quantite}, id_categorie = {id_categorie} where id = {id}")

    db.commit()
    #Fonction permettant de supprimer les valeurs rentrées pour en rajouter de nouvelles plus rapidement.
    mdfid.delete(0, END)
    mdfnom.delete(0, END)
    mdfdescr.delete(0, END)
    mdfprix.delete(0, END)
    mdfqnt.delete(0, END)
    mdfid_cat.delete(0, END)

    #Actualise le tableau en supprimant les anciennes valeurs pour ajouter la nouvelle en plus des anciennes valeurs. 
    for item in tree.get_children():
        tree.delete(item)
      
    cursor.execute("SELECT * FROM produit")
    data =cursor.fetchall()

    for i in data:
        tree.insert("", END, values=i)

    cursor.close()
##---Fin définition global des fonctions "Ajouter", "Supprimer", "Modifier"---##


##---Définition des boutons---##
#Boutons.
ajoutbouton = Button(tableau, text = "Ajouter un produit", command = soumettre_ajout)
supprbouton = Button(tableau, text = "Supprimer un produit", command = soumettre_suppr)
modifbouton = Button(tableau, text = "Modifier un produit", command = soumettre_modifier)

#Emplacement des boutons.
ajoutbouton.grid(row = 6, column = 1)
supprbouton.grid(row = 2, column = 3)
modifbouton.grid(row = 7, column = 5)
##---Fin définition des boutons---##

tableau.grid(row = 2, column = 0)
fenetre.mainloop()