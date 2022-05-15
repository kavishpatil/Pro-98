def SwapFileData():
    File1 = input("Enter file name to be swapped:")
    File2 = input("Enter the 2nd filr name to be swapped:")

    with open(File1,'r') as a:
        data_a = a.read()

    with open(File2,'r') as b:
        data_b = b.read()

    with open(File1,'w') as a:
        a.write(data_b)

    with open(File2,'w') as b:
        b.write(data_a)

SwapFileData()
        