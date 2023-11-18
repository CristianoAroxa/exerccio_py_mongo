import tkinter as tk

import pymongo

class CRUD(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.master.title("CRUD")

        self.attributes = ["marca", "modelo", "cor", "preço", "ano"]

        self.table = tk.Treeview(self)
        self.table.pack()

        for attribute in self.attributes:
            self.table.column(attribute, width=100)
            self.table.heading(attribute, text=attribute)

        self.load_data()

        self.insert_btn = tk.Button(self, text="Inserir", command=self.insert)
        self.insert_btn.pack()

        self.consult_btn = tk.Button(self, text="Consultar", command=self.consult)
        self.consult_btn.pack()

        self.delete_btn = tk.Button(self, text="Excluir", command=self.delete)
        self.delete_btn.pack()

        self.update_btn = tk.Button(self, text="Alterar", command=self.update)
        self.update_btn.pack()

    def load_data(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        database = client["celular"]
        collection = database["celulares"]

        for celular in collection.find():
            self.table.insert("", "end", values=celular)
