#expanse tracter project

expenseslist = [] #list of expenses in form of dictionary
print("Welcome to expense Tracker ")

while True:
    print("====Menu====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Veiw Totel Khrcha")
    print("4. Exit")

    choice=int(input("Please Enter Your Choice: "))

#ADD EXPENSE

    if(choice == 1):
        date=input("Enter The Date : ")
        category=input("Enter The Category (Food,Travel,Makup,Books) : ")
        description=input("Give Extra Details : ")
        amount=float(input("Enter The Amount : "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenseslist.append(expense)
        print("\n Done. Expense is Added Successfully")

#2. VIEW ALL EXPENSES
    elif(choice == 2):
        if( len(expenseslist)==0 ):
            print("No Expenses Added.Please You Can Go And Invest Money.")
        else:
            print("===== Your All The Expense =====")  
            count = 1
            for eachinvest in expenseslist:
                print(f"Invest Number{count} => {eachinvest["date"]}, {eachinvest["category"]}, {eachinvest["description"]}, {eachinvest["amount"]}")
                count= count+1

#3. view totel spending

    elif(choice == 3): 
      total= 0
      for eachinvest in expenseslist:
        total=total+eachinvest["amount"]

      print("\n TOTAL INVEST = ",total) 

#4. EXIT        
   
    elif(choice == 4):
        print("thanks you...")
        break
    else:
        print("INVALID CHOICE... TRY AGAIN...")




            

