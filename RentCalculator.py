persons=int(input("Enter number of persons :"))
rent=int(input("Enter total rent of the flat :"))
food=int(input("Enter total cost of food :"))
electicity=float(input("Enter unit of electricity spend :"))
charge=int(input("Enter charge per unit of electricity :"))
each=(rent+food+electicity*charge)/persons
print(f"Each person will pay bill of {each}")