try:
    with open("sample.txt","r") as f:
        print(f.read())
except FileNotFoundError :
    print("Error: The file 'sample.txt' was not found.")
    option = str(input("Do you want to create the file and then test the program? (Y/N) :"))
    option = option.strip()
    if option == "Y" :
        with open("sample.txt","x") as f:
            lines=["Reading file content.","\nLine 1: This is a sample text file.","\nLine 2: It contains multiple lines"]
            f.writelines(lines)
            print("Now run the program again to check output")
    elif option == "N" :
        print("Thank You!!!")
    else :
        raise ValueError("Please enter either 'Y' or 'N'.")










    



       


