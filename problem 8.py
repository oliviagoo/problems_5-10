#problem 8
#olivia g 10/2/20

USD = 1.154
AUD = 1.22

usbal = float(input("What is the balance in the US account? "))
aubal = float(input("What is the balance in the AUS account? "))

nz_usbal = usbal * USD
nz_aubal = aubal * AUD
nz_bal = nz_usbal + nz_aubal

print("--------------------")
print("US${:.2f} exchanges to NZ${:.2f}".format(usbal, nz_usbal))
print("AUS${:.2f} exchanges to NZ${:.2f}".format(aubal, nz_aubal))
print()
#print("NZ balance: ${:.2f}")
