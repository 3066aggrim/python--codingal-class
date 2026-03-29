def shutdown():
    user_input = input("Do you want to shut down the system? (yes/no): ")

    if user_input.lower() == "yes":
        print("Shutting down...")

    elif user_input.lower() == "no":
        print("Abort shutting down.")

    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


shutdown()
