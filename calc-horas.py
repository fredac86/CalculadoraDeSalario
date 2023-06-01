from tkinter import *
from tkinter import messagebox
import tkinter

def calculate_salary():
    try:
        days_worked = int(days_entry.get())
        hourly_rate = float(rate_entry.get().replace(",","."))

        monthly_salary = days_worked * 8 * hourly_rate

        messagebox.showinfo("Resultado", f"Salário Mensal: R$ {monthly_salary:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Digite valores válidos.")

root = Tk()
root.title("Calculadora de Salário Mensal")


#root.iconbitmap(r"C:\\Users\\Fred\\Desktop\\calc-horas\\icon.ico")
root.configure(bg="SteelBlue3") 

# Função para exibir a imagem no cabeçalho
def show_image():
    image = tkinter.PhotoImage(file="logo.png")
    img_label = Label(root, image = image)
    img_label.grid(row=15, column=0, columnspan=2, pady=10)
    img_label.image = image
    

# Chamada da função para exibir a imagem
show_image()

# Labels
blank_label = Label(root, text="", background="SteelBlue3")
blank_label.grid(row=1, column=0, sticky=E)

days_label = Label(root, text="Número de Dias Trabalhados:", background="SteelBlue3", font=("Comic Sans", 12, "bold"), fg="white")
days_label.grid(row=3, column=0, sticky=E)

rate_label = Label(root, text="Valor da Hora Trabalhada (R$):", background="SteelBlue3", font=("Comic Sans", 12, "bold"), fg="white")
rate_label.grid(row=4, column=0, sticky=E)

# Entradas de dados
days_entry = Entry(root, font=("Comic Sans", 12, "bold"))
days_entry.grid(row=3, column=1)

rate_entry = Entry(root, font=("Comic Sans", 12, "bold"))
rate_entry.grid(row=4, column=1)

# Botão para calcular o salário
calculate_button = Button(root, text="Calcular Salário", command=calculate_salary, font=("Comic Sans", 10, "bold"))
calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

# Definir tamanho fixo da janela e justificar seu conteúdo
root.geometry("800x600")  # Definir largura e altura da janela em pixels
root.grid_columnconfigure(0, weight=1)  # Justificar conteúdo à esquerda
root.grid_columnconfigure(1, weight=1)  # Justificar conteúdo à direita

root.mainloop()





