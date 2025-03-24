from tkinter import *
import psycopg2 
from tkinter import messagebox
from tkinter import ttk

def sendInfo():
    name = driverName.get()
    plate = plateCode.get()
    user_type = personOption.get()

    print(f'O motorista se chama: {name}')
    print(f'A placa do carro é: {plate}')
    print(f'Tipo de usuário: {user_type}')

    # Conectar ao banco de dados
    connect = psycopg2.connect(
        dbname="sistemacadastro",
        user="postgres",
        host="localhost",
        password="postgres",
        port="5432"
    )

    cursor = connect.cursor()

    check_query = f"""
        SELECT 1 FROM Estudantes WHERE plateCode = %s
        UNION
        SELECT 1 FROM Servidores WHERE plateCode = %s
        UNION
        SELECT 1 FROM Visitantes WHERE plateCode = %s;
    """
    cursor.execute(check_query, (plate, plate, plate))
    existing_plate = cursor.fetchone()

    if existing_plate:
        messagebox.showerror("Erro", "Esta placa já está cadastrada no sistema!")
    else:
        
        if user_type == 'Estudante':
            query = f"""
                INSERT INTO Estudantes(fullName, plateCode)
                VALUES (%s, %s);
            """
            cursor.execute(query, (name, plate))

        if user_type == 'Servidor':
            query = f"""
                INSERT INTO Servidores(fullName, plateCode)
                VALUES (%s, %s);
            """
            cursor.execute(query, (name, plate))

        if user_type == 'Visitante':
            query = f"""
                INSERT INTO Visitantes(fullName, plateCode)
                VALUES (%s, %s);
            """
            cursor.execute(query, (name, plate))

        connect.commit()
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

    connect.close()

    driverName.delete(0, END)
    plateCode.delete(0, END)
    personOption.set('')

def removeInfo():
    plate = removePlateCode.get()

    if not plate:
        messagebox.showerror("Erro", "Por favor, insira uma placa válida!")
        return

    connect = psycopg2.connect(
        dbname="sistemacadastro",
        user="postgres",
        host="localhost",
        password="postgres",
        port="5432"
    )

    cursor = connect.cursor()

    check_query = f"""
        SELECT 1 FROM Estudantes WHERE plateCode = %s
        UNION
        SELECT 1 FROM Servidores WHERE plateCode = %s
        UNION
        SELECT 1 FROM Visitantes WHERE plateCode = %s;
    """
    cursor.execute(check_query, (plate, plate, plate))
    existing_plate = cursor.fetchone()

    if not existing_plate:
        messagebox.showerror("Erro", "Esta placa não está cadastrada no sistema!")
    else:
        delete_query = f"""
            DELETE FROM Estudantes WHERE plateCode = %s;
            DELETE FROM Servidores WHERE plateCode = %s;
            DELETE FROM Visitantes WHERE plateCode = %s;
        """
        cursor.execute(delete_query, (plate, plate, plate))
        connect.commit()
        messagebox.showinfo("Sucesso", "Indivíduo removido com sucesso!")

    connect.close()
    removePlateCode.delete(0, END)

# Código Interface Gráfica
window = Tk()
window.geometry('400x350')
window.title("Cadastro de Veículos")

notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=1)

cadastro_frame = Frame(notebook)
notebook.add(cadastro_frame, text="Cadastro")

maintitle = Label(cadastro_frame, text='Cadastro de Veículos', font=("Arial", 16, "bold"))
maintitle.pack(pady=20)

name_frame = Frame(cadastro_frame)
name_label = Label(name_frame, text="Nome:", font=("Arial", 12))
name_label.pack(side=LEFT, padx=5)
driverName = Entry(name_frame)
driverName.pack(side=LEFT, padx=5)
name_frame.pack(pady=5)

plate_frame = Frame(cadastro_frame)
plate_label = Label(plate_frame, text="Placa:", font=("Arial", 12))
plate_label.pack(side=LEFT, padx=5)
plateCode = Entry(plate_frame)
plateCode.pack(side=LEFT, padx=5)
plate_frame.pack(pady=5)

personOption = StringVar(value='')

radio_frame = Frame(cadastro_frame)
studentRadioButton = Radiobutton(radio_frame, text='Estudante', variable=personOption, value='Estudante')
serverRadioButton = Radiobutton(radio_frame, text='Servidor', variable=personOption, value='Servidor')
visitorRadioButton = Radiobutton(radio_frame, text='Visitante', variable=personOption, value='Visitante')

studentRadioButton.pack(side=LEFT, padx=5)
serverRadioButton.pack(side=LEFT, padx=5)
visitorRadioButton.pack(side=LEFT, padx=5)

radio_frame.pack(pady=10)

signUp = Button(cadastro_frame, text='Cadastrar', command=sendInfo)
signUp.pack(pady=20)

remover_frame = Frame(notebook)
notebook.add(remover_frame, text="Remover")

remove_title = Label(remover_frame, text='Remoção de Veículos', font=("Arial", 16, "bold"))
remove_title.pack(pady=20)

remove_plate_frame = Frame(remover_frame)
remove_plate_label = Label(remove_plate_frame, text="Placa:", font=("Arial", 12))
remove_plate_label.pack(side=LEFT, padx=5)
removePlateCode = Entry(remove_plate_frame)
removePlateCode.pack(side=LEFT, padx=5)
remove_plate_frame.pack(pady=5)

removeButton = Button(remover_frame, text='Remover', command=removeInfo)
removeButton.pack(pady=20)

window.mainloop()
