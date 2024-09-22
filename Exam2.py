#Class boison

# definir une classe Boison
class Boisson:
    def __init__ (self, volume, peremption): 
        self.volume = volume # volume
        self.peremption = peremption # peremption en jours
        
    def prochain_jour (self):
        self.peremption = self.peremption - 1
        print(self.peremption)
        
#nstancier une première Boisson dont le volume sera de 350mL et dont la date de péremption est dans 2 semaines.
boisson1 = Boisson(350, 14)

print("Le volume de la boison1 est: " , boisson1.volume ,"ml")
print("La date de peremption de la boison1 est:" , boisson1.peremption , "jours")
---------------------------------------------------------------------------------------------

# définir une classe Jus qui héritera de la classe Boison
class Jus(Boisson):
    def __init__(self, volume):
        self.volume = volume # volume
        self.peremption = 7 # peremption en 7 jours
        
# deifnition de la class DataCola
class DataCola(Boisson):
    def __init__ (self, c):
        if (c == 'canette'):
            # pour les canettes le volume est 330 mL et les jours de péremption = 60j
            # initialisation des valeurs en utilisant le constructeur de la class Boisson
            super().__init__(volume=330, peremption=60)
            
        elif (c == 'bouteille'):
            # pour les canettes le volume est 500 mL et les jours de péremption = 30j
            # initialisation des valeurs en utilisant le constructeur de la class Boisson
            super().__init__(volume=500, peremption=30)
        
        else:
            raise ValueError("Veuillez saisir 'bouteille' ou 'canette' comme valeur d'entrée du constructeur")

#instanciez un objet de type Jus dont le volume sera de 1000mL
Jus1 = Jus(1000)
# vsisualiser les attributs de l'object
print('Jus1.volume:',Jus1.volume)
print('Jus1.peremption:',Jus1.peremption)

#Instanciez un objet de type DataCola dont le récipient sera une canette.
DataCola1 = DataCola('canette')
# vsisualiser les attributs de l'object
print('DataCola1.volume:',DataCola1.volume)
print('DataCola1.peremption:',DataCola1.peremption)

--------------------------------------------------------------------------
class Distributeur:
    def __init__(self, contenu, taille): # constructeur de la classe
        self.contenu = contenu # attribut qui contiendra la liste d'objet de type Boisson
        self.taille = taille # attribut qui contiendra le nombre max de boison dans le distributeur
        
    def ajouter(self, boisson): # Méthode pour ajouter une boisson à la fin de la liste
        if len(self.contenu) < self.taille:
            self.contenu.append(boisson) # ajouter une boisson à la fin de la liste
    
    def enlever(self, i): # Méthode pour supprimer une boisson de la liste
        boisson_sup = self.contenu.pop(i)  # Supprimer une boisson de la liste à la position i
        print("Boisson supprimée: ",boisson_sup)

    def verifier(self): #Méthode pour vérifier les dates de péremption
        for index, boisson in enumerate(self.contenu):
            if boisson.peremption <= 0: # vérification de la péremption
                self.enlever(index) # retirer les boisson périmée du distributeur avec la méthode enlever()
                
    def prochain_jour(self): #Méthode pour réduire le nombre de jours de conservation restant à toutes les boissons
        for boisson in self.contenu:
            boisson.peremption = boisson.peremption - 1
            
# tester la classe et les méthodes
print("********création d'un distributeur avec les boissons ******")
boisson1 = Boisson(330, 7)
distributeur1 = Distributeur([boisson1], 5) # distributeur avec une boisson et une taille de 5
# ajouter des boissons au distributeur
distributeur1.ajouter(Boisson(330, 1))
distributeur1.ajouter(Boisson(330, 2))
distributeur1.ajouter(Boisson(330, 3))
distributeur1.ajouter(Boisson(350, 4))
distributeur1.ajouter(Boisson(350, 50))
distributeur1.ajouter(Boisson(350, 15))

for i in range(5):
    print("boisson",i," peremption:",distributeur1.contenu[i].peremption)
    print("boisson",i," volume:",distributeur1.contenu[i].volume)

