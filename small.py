# while True:
#     try:
#         user_input= int(input("Enter the number of file: "))

#         if user_input <=0:
#             print("Enter a valid number")
#             continue
                   

#         for number in range(1,user_input+1):
#             filename = f"file{number}.txt"

           

#             with open(filename, "w") as file:
#                 file.write("my first script")
#         print("file created successfuly!")
#         break

#     except ValueError:
#         print("enter valid number")


import os
while True:
    try:

        collet = int(input("enter number you want to delete"))

        if collet <= 0:
            print("enter correct number")
            continue

        for number in range (1, collet +1):
            filename = f"file{number}.txt"

            if os.path.exists(filename):
                os.remove(filename)
                print(f"{filename} deleted successfully")
                
                
               
            else:

                print(f"{filename} does not exist ")
        break

    except ValueError:
        print("enter a digit")
      
        
