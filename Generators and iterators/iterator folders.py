from pathlib import Path

p = Path(r"C:\Users\mastermor\Desktop\programms")
for child in p.iterdir(): print(str(child))

