import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# --- Dados da loja ---
produtos = {
    "Quadro geek": 450,
    "Funko pop": 3000,
    "Camisa": 2000,
    "Cubo mágico": 1800,
    "Bis": 400,
    "Kit arduino": 3200,
}

saldo_inicial = 1000
saldo = saldo_inicial

# --- Funções ---
def comprar():
    selecionado = lista_produtos.curselection()
    if not selecionado:
        messagebox.showwarning("Nenhum item selecionado", "Escolha um produto para comprar.")
        return

    nome_completo = lista_produtos.get(selecionado)
    produto = nome_completo.split(" - ")[0]
    preco = produtos[produto]

    global saldo
    if preco <= saldo:
        saldo -= preco
        adicionar_ao_inventario(produto, preco)
        atualizar_saldo()
        messagebox.showinfo("Compra realizada", f"Você comprou: {produto} por {preco} Ctrl Cash!")
    else:
        messagebox.showwarning("Saldo insuficiente", "Você não tem Ctrl Cash suficiente!")

def adicionar_saldo():
    global saldo
    try:
        valor = int(entrada_valor.get())
        if valor > 0:
            saldo += valor
            atualizar_saldo()
            entrada_valor.delete(0, tk.END)
            messagebox.showinfo("Saldo adicionado", f"Você adicionou {valor} Ctrl Cash!")
        else:
            messagebox.showwarning("Valor inválido", "Digite um valor positivo.")
    except ValueError:
        messagebox.showwarning("Entrada inválida", "Digite um número válido.")

def retirar_saldo():
    global saldo
    try:
        valor = int(entrada_retirar.get())
        if valor > 0:
            if valor <= saldo:
                saldo -= valor
                atualizar_saldo()
                entrada_retirar.delete(0, tk.END)
                messagebox.showinfo("Retirada realizada", f"Você retirou {valor} Ctrl Cash!")
            else:
                messagebox.showwarning("Saldo insuficiente", "Você não tem Ctrl Cash suficiente.")
        else:
            messagebox.showwarning("Valor inválido", "Digite um valor positivo.")
    except ValueError:
        messagebox.showwarning("Entrada inválida", "Digite um número válido.")

def atualizar_saldo():
    lbl_saldo.config(text=f"Saldo: {saldo} Ctrl Cash")

def adicionar_ao_inventario(produto, preco):
    inventario.insert(tk.END, f"{produto} - {preco} CC")
    atualizar_total()

def atualizar_total():
    total = 0
    for item in inventario.get(0, tk.END):
        preco = int(item.split(" - ")[1].split(" ")[0])
        total += preco
    lbl_total.config(text=f"Total: {total} CC")

def toggle_fullscreen():
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

# --- Interface Gráfica ---
root = tk.Tk()
root.title("🛒 Lojinha Ctrl Cash")
root.attributes('-fullscreen', True)

# --- Carregar imagem de fundo ---
image_path = "background.jpg"
if not os.path.exists(image_path):
    messagebox.showerror("Erro", "Imagem de fundo não encontrada!")
    exit()

try:
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    original_image = Image.open(image_path)
    resized_image = original_image.resize((screen_width, screen_height), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(resized_image)
except Exception as e:
    messagebox.showerror("Erro", f"Erro ao carregar a imagem: {e}")
    exit()

# --- Canvas principal como fundo ---
canvas = tk.Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")
canvas.image = bg_photo


style_button = {
    'bd': 0,
    'highlightthickness': 0,
    'relief': 'flat',
    
    
}

# Função para criar botões
def criar_botao(parent, texto, comando, cor, font=("Verdana", 12)):
    return tk.Button(parent, text=texto, command=comando, bg=cor, fg="white", font=font, **style_button)

# --- Criação dos elementos ---
lbl_titulo = tk.Label(canvas, text="🛒 Lojinha Ctrl Cash", 
                     font=("Verdana", 18, "bold"), fg="#4CAF50")
canvas.create_window(screen_width//2, 50, window=lbl_titulo)

lbl_saldo = tk.Label(canvas, text=f"Saldo: {saldo_inicial} Ctrl Cash", 
                    font=("Verdana", 14))
canvas.create_window(screen_width//2, 100, window=lbl_saldo)

lista_produtos = tk.Listbox(canvas, height=6, font=("Verdana", 11), 
                           fg="#333333", selectmode=tk.SINGLE,
                           bg="#f0f0f0", width=30)
for item, preco in produtos.items():
    lista_produtos.insert(tk.END, f"{item} - {preco} CC")
canvas.create_window(screen_width//2, 220, window=lista_produtos)

btn_comprar = criar_botao(canvas, "Comprar", comprar, "#4CAF50")
btn_comprar.config(width=20, height=2)
canvas.create_window(screen_width//2, 320, window=btn_comprar)

entrada_valor = tk.Entry(canvas, font=("Verdana", 12), justify='center', 
                         fg="#333333", width=20)
entrada_valor.insert(0, "100")
canvas.create_window(screen_width//2, 370, window=entrada_valor)

btn_adicionar = criar_botao(canvas, "Adicionar Ctrl Cash", adicionar_saldo, "#2196F3")
btn_adicionar.config(width=20, height=2)
canvas.create_window(screen_width//2, 420, window=btn_adicionar)

entrada_retirar = tk.Entry(canvas, font=("Verdana", 12), justify='center', 
                           fg="#333333",  width=20)
canvas.create_window(screen_width//2, 470, window=entrada_retirar)

btn_retirar = criar_botao(canvas, "Retirar Ctrl Cash", retirar_saldo, "#FF5733")
btn_retirar.config(width=20, height=2)
canvas.create_window(screen_width//2, 520, window=btn_retirar)

lbl_inventario = tk.Label(canvas, text="📦 Inventário", 
                         font=("Verdana", 14, "bold"), fg="white", bg="#2196F3")
canvas.create_window(screen_width//2, 580, window=lbl_inventario)

inventario = tk.Listbox(canvas, height=6, font=("Verdana", 11), 
                       fg="#333333", bg="#f0f0f0", selectmode=tk.SINGLE,
                       width=30)
canvas.create_window(screen_width//2, 680, window=inventario)

lbl_total = tk.Label(canvas, text="Total: 0 CC", 
                    font=("Verdana", 12))
canvas.create_window(screen_width//2, 750, window=lbl_total)

# Botão de fullscreen corrigido
btn_fullscreen = tk.Button(canvas, text="⛶", command=toggle_fullscreen,
                           bg="black", fg="white", font=("Verdana", 12), **style_button)
canvas.create_window(screen_width-50, 30, window=btn_fullscreen)

# --- Inicia o aplicativo ---
root.mainloop()