# reduire le nombre de jours
print("\n********reduire le nombre de jours******")
distributeur1.prochain_jour()
for i in range(5):
    print("boisson",i," peremption:",distributeur1.contenu[i].peremption)
    print("boisson",i," volume:",distributeur1.contenu[i].volume)

# vérifier les boissons
print("\n********vérifier les boissons******")
distributeur1.verifier()
for i in range(len(distributeur1.contenu)):
    print("boisson",i," peremption:",distributeur1.contenu[i].peremption)
    print("boisson",i," volume:",distributeur1.contenu[i].volume)

-------------------------Morpion ---------------------------

##################Exercice: Morpion ####################
class Case: # definition de la classe Case avec un seul attribut
    def __init__(self): # definition du constructeur de la classe Case
        self.occupe = ' ' # lors de l'instanciation attribuer la valeur = ' '
        
    def jouer1(self): # definition de la méthode jouer1
        if(self.occupe == ' '):
            self.occupe = 'X'
            
    def jouer2(self): # definition de la méthode jouer2
        if(self.occupe == ' '):
            self.occupe = 'O'

# tester la classe Case et ces méthodes 
case1 = Case() # creation d'une instance de la classe case
print(case1.occupe) # vérification de la valeur de l'attribut occupe
case1.jouer1() # exécution de la méthode jouer1
case1.jouer2() # exécution de la methode jouer2
print(case1.occupe) # vérification de la valeur de l'attribut occupe

              -----------------------------------
# définition de la classe Terrain
class Terrain:
    def __init__(self):
        self.grille = [Case() for i in range(1, 10)] # initialisation de l'attribut grille contenant 9 cases
        self.tour = 1 # initialisation de l'attribut avec la valeur 1
        
    def __str__(self): # méthode str pour formater et afficher un objet terrain avec print()
        ligne1 = self.grille[0:3] # récupération de la premiere ligne de 0 à 2
        ligne2 = self.grille[3:6] # récupération de la deuxième ligne de 3 à 5
        ligne3 = self.grille[6:]  # récupération de la troisième ligne de 6 à 8
        
        #formatage des lignes         
        str_ligne1 = ligne1[0].occupe.__str__() +' | '+ ligne1[1].occupe.__str__() +' | '+ ligne1[2].occupe.__str__()+'\n'
        str_ligne2 = ligne2[0].occupe.__str__() +' | '+ ligne2[1].occupe.__str__() +' | '+ ligne2[2].occupe.__str__()+'\n'
        str_ligne3 = ligne3[0].occupe.__str__() +' | '+ ligne3[1].occupe.__str__() +' | '+ ligne3[2].occupe.__str__()+'\n'
        
        result = str_ligne1 + str_ligne2 + str_ligne3
        
        return result
    
    def jouer(self, a):
        if (a >= 0 and a <= 8):
            
            if self.tour == 1: # vérifier à qui le tour de jouer
                self.grille[a].jouer1() # faire appel à la méthode jouer1() de la case concernée
                self.tour = 2 # donner la main à l'autre joueur
                
            elif self.tour == 2: # vérifier à qui le tour de jouer
                self.grille[a].jouer2() # faire appel à la méthode jouer2() de la case concernée
                self.tour = 1 # donner la main à l'autre joueur
                     
        
# test des code
#terrain1 = Terrain()
#terrain1.grille[3].jouer1()
#terrain1.grille[2].jouer2()
#print(terrain1)

              -----------------------------------
# affichage simple 
terrain1 = Terrain() # créer une instance de la classe terrain
# faire appel à la méthode jouer() par chaque joueur à son tour
terrain1.jouer(3) 
terrain1.jouer(6)
terrain1.jouer(5)
terrain1.jouer(2)
terrain1.jouer(4)

#affichage du resultat
print(terrain1)


              -----------------------------------
# affichage dynamique
import time

terrain1 = Terrain()

def affichage_dynamique(i):
    terrain1.jouer(i)
    print(terrain1)
    time.sleep(1)  # Pause d'une seconde
    
list_instructions = [3,6,5,2,4]

for i in list_instructions:
    affichage_dynamique(i)
