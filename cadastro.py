from tkinter import Button
from tkinter import Label
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk


def cadastro_enviado(): 
    messagebox.showinfo("Informação", "Em até 24h você receberá o dinheiro na sua conta!") 
       
#Janela
urubudopix = tk.Tk()
urubudopix.title("Urubu do Pix")
urubudopix.geometry("400x500")

#Imagem de fundo 
imagemfundo_org = Image.open("teladefundo.png")
imagemfundo_resized = imagemfundo_org.resize((400,200))
imagemfundo = ImageTk.PhotoImage(imagemfundo_resized)
rotulo = tk.Label(urubudopix, image = imagemfundo)
rotulo.pack()


#Titulo forms
label = Label(urubudopix, text = "Bem-vindo ao Urubu do PIX", font = ("Working", 24), bg = "white", highlightthickness = 3, highlightbackground = "grey")
label.pack()

#Mensagem
label_mensagem = Label(urubudopix, text = "Clique no botão para ganhar dinheiro", font = ("Working, 16"), bg = "white", highlightthickness= 3, highlightbackground = "grey")
label_mensagem.pack()

#botão solicitar
imagem = Image.open("enviar.png")
imagem_resized = imagem.resize((60,40))
imagem_botao = ImageTk.PhotoImage(imagem_resized)

btn = Button(urubudopix, image = imagem_botao, command = cadastro_enviado)
btn.pack(pady = 20)

urubudopix.mainloop()