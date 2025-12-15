with open("output.txt","w") as o :
    input_text = str(input("Enter text to write to the file: "))
    o.write(input_text)
    print("Data successfully written to output.txt.")
print("\n")
with open("output.txt","a") as o :
    additional_text = str(input("Enter additional text to append: "))
    o.write("\n")
    o.write(additional_text)
    print("Data successfully appended.")
print("\n")
with open("output.txt","r") as o :
    read_text = o.read()
    print(f"Final content of output.txt: \n{read_text}")











    



       



