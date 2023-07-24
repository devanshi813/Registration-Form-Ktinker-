from mydatabase import myDB

def main():
    db = myDB()
    while True:
        print("press 1 to insert new user")
        print("press 2 to display all user")
        print("press 3 to delete user")
        print("press 4 to update user")
        print("press 5 to exit program")
        print()

        try:
            choice = int(input())
            if(choice==1):
                #insert user
                userId = int(input("Enter user Id: "))
                userName = input("Enter user name: ")
                userPhone = input("Enter user phone: ")
                db.insert_user(userId,userName,userPhone)               
                
            elif choice == 2:
                #display user
                db.fetch_all()

            elif choice == 3:
                #delete user
                userid = int(input("enter user id id you want to delete"))
                db.delete_user(userid)

            elif choice == 4:
                #update user
                userId = int(input("Enter user Id: "))
                userName = input("new name: ")
                userPhone = input("new phone: ")
                db.update_user(userId,userName,userPhone)

            elif choice == 5:
                break
            else:
                print("Invalid input! Try again")

        except Exception as e:
            print(e)
            print("Invalid Details ! Try again")

        
if __name__ == "__main__":
    main()
