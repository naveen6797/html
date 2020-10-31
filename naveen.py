import os
def account_creation(a,b,c,d):
    data = "{},{},{},{},{}".format(a,b,c,d,"OPEN")
    file_name = "{}".format(a + ".txt")

    cwd = os.getcwd()
    ac = os.listdir(cwd)
    for each_line in ac:
        if file_name == each_line:
            print("account already created")
            break
    else:
        f = open(file_name , 'a+')
        f.write(data)
        print("your account created")
        f.close()

def money_withdraw():
    account_name = input("enter your account_name:")
    searching_user_account = "{}".format(account_name + ".txt")
    cwd = os.getcwd()
    ac = os.listdir(cwd)
    B = 0
    for each_file in ac:
        if searching_user_account == each_file:
            f = open(each_file)
            file_line = f.readline()
            account_check = file_line.split(",")[4].strip()
            A1 = "{}".format("OPEN")
            if account_check == A1:
                withdraw_amount = int(input("enter your withdraw amount:"))
                customer_account_balance = int(file_line.split(",")[2])
                if customer_account_balance >= withdraw_amount:
                    p = file_line.split(",")[0]
                    q = file_line.split(",")[1]
                    r = int(file_line.split(",")[2])
                    s = file_lines.split(",")[3]
                    t = file_line.split(",")[4].strip()
                    u = r - withdraw_amount
                    file_lines = "{},{},{},{},{}".format(p,q,u,s,t)
                    B = 1
                    print("name:",account_name,"\n""your current balance is :",p,"\n",file_lines)
                else:
                    print("insufficient_balance")
            else:
                print("your account closed")
            break
    f.close()
    if B == 1:
        
        for x in ac:
            if searching_user_account == x:
                f = open(x, 'w')
                f.seek(0)
                f.write(file_lines)
                break
        f.close()
                
        
            
                

                        
    
    

print("""1.account_creation:
2.amount_withdraw:
3.amount_deposite:
4.card_deposite:
5.card_withdraw:
6.close_account:""")
choice = int(input("enter your choice:"))
if choice == 1:
    account_name = input("enter your account_name:")
    account_number = input("enter your account_number:")
    account_balance = input("enter your account_balance:")
    debit_card_pin = input("enetr your debit_card_pin:")
    account_creation(account_name, account_number, account_balance, debit_card_pin)

if choice == 2:
    money_withdraw()
