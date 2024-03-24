import mysql.connector

#connexion à la bade de données
connexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="crud"
)

#fonction pour la creation d'un utilisateur
def creat_user(nom, email):
    cursor=connexion.cursor()
    cursor.execute("INSERT INTO utilisateurs (nom, email) VALUES (%s, %s)", (nom, email))
    connexion.commit()

#fonction pour  la lecture des utilisateurs
def read_user():
    cursor=connexion.cursor()
    cursor.execute("SELECT * FROM utilisateurs")
    for (id, nom, email) in cursor:
        print(f"ID: {id}. Nom :{nom}, Email:{email}")

#fonction pour la modification de l'email d'un utilisateur
def update(id,email):
    cursor=connexion.cursor()
    cursor.execute("UPDATE utilisateurs SET email= %s WHERE id= %s ",(email,id))
    connexion.commit()

#fonction pour la suppression d'un utilisateur
def delete(id):
    cursor=connexion.cursor()
    cursor.execute("DELETE FROM utilisateurs WHERE id=%s",(id,))
    connexion.commit()
    





#creat_user("john", "john@gmail.com")
#ead_user()
#update(1, "jonny@yahoo.fr")
delete(1)