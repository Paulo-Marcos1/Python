import tkinter as tk
from tkinter import messagebox

class AddUserWindow(tk.Toplevel):
    """Janela para adicionar um novo usuario"""

    def __init__(self, master, database, on_sucess=None):
        """

        :param master: janela-pai (Tk)
        :param database: instancia da classe Database
        :param on_sucess: callback sem argumentos, chamado após inclusao
        """

        super().__init__(master)
        self.title("Incluir usuario")
        self.resizable(False, False)
        self.database = database
        self.on_sucess = on_sucess

        #layout
        tk.Label(self, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_nome = tk.Entry(self, width=30)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Email:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_email = tk.Entry(self, width=30)
        self.entry_email.grid(row=0, column=1, padx=10, pady=5)

        btn_frame = tk.Frame(self)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(btn_frame, text="Salvar", command=self.salvar).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Cancelar", command=self.salvar).pack(side="right", padx=5)

        #centraliza a janela sobre a principal

        self.transient(master)
        self.grab_set()
        master.wait_window(self)

        def salvar(self):
            nome = self.entry_nome.get().strip()
            email = self.entry_email.get().strip()
            if not nome or not email:
                messagebox.showerror("Erro", "Preencha todos os campos!")
                return

            try:
                self.database.add_user(nome, email)
            except Exception as e:
                #espera sqlite.integrityerror para email duplicado
                messagebox.showerror("Erro ao adicionar", str(e))
                return

            messagebox.showinfo("Sucesso", "Usuario adicionado com sucesso")
            if callable(self.on_success):
                self.on_success()
            self.destroy()


        


