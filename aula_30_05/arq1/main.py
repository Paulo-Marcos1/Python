import tkinter as tk
import os
from incluir import AddUserWindow

class Database:
    """Classe responsavel pelo acesso ao SQLite."""
    def __init__(self, db_filename: str):
        self.db_file = os.path.join(os.path.dirname(__file__), db_filename)
        self._ensure_table()

    def _connect(self):
        import  sqlite3
        return sqlite3.connect(self.db_file)

    def _ensure_table(self):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXTO NOT NULL,
            email TEXT NOT NULL UNIQUE
            )
        """)
        conn.commit()
        conn.close()

    def add_user(self, nome:str, email: str)-> None:
        """Tenta inserir um novo usuario; lança erro se o email ja existir"""
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios ( nome, email) VALUES (?, ?)", (nome, email))
        conn.commit()
        conn.close()

    def list_users(self):
        """Retorna lista de tuplas (id, nome, email)"""
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email FROM usuarios")
        rows = cursor.fetchall()
        conn.close()
        return rows

class MainApp:
    """Janela principal que lista usuarios e abre a janela de inclusao"""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("CRUD com tkinter e sqlite")
        self.root.geometry("450x400")

        self.db = Database("usuarios.db")

        #Widgets
        self.btn_novo = tk.Button(root, text= "Novo Usuario", command=self.abrir_janela_inclusao)
        self.btn_novo.pack(pady=10)

        self.listbox = tk.Listbox(root, width=60, height=15)
        self.listbox.pack(padx=10, pady=10)

        #carrega lista inicial
        self.refresh_list()

    def refresh_list(self):
        """Limpa e preenche o listbox com os usuariops do banco"""
        self.listbox.delete(0, tk.END)
        for uid, nome, email in self.db.list_users():
            self.listbox.insert(tk.END, f"ID: {uid:03d} - {nome} <{email}>")

    def abrir_janela_inclusao(self):
        """Abre a janela de inclusao, passando callback para atualizaçao"""
        AddUserWindow(self.root, self.db, on_sucess=self.refresh_list)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

