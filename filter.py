import re
from typing import List
from collections import OrderedDict

with open("text.txt") as f:
    transactions_raw: List[str] = f.read().split("\n")
    transactions_clean: List[OrderedDict] = []
    peter: int = 0
    arielle: int = 0
    for transaction in transactions_raw:
        price: float = float(re.search('[.0-9]+', transaction).group())
        _other: List[str] = [_.strip() for _ in re.split('[.0-9]+', transaction)]
        initials, reason= tuple(_other) # initials: str, reason: str
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
    print(f"Peter paid ${peter}")
    print(f"Arielle paid ${arielle}")
    print("And so...")
    if arielle > peter:
        difference: float = arielle/2 - peter/2
        print(f"Peter owes Arielle ${round(difference, 2)}")
    elif peter > arielle:
        difference: float = peter / 2 - arielle / 2
        print(f"Arielle owes Peter ${round(difference, 2)}")

