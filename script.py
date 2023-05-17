
import mysql.connector

#cnx ou caramel, peut importe le nom choisis
cnx = mysql.connector.connect( #Établit une connexion à votre base de données MySQL en utilisant les informations d'identification appropriées
    host="localhost",
    user="root",
    port="3307",
    password="example",
    database="apprenants"
)

cursor = cnx.cursor() #Crée un curseur pour exécuter des requêtes SQL 
                      

# Exécutez une requête pour récupérer les noms et prénoms des élèves depuis une table "eleves"
query = "SELECT nom,prenom FROM apprenant"
cursor.execute(query)

result = cursor.fetchall()  # Récupère toutes les lignes de résultat

#for row in result: 
    #print(row[0])
    #print(row[1])      cette partie permettrai d'afficher tous les nom et prénom de la bdd qui est appelé.
    






import random #importe la biblihotèque random


#VERSION INITIAL DE LA BOUCLE:

#nombre_eleves =len(result)
#taille_groupe =2
#random.shuffle(result)  #random.shuffle permet de melanger la liste de nom et prenom de manière aléatoire


#for i in range (0, nombre_eleves, taille_groupe):
#   print('groupe numero', int(i/2)+1,':', result[i],'&', result[i+1]) 
 #  if len(result)/taille_groupe == 1:
  #     print("un des groupes sera incomplet") #cette ligne permet de prevenir qu'un groupe sera incomplet si la liste est impair#
# FIN
   





taille_groupe = int(input("Entrez la taille des groupes : ")) #"c'est à l'utilisateur de determiner le nombre de personne par groupe avant de lancer la boucle"

 
# Mélange la liste de noms et prénoms de manière aléatoire
random.shuffle(result)

nombre_eleves = len(result) #nombre d'élement de la liste
nombre_groupes = nombre_eleves // taille_groupe  #cette partie sert a diviser le nombre d'éleves par le 
                                                 #groupe sans prendre en compte la partie fractionnaire

for i in range(0, nombre_eleves, taille_groupe):  
    groupe_num = i // taille_groupe + 1 #permet de numeroté les groupes. le + 1 evite de partir de 0 (python ..)
    
    groupe = result[i:i+taille_groupe]  # les   Par exemple, si i vaut 0 et taille_groupe vaut 2, 
                                         #  il prendra la premiere itération (donc la 1) puis celle qui est à l'emplacement de la "première + 1" (donc la 2)

    print("Groupe numéro", groupe_num, ":")

    for nom, prenom in groupe: #sert a imprimé le nom et le prenom dans les groupe créé
        print(nom, prenom)

    if len(groupe) < taille_groupe: #si un groupe est pas assez nombreux alors cela affichera 
                                    #leurs nom dans le dernier groupe avec une phrase pour le mentionner
        print("Ce groupe est incomplet")

    print()

if nombre_eleves % taille_groupe != 0:
    nb_personnes_sans_groupe = nombre_eleves % taille_groupe # cette partie sert a comptabiliser le nombre de personne sans groupe 
                                                             #en calculant le reste de la division du nombre d'eleves par la taille de groupe.
                                                             #probablement superflue mais j'aime bien3
                                                            
    print("il y aura un groupe incomplet de :",nb_personnes_sans_groupe, "personne")





"""insert_query = "INSERT INTO groupes (nom, prenom, groupe_num) VALUES (%s, %s, %s)"

for i in range(0, nombre_eleves, taille_groupe):
    groupe_num = int(i / taille_groupe) + 1
    groupe = result[i:i+taille_groupe]

    for row in groupe:
        nom = row[0]
        prenom = row[1]
        values = (nom, prenom, groupe_num)
        cursor.execute(insert_query, values)"""

cnx.commit()





















#Ferme le curseur et la connexion à la base de données :

cursor.close()
cnx.close()