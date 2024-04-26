import tkinter as tk

class Application:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Application avec Carre et Texte")
        self.fenetre.geometry("250x100")  # Taille de la fenêtre

        # Arrière-plan vert
        fond_vert = tk.Canvas(fenetre, bg="blue", width=350, height=350)
        fond_vert.pack()

        # Texte "Bonjour" au milieu du carré
        texte1 = tk.Label(fenetre, text="Montant insuffisant", font=("Helvetica", 16), fg="white", bg="blue")
        texte1.place(relx=0.5, rely=0.5, anchor="center")


def main():
    fenetre = tk.Tk()
    app = Application(fenetre)
    fenetre.mainloop()

if __name__ == "__main__":
    main()
