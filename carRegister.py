from tkinter import *

def sendInfo():
    name = driverName.get()
    plate = plateCode.get()
    user_type = personOption.get()
    print(f'O motorista se chama: {name}')
    print(f'A placa do carro é: {plate}')
    print(f'Tipo de usuário: {user_type}')

window = Tk()
window.geometry('400x300')
window.title("Cadastro de Veículos")

maintitle = Label(window, text='Cadastro de Veículos', font=("Arial", 16, "bold"))
maintitle.pack(pady=20)

name_frame = Frame(window)
name_label = Label(name_frame, text="Nome:", font=("Arial", 12))
name_label.pack(side=LEFT, padx=5)
driverName = Entry(name_frame)
driverName.pack(side=LEFT, padx=5)
name_frame.pack(pady=5)

plate_frame = Frame(window)
plate_label = Label(plate_frame, text="Placa:", font=("Arial", 12))
plate_label.pack(side=LEFT, padx=5)
plateCode = Entry(plate_frame)
plateCode.pack(side=LEFT, padx=5)
plate_frame.pack(pady=5)

personOption = StringVar(value='')

radio_frame = Frame(window)
studentRadioButton = Radiobutton(radio_frame, text='Estudante', variable=personOption, value='Estudante')
serverRadioButton = Radiobutton(radio_frame, text='Servidor', variable=personOption, value='Servidor')
visitorRadioButton = Radiobutton(radio_frame, text='Visitante', variable=personOption, value='Visitante')

studentRadioButton.pack(side=LEFT, padx=5)
serverRadioButton.pack(side=LEFT, padx=5)
visitorRadioButton.pack(side=LEFT, padx=5)

radio_frame.pack(pady=10)

signUp = Button(window, text='Cadastrar', command=sendInfo)
signUp.pack(pady=20)

window.mainloop()