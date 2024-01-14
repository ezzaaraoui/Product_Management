class Produit:
    def __init__(self, nom, prix_achat, prix_vente, description="Pas de description", stock=0):
        self._nom = nom
        self._prix_achat = prix_achat
        self._prix_vente = prix_vente
        self._stock = stock
        self._description = description

    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @property
    def prix_achat(self):
        return self._prix_achat
    
    @prix_achat.setter
    def prix_achat(self, prix_achat):
        self._prix_achat = prix_achat

    @property
    def prix_vente(self):
        return self._prix_vente
    
    @prix_vente.setter
    def prix_vente(self, prix_vente):
        self._prix_vente = prix_vente

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = description

    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, stock):
        self._stock = stock

    def __str__(self):
        return f"Nom: {self.nom}, Prix d'achat: {self.prix_achat}, Prix de vente: {self.prix_vente}, Stock: {self.stock}, Description: {self.description}"
    
    def __eq__(self, p):
        return self.nom == p.nom and self.prix_achat == p.prix_achat and self.prix_vente == p.prix_vente and self.description == p.description and self.stock == p.stock 

    def afficher_description(self):
        print(f"Description du produit {self.nom}: {self.description}")

    def modifier_description(self, nouvelle_description):
        self.description = nouvelle_description

    def augmenter_stock(self, quantite):
        self.stock += quantite

    def diminuer_stock(self, quantite):
        if self.stock >= quantite:
            self.stock -= quantite
        else:
            print(f"Stock insuffisant pour {self.nom}")

    def obtenir_valeurs(self):
        return {
            "Nom": self.nom,
            "Prix d'achat": self.prix_achat,
            "Prix de vente": self.prix_vente,
            "Stock": self.stock,
            "Description": self.description,
        }


class Magasin:
    def __init__(self, adresse):
        self.adresse = adresse
        self.stock_produits = []

    def ajouter_produit(self, produit):
        self.stock_produits.append(produit)

    def acheter_produit(self, reference_produit, nombre_exemplaires):
        self.stock_produits[reference_produit].augmenter_stock(nombre_exemplaires)

    def vendre_produit(self, reference_produit, nombre_exemplaires):
        self.stock_produits[reference_produit].diminuer_stock(nombre_exemplaires)

    def bilan(self):
        for produit in self.stock_produits:
            print(produit.obtenir_valeurs())

    def ajouter_livre(self, livre):
        self.stock_produits.append(livre)

    def ajouter_cd(self, cd):
        self.stock_produits.append(cd)

    def rechercher_produit(self, nom):
        for produit in self.stock_produits:
            if produit.nom == nom:
                return produit
        return None

    def rechercher_produit_par_mot(self, mot):
        resultats = []
        for produit in self.stock_produits:
            if mot in produit.description:
                resultats.append(produit)
        return resultats


class Livre(Produit):
    def __init__(self, nom, prix_achat, prix_vente, auteur, editeur, description="Pas de description"):
        super().__init__(nom, prix_achat, prix_vente, description)
        self._auteur = auteur
        self._editeur = editeur

    @property
    def auteur(self):
        return self._auteur
    
    @auteur.setter
    def auteur(self, auteur):
        self._auteur = auteur

    @property
    def editeur(self):
        return self._editeur
    
    @editeur.setter
    def editeur(self, editeur):
        self._editeur = editeur

    def __str__(self):
        return super().__str__() + f", Auteur: {self.auteur}, Editeur: {self.editeur}"


class Cd(Produit):
    def __init__(self, nom, prix_achat, prix_vente, auteur, interprete, titres, description="Pas de description"):
        super().__init__(nom, prix_achat, prix_vente, description)
        self.__auteur = auteur
        self.__interprete = interprete
        self.__titres = titres
    
    @property
    def auteur(self):
        return self.__auteur
    
    @auteur.setter
    def auteur(self, auteur):
        self.__auteur= auteur
    
    @property
    def interprete(self):
        return self.__interprete
    
    @interprete.setter
    def interprete(self, interprete):
        self.__interprete= interprete
    
    @property
    def titres(self):
        return self.__titres
    
    @titres.setter
    def titres(self, titres):
        self.__titres= titres

    def __str__(self):
        return super().__str__() + f", Auteur: {self.auteur}, Interprete: {self.interprete}, Titres: {self.titres}"

class Interaction:
    def __init__(self, magasin):
        self.__magasin = magasin

    def ajouter_produit(self):
        nom = input("Nom du produit: ")
        prix_achat = float(input("Prix d'achat: "))
        prix_vente = float(input("Prix de vente: "))
        description = input("Description du produit: ")
        
        choix = input("Voulez-vous ajouter un livre (L) ou un CD (C)? ").upper()

        if choix == "L":
            auteur = input("Auteur du livre: ")
            editeur = input("Editeur du livre: ")
            produit = Livre(nom, prix_achat, prix_vente, auteur, editeur, description)
        elif choix == "C":
            auteur = input("Auteur du CD: ")
            interprete = input("Interprete du CD: ")
            titres = input("Titres du CD (separés par des virgules): ").split(",")
            produit = Cd(nom, prix_achat, prix_vente, auteur, interprete, titres, description)
        else:
            produit = Produit(nom, prix_achat, prix_vente, description)

        self.__magasin.ajouter_produit(produit)
        print(f"{produit.nom} ajouté au stock.")

    def acheter_produit(self):
        reference_produit = int(input("Référence du produit à acheter: "))
        nombre_exemplaires = int(input("Nombre d'exemplaires à acheter: "))
        self.__magasin.acheter_produit(reference_produit, nombre_exemplaires)
        print(f"{nombre_exemplaires} exemplaires de {self.__magasin.stock_produits[reference_produit].nom} ajoutes au stock.")

    def vendre_produit(self):
        reference_produit = int(input("Référence du produit à vendre: "))
        nombre_exemplaires = int(input("Nombre d'exemplaires à vendre: "))
        self.__magasin.vendre_produit(reference_produit, nombre_exemplaires)
        print(f"{nombre_exemplaires} exemplaires de {self.__magasin.stock_produits[reference_produit].nom} vendus.")

    def modifier_description(self):
        reference_produit = int(input("Reference du produit à modifier: "))
        nouvelle_description = input("Nouvelle description: ")
        self.__magasin.stock_produits[reference_produit].modifier_description(nouvelle_description)
        print(f"Description de {self.__magasin.stock_produits[reference_produit].nom} modifiee.")

    def afficher_bilan(self):
        self.__magasin.bilan()

    def rechercher_produit(self):
        nom = input("Nom du produit à rechercher: ")
        produit = self.__magasin.rechercher_produit(nom)
        if produit:
            print(produit.obtenir_valeurs())
        else:
            print(f"Produit {nom} non trouve.")

    def rechercher_produit_par_mot(self):
        mot = input("Mot à rechercher dans la description: ")
        produits_trouves = self.__magasin.rechercher_produit_par_mot(mot)
        if produits_trouves:
            for produit in produits_trouves:
                print(produit.obtenir_valeurs())
        else:
            print(f"Aucun produit trouve avec le mot {mot} dans la description.")
