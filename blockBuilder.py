##Take user input
height = int(input("Enter block height: "))

##Build rows
for i in range(0, (height + 1)):
    ##Build columns
    for j in range(0, i):
        ##Place blocks
        print("#", end="")
    ##Move to next row
    print()