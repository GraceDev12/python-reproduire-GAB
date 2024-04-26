import tkinter as tk

def traiter_montant(montant):
    fenetre = tk.Tk()

    reste = 80000 - montant
    fenetre = fenetre
    fenetre.title("Application avec Carre et Texte")
    fenetre.geometry("400x200")  # Taille de la fenêtre

    # Arrière-plan vert
    fond_vert = tk.Canvas(fenetre, bg="blue", width=350, height=350)
    fond_vert.pack()

    # Texte "Bonjour" au milieu du carré
    texte1 = tk.Label(fenetre, text="Montant retiré, il vous reste ", font=("Helvetica", 16), fg="white", bg="blue")
    texte1.place(relx=0.5, rely=0.3, anchor="center")
    texte1 = tk.Label(fenetre, text=reste, font=("Helvetica", 16), fg="white", bg="blue")
    texte1.place(relx=0.5, rely=0.6, anchor="center")

    print(reste)
    fenetre.mainloop()








