import tkinter as tk
from suite import traiter_montant
from subprocess import call

class Client:
    def __init__(self, nom, numero_compte, mot_de_passe, montant_ini):
        self.nom = nom
        self.numero_compte = numero_compte
        self.mot_de_passe = mot_de_passe
        self.montant_ini = montant_ini

class Application:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Application avec Carre et Texte")
        self.fenetre.geometry("1000x700")  # Taille de la fenêtre

        # Arrière-plan vert
        fond_vert = tk.Canvas(fenetre, bg="green", width=1000, height=700)
        fond_vert.pack()

        # Carré à l'arrière-plan bleu au centre
        taille_carre = 350
        self.carre_bleu = tk.Canvas(fenetre, bg="blue", width=taille_carre, height=taille_carre)
        self.carre_bleu.place(relx=0.5, rely=0.26, anchor="center")

        # Texte "Bonjour" au milieu du carré
        texte1 = tk.Label(self.carre_bleu, text="Service sans carte", font=("Helvetica", 16), fg="white", bg="blue")
        texte1.place(relx=0.7, rely=0.3, anchor="center")
        texte2 = tk.Label(self.carre_bleu, text="Gimac", font=("Helvetica", 16), fg="white", bg="blue")
        texte2.place(relx=0.87, rely=0.6, anchor="center")
        bouton1 = tk.Button(fenetre, text="<", bg="white", fg="black", font=("Helvetica", 14),
                            command=self.supprimer_dernier_nombre)
        bouton1.place(relx=0.7, rely=0.16, anchor="center")
        bouton2 = tk.Button(fenetre, text="<", bg="white", fg="black", font=("Helvetica", 14),
                            command=self.supprimer_dernier_nombre)
        bouton2.place(relx=0.7, rely=0.31, anchor="center")
        bouton3 = tk.Button(fenetre, text="-----------------", bg="white", fg="black", font=("Helvetica", 14))
        bouton3.place(relx=0.85, rely=0.25, anchor="center")

        # Champ pour entrer les nombres
        self.champ_nombre = tk.Entry(fenetre, font=("Helvetica", 14))
        self.champ_nombre.place(relx=0.5, rely=0.6, anchor="center")

        # Bouton Entrer
        bouton_entrer = tk.Button(fenetre, text="Entrer", bg="white", fg="black", font=("Helvetica", 14),
                                  command=self.ajouter_nombre)
        bouton_entrer.place(relx=0.55, rely=0.85, anchor="center")

        # Bouton Entrer
        bouton_supprimer = tk.Button(fenetre, text="Supprimer", bg="white", fg="black", font=("Helvetica", 14),
                                     command=self.supprimer_dernier_nombre)
        bouton_supprimer.place(relx=0.45, rely=0.85, anchor="center")

        # Carré pour les nombres
        haut = 50
        large = 500
        self.carre_bleu = tk.Canvas(fenetre, bg="#525252", width=large, height=haut)
        self.carre_bleu.place(relx=0.5, rely=0.77, anchor="center")

        # Ajouter des boutons de 0 à 9
        for i in range(10):
            bouton_nombre = tk.Button(fenetre, text=str(i), bg="#525252", fg="white", font=("Helvetica", 10),
                                      command=lambda i=i: self.ajouter_chiffre(i))
            bouton_nombre.place(relx=0.27 + i * 0.05, rely=0.77, anchor="center")

        # Ajouter des clients
        self.clients = [
            Client("Client1", "12345", "1234", "123456"),
            Client("Client2", "67890", "1284", "50000"),
            Client("Client3", "54321", "3000", "800000")
        ]

    def ajouter_chiffre(self, chiffre):
        # Ajouter le chiffre au champ de saisie
        texte_actuel = self.champ_nombre.get()
        nouveau_texte = texte_actuel + str(chiffre)
        self.champ_nombre.delete(0, tk.END)
        self.champ_nombre.insert(0, nouveau_texte)


    prix = 0

    def ajouter_nombre(self):
        nombre = self.champ_nombre.get()

        # Vérifier si le mot de passe correspond à l'un des clients
        client_trouve = False
        for client in self.clients:
            if nombre == client.mot_de_passe:
                client_trouve = True
                # Appeler la fonction dans suite.py avec le montant du client

                prix = client.montant_ini
                break
        if client_trouve:
            print("Client trouvé")
            self.fenetre.destroy()
            traiter_montant(prix)
            call(["python", "fic.py"])
        else:
            print("Client non trouvé")

    def supprimer_dernier_nombre(self):
        texte_actuel = self.champ_nombre.get()
        if texte_actuel:
            nouveau_texte = texte_actuel[:-1]
            self.champ_nombre.delete(0, tk.END)
            self.champ_nombre.insert(0, nouveau_texte)

    def mettre_a_jour_nombre(self, nombre):
        print(nombre)

def main():
    fenetre = tk.Tk()
    app = Application(fenetre)
    fenetre.mainloop()

if __name__ == "__main__":
    main()
