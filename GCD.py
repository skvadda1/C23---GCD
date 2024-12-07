numberLargest = int(input("What is the large number:"))
numberSmallest = int(input("What is the small number"))
while numberSmallest:
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is:" , numberLargest)