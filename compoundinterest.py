rate = 0.05
amount = 1000
years = 0
while years<10:
    amount = (amount*0.05)+amount
    years+=1
    print(amount, "for years", years)