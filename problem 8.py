#problem 8
#olivia g 10/2/20
#setting the constants - exchange rates
USD = 1.154
AUD = 1.22
#input- balances in the accounts
usbal = float(input("What is the balance in the US account? "))
aubal = float(input("What is the balance in the AUS account? "))
#process - calculations (converting to nzd)
nz_usbal = usbal * USD
nz_aubal = aubal * AUD
nz_bal = nz_usbal + nz_aubal
#output - printing the nzd values and final balance
print("--------------------")
print("US${:.2f} exchanges to NZ${:.2f}".format(usbal, nz_usbal))
print("AUS${:.2f} exchanges to NZ${:.2f}".format(aubal, nz_aubal))
print()
print("NZ balance: ${:.2f}".format(nz_bal))
