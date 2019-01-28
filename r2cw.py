# Creating my own TaskList.


# 1. List all tasks.
# 2. Add a task to the list.
# 3. Delete a task.
# 0. To quit the program
def main():
    print("Congratulations You are running Enricka's task list.")
    print("What do you want to do next?")
    arraryoftasks=["clean house","Bank Run","Wash Car"]
    userInput=-1
    num1= "List all task"
    num2="Add a task to the list."
    num3="Delete a task"
    num0="Try to quit program"

    while userInput!=0:
        userInput=int(input("enter a number 0-3."))


        if userInput==1:
            print (arraryoftasks)
        elif userInput == 2:
            yourinput=input("add a task.")
            arraryoftasks.append(yourinput)
            print(arraryoftasks)

        elif userInput ==3:
            yourinput=input('remove ')
            for el in arraryoftasks:
                print(el)
            arraryoftasks.remove(yourinput)
            print(arraryoftasks)





















if __name__ == '__main__':
    main()


