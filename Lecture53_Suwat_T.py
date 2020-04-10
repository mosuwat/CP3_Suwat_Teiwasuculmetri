def VatCalulator(TotalPrice):
    result = TotalPrice+(TotalPrice*7/100)
    return float(result)

Price = float(input("Enter price: "))
print("You have to pay",VatCalulator(Price),"THB")