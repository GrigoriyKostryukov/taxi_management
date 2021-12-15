from tkinter import *
import psycopg2

# postgresql-cubic-98264

root = Tk()
root.title('Сервис такси')
root.geometry("500x550")


def query():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="test_db",
        user="grigoriy",
        password="12345",
        port="5432"
    )

    c = conn.cursor()


    conn.commit()
    conn.close()


def submit():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="test_db",
        user="grigoriy",
        password="12345",
        port="5432"
    )

    c = conn.cursor()
    c.execute('''INSERT INTO customers (first_name, last_name)
    VALUES (%s, %s)
    ''', (f_name.get(), l_name.get()))
    conn.commit()
    conn.close()
    update()


def update():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="test_db",
        user="grigoriy",
        password="12345",
        port="5432"
    )

    c = conn.cursor()
    c.execute("SELECT * FROM customers")
    records = c.fetchall()
    output = ''
    for record in records:
        output_label.config(text=f'{output}\n{record[0]} {record[1]}')
        output = output_label['text']
    conn.close()

# Create The GUI For The App
my_frame = LabelFrame(root, text="Postgres Example")
my_frame.pack(pady=20)

f_label = Label(my_frame, text="First Name:")
f_label.grid(row=0, column=0, pady=10, padx=10)

f_name = Entry(my_frame, font=("Helvetica, 18"))
f_name.grid(row=0, column=1, pady=10, padx=10)

l_label = Label(my_frame, text="Last Name:")
l_label.grid(row=1, column=0, pady=10, padx=10)

l_name = Entry(my_frame, font="Helvetica, 18")
l_name.grid(row=1, column=1, pady=10, padx=10)

submit_button = Button(my_frame, text="Submit", command=submit)
submit_button.grid(row=2, column=0, pady=10, padx=10)

update_button = Button(my_frame, text="Update", command=update)
update_button.grid(row=2, column=1, pady=10, padx=10)

output_label = Label(root, text="")
output_label.pack(pady=50)

query()
root.mainloop()
