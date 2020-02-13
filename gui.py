from tkinter import Tk, scrolledtext, messagebox, END, Button
from typing import List
from collections import OrderedDict
import re

def create_message(text: str) -> str:
    transactions_raw: List[str] = text.split("\n")
    transactions_clean: List[OrderedDict] = []
    peter: int = 0
    arielle: int = 0
    for transaction in transactions_raw: #transaction: str
        if transaction:
            price: float = float(re.search('[.0-9]+', transaction).group())
            initials_reason_data: List[str] = [_.strip() for _ in re.split('[.0-9]+', transaction)]
            initials: str
            reason: str
            initials, reason= tuple(initials_reason_data)
            reason = reason if reason else "unknown"
            if initials.strip() == "P":
                payer: str = "Peter"
                peter += price
            elif initials.strip() == "A":
                payer: str = "Arielle"
                arielle += price
            else:
                payer: str = "unknown"
                print("Unknown error.")
            transaction_dict: OrderedDict = OrderedDict({"payer": payer,
                                                         "price": price,
                                                         "reason": reason})
            transactions_clean.append((transaction_dict))
    if arielle > peter:
        difference: float = arielle / 2 - peter / 2
        message: str = f"Peter paid ${peter}\nArielle paid ${arielle}\n" \
                       f"And so...\nPeter owes Arielle ${round(difference, 2)}"
    elif peter > arielle:
        difference: float = peter / 2 - arielle / 2
        message: str = f"Peter paid ${peter}\nArielle paid ${arielle}\n" \
                       f"And so...\nArielle owes Peter ${round(difference, 2)}"
    return message

def clicked():
    message: str = create_message(txt.get(0.0, END))
    messagebox.showinfo('Results', message)

root = Tk()
root.title("Peter and Arielle's Budget Calculator :)")
root.geometry('500x250')
txt = scrolledtext.ScrolledText(root,width=60,height=10)
txt.grid(column=1, row=2)
txt.focus()
btn = Button(root, text="Crunch the #s", command=clicked)
btn.grid(column=1, row=3)

root.mainloop()