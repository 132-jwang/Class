import myclass
owner1= input("What is your name?")
acct1 = myclass.Account(owner1,100)

dep1= int(input("How much do you want to deposit?"))
wit1= int(input("How much do you want to withdrawl?"))
acct1.deposit(dep1)
acct1.withdrawl(wit1)


print(acct1.owner, acct1.balance)
acct1.balance = acct1.balance*1.05
print(acct1._str_())
