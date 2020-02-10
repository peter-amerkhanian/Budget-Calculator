import re
from typing import List

with open("text.txt") as f:
    transactions_raw: List[str] = f.read().split("\n")
    transactions_clean: List[dict] = []
    peter: int = 0
    arielle: int = 0
    for transaction in transactions_raw:
        price: float = float(re.search('[.0-9]+', transaction).group())
        _other: List[str] = [_.strip() for _ in re.split('[.0-9]+', transaction)]
        initials, reason= tuple(_other) # initials: str, reason: str
        reason = reason if reason else "unknown"
        payer: str = "Peter" if initials.strip() == "P" else "Arielle"
        if payer == "Peter":
            peter += price
        elif payer == "Arielle":
            arielle += price
        else:
            print("Unknown error.")
        print(f"{payer}: {price} for {reason}")
    print(f"Peter paid {peter}")
    print(f"Arielle paid {arielle}")

