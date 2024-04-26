import tkinter as tk
from subprocess import call


def traiter_montant(montant):
    # Ici, vous pouvez effectuer le traitement du montant comme nécessaire
    print(f"Montant du client : {montant}")
    print(montant)
    return montant

# Vous pouvez ajouter plus de fonctions dans ce fichier selon vos besoins


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
        texte1 = tk.Label(self.carre_bleu, text="", font=("Helvetica", 16), fg="white", bg="blue")
        texte1.place(relx=0.48, rely=0.28, anchor="center")
        texte2 = tk.Label(self.carre_bleu, text="Merci de votre visite", font=("Helvetica", 16), fg="white", bg="blue")
        texte2.place(relx=0.50, rely=0.53, anchor="center")
        texte3 = tk.Label(self.carre_bleu, text="", font=("Helvetica", 16), fg="white", bg="blue")
        texte3.place(relx=0.69, rely=0.75, anchor="center")
        bouton1 = tk.Button(fenetre, text="<", bg="white", fg="black", font=("Helvetica", 14))
        bouton1.place(relx=0.7, rely=0.14, anchor="center")
        bouton2 = tk.Button(fenetre, text="<", bg="white", fg="black", font=("Helvetica", 14))
        bouton2.place(relx=0.7, rely=0.28, anchor="center")
        bouton4 = tk.Button(fenetre, text="<", bg="white", fg="black", font=("Helvetica", 14))
        bouton4.place(relx=0.7, rely=0.39, anchor="center")
        # Texte "Bonjour" au milieu du carré
        texte1_d = tk.Label(self.carre_bleu, text="", font=("Helvetica", 16), fg="white", bg="blue")
        texte1_d.place(relx=0.14, rely=0.25, anchor="center")
        texte2_d = tk.Label(self.carre_bleu, text="", font=("Helvetica", 16), fg="white", bg="blue")
        texte2_d.place(relx=0.10, rely=0.53, anchor="center")
        texte3_d = tk.Label(self.carre_bleu, text="", font=("Helvetica", 16), fg="white", bg="blue")
        texte3_d.place(relx=0.14, rely=0.75, anchor="center")
        bouton1_d = tk.Button(fenetre, text=">", bg="white", fg="black", font=("Helvetica", 14))
        bouton1_d.place(relx=0.3, rely=0.14, anchor="center")
        bouton2_d = tk.Button(fenetre, text=">", bg="white", fg="black", font=("Helvetica", 14))
        bouton2_d.place(relx=0.3, rely=0.28, anchor="center")
        bouton4_d = tk.Button(fenetre, text=">", bg="white", fg="black", font=("Helvetica", 14))
        bouton4_d.place(relx=0.3, rely=0.39, anchor="center")



        bouton3 = tk.Button(fenetre, text="-----------------", bg="white", fg="black", font=("Helvetica", 14))
        bouton3.place(relx=0.85, rely=0.25, anchor="center")


        # Bouton Entrer
        bouton_entrer = tk.Button(fenetre, text="Entrer", bg="white", fg="black", font=("Helvetica", 14))
        bouton_entrer.place(relx=0.55, rely=0.85, anchor="center")

        # Bouton Entrer
        bouton_supprimer = tk.Button(fenetre, text="Supprimer", bg="white", fg="black", font=("Helvetica", 14))
        bouton_supprimer.place(relx=0.45, rely=0.85, anchor="center")

        # Carré pour les nombres
        haut = 50
        large = 500
        self.carre_bleu = tk.Canvas(fenetre, bg="#525252", width=large, height=haut)
        self.carre_bleu.place(relx=0.5, rely=0.77, anchor="center")

        # Ajouter des boutons de 0 à 9
        for i in range(10):
            bouton_nombre = tk.Button(fenetre, text=str(i), bg="#525252", fg="white", font=("Helvetica", 10))
            bouton_nombre.place(relx=0.27 + i * 0.05, rely=0.77, anchor="center")




def main():
    fenetre = tk.Tk()
    app = Application(fenetre)
    fenetre.mainloop()

if __name__ == "__main__":
    main()
