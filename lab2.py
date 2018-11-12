from tkinter import *
import sqlite3


def init_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE stocks
                (date TEXT, trans TEXT, name TEXT, qty REAL, price REAL)''')
        conn.commit()
        conn.close()
    except:
        pass


class App:
    def __init__(self, master):

        frame = Frame(master, bg="green")

        frame.pack(fill=BOTH)

        self.quit_button = Button(frame, text="QUIT", fg="red", command=self.exitt)
        self.quit_button.pack(side=LEFT)
        self.select_button = Button(frame, text="Select", fg="blue", command=self.say_hi)
        self.select_button.pack(side=LEFT)

        self.select_button = Button(frame, text="Find", fg="gray", command=self.fetch)
        self.select_button.pack(side=LEFT)

        self.name_field = Text(frame, height=1, width=35, font='Arial 10', wrap=WORD)
        self.name_field.pack(side=RIGHT)

        self.records_text = Message(root, width=300)
        self.records_text.place(x=150, y=150)

        self.names = ['Carl', 'Patrick', 'Lindsay', 'Helmut', 'Chris', 'Gwen']
        self.listbox = Listbox(root)  # Create 2 listbox widgets
        for item in self.names:
            self.listbox.insert(0, item)

        self.listbox.place(x=22, y=150)

        form_fields = 'Transaction Type', 'Quantity', 'Price'
        entries = self.generate_input_fields(form_fields)
        root.bind('<Return>', (lambda event, e=entries: self.insert_record(entries)))
        insert_button = Button(root, text='Insert',
                               command=(lambda e=entries: self.insert_record(entries)))
        insert_button.pack(side=RIGHT, padx=5, pady=5)

        init_db()

    def insert_record(self, entries):
        for entry in entries:
            field = entry[0]
            text = entry[1].get()
            print('%s: "%s"' % (field, text))

        conn = sqlite3.connect('example.db')
        c = conn.cursor()

        selection = self.listbox.curselection()
        if len(selection) is 0:
            return
        name = self.listbox.get(self.listbox.curselection())
        print('Name: "%s"' % name)

        now = sqlite3.datetime.datetime.now()
        sql = "INSERT INTO stocks (date, trans, name, qty, price) VALUES ('%s','%s','%s','%s','%s')" % (
            now.strftime("%Y-%m-%d"), entries[0][1].get(), name, entries[1][1].get(),
            entries[2][1].get())
        c.execute(sql)
        conn.commit()
        conn.close()

    def generate_input_fields(self, fields):
        entries = []
        for field in fields:
            row = Frame(root)
            lab = Label(row, width=15, text=field, anchor='w')
            ent = Entry(row)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries.append((field, ent))
        return entries

    def say_hi(self):
        selection = self.listbox.curselection()
        if len(selection) is 0:
            return
        self.name_field.delete('1.0', END)
        self.name_field.insert(1.0, self.listbox.get(self.listbox.curselection()))

    def exitt(self):
        root.destroy()

    def fetch(self):
        conn = sqlite3.connect('example.db')
        c = conn.cursor()

        selection = self.listbox.curselection()
        if len(selection) is 0:
            return
        name = self.listbox.get(self.listbox.curselection())

        result = ''
        for row in c.execute("SELECT * FROM stocks WHERE name = '%s'" % name):
            print(row)
            result += str(row) + '\n'
            break
        if result == '':
            result = "None"
        self.records_text.configure(text=result)


# ++++++++++++++++++++++++++++
root = Tk()
root.geometry("600x400")
app = App(root)

root.mainloop()
