import tkinter as tk
import smtplib
from email.mime.text import MIMEText
import tkinter.messagebox

def enviar_email():
    destinatario = entrada_destinatario.get()
    assunto = entrada_assunto.get()
    corpo = entrada_corpo.get("1.0", tk.END)

    servidor = 'smtp.gmail.com'
    porta = 587
    usuario = 'seu email'
    senha = 'sua chave disponivel no seu gmail'

    mensagem = MIMEText(corpo)
    mensagem['Subject'] = assunto
    mensagem['From'] = usuario
    mensagem['To'] = destinatario

    try:
        with smtplib.SMTP(servidor, porta) as smtp:
            smtp.starttls()  # Inicia a criptografia
            smtp.login(usuario, senha)  # Faz login
            smtp.sendmail(usuario, destinatario, mensagem.as_string())  # Envia o e-mail
            tk.messagebox.showinfo("Sucesso", "E-mail enviado com sucesso!")
    except Exception as e:
        tk.messagebox.showerror("Erro", f"Falha ao enviar e-mail: {e}")

root = tk.Tk()
root.title("Enviar Email")
root.geometry("400x400")

tk.Label(root, text='Destinatario:').pack()
entrada_destinatario = tk.Entry(root, width=40)
entrada_destinatario.pack()

tk.Label(root, text="Assunto:").pack()
entrada_assunto = tk.Entry(root, width=40)
entrada_assunto.pack()


tk.Label(root, text="Corpo:").pack()
entrada_corpo = tk.Text(root, height=10, width=40)
entrada_corpo.pack()

botao_enviar = tk.Button(root, text="Enviar", command=enviar_email)
botao_enviar.pack(pady=10)

root.mainloop()
