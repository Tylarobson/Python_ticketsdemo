from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()

        self.title("Tickets")
        self.configure(padx=10, pady=10)

        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
    
    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure (  font="Arial 24",
                                        text="Entrance Ticket")

    def __add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.grid (row=1, column=0, sticky=W)
        self.instruction_label.configure(text="How many tickets are needed?")

    def __add_tickets_entry(self):
        self.tickets_entry = Entry()
        self.tickets_entry.grid(row=2, column=0, pady=10)

    def __add_buy_button(self):
        self.buy_button = Button()
        self.buy_button.grid(row=3, column=0)
        self.buy_button.configure(text="buy")
        self.buy_button.configure(text="Submit")
        self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)

    def __buy_button_clicked(self, event):
        messagebox.showinfo("Purchased!", "You have purchased the ticket")
