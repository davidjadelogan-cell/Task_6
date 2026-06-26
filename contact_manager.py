print("WELCOME TO THE BLS CONTACT MANAGER APP.")
# This block is where variables holding a data set sre defined (e.g sets, lists or dictionaries)
start = True
contacts = {}
phone_numbers = set()
emails = set()
role_list = ["Student", "Staff", "Parent"]
# This block contains the start of the loop and where the service feature of the program starts
while start:
    print("\nMENU")
    print("1. Add contacts \n2. Update Contacts \n3. Delete Contacts.\n4. Search Contacts\n5. List of Contacts\n6. Exit")
    action = input("What do you want to do: ").lower()
    # This block is where the addition of a contact and validation of the contact added is done
    if action == "1":
       unique_id = input("\nplease enter your ID: ").upper()
       name = input("please enter your full Name: ").title()
       phone_number = input("please enter your Phone Number: ")
       email = input("please enter your Email: ").lower()
       role = input("please enter your Role: ").capitalize()

       if not phone_number.isdigit():
           print("Please phone numbers must be in number, please try again.")
       else:
            if len(phone_number) != 11:
                print("Phone numbers must be exactly 11 digits")
            elif "@" not in email or "." not in email:
                print("Please enter a valid email")
            else:
                if unique_id in contacts:
                    print("Sorry this ID is exists already")
                elif phone_number in phone_numbers:
                    print("Sorry this phone number already exists")
                elif email in emails:
                    print("Sorry this Email already exists")
                elif role not in role_list:
                    print("This role isn't available")
                else:
                    contacts[unique_id] = {
                                                "Full Name" : name,
                                                "Phone Number" : phone_number,
                                                "Email" : email,
                                                "Role" : role
                                                }
                    phone_numbers.add(phone_number)
                    emails.add(email)
                    print("Contact has been added successfully")
# This block is where the updating of contact and validation of the contact updated is done. 
    elif action == "2":
        update = input("\nEnter your ID: ").upper()
        if update not in contacts:
            print("Sorry this ID does not exist")
        else:
        # This is where the user selects fields they want to update.
            print("\nContact Fields\n1. Name\n2. Phone Number\n3. Email\n4. Role")
            update1 = input("Enter the field you want to update: ")
            if not update1.isdigit():
                print("Please enter a number attached to the what you want to update")
            else:
                update1 = int(update1)
                if update1 == 1:
                    current_name = contacts[update]["Full Name"]
                    print(f"\nYour current name is {current_name}")
                    new_name = input("Please enter new name: ").title()
                    contacts[update]["Full Name"] = new_name
                    print("Name has been updated successfully")
                elif update1 == 2: 
                    current_phone_number_check = input("\nPlease enter current phone number: ")
                    current_phone_number = contacts[update]["Phone Number"]
                    if current_phone_number_check == current_phone_number:
                        new_phone_number = input("Please enter new phone number: ")
                        if not new_phone_number.isdigit():
                            print("Please phone number must be in numbers")
                        else: 
                            if new_phone_number == current_phone_number:
                                print("This is the current number, please enter a new number")
                            elif new_phone_number in phone_numbers:
                                print("This phone number already exist")
                            elif len(new_phone_number) != 11:
                                print("Phone number must be exactly 11 digits")
                            else: 
                                phone_numbers.remove(current_phone_number)
                                contacts[update]["Phone Number"] = new_phone_number
                                phone_numbers.add(new_phone_number)
                                print("Phone Number has been updated sucessfully")
                    else:
                        print("Wrong Phone number, please try again")
                elif update1 == 3:
                    current_email_check = input("\nPlease enter current Email: ")
                    current_email = contacts[update]["Email"]
                    if current_email_check == current_email:
                        new_email = input("Please enter new Email: ").lower()
                        if new_email == current_email:
                            print("This is the current Email, please enter a new mail.")
                        elif new_email in emails:
                            print("This Email has already been taken ")
                        elif "@" not in new_email or "." not in new_email:
                            print("Please enter a valid Email")
                        else:
                            emails.remove(current_email)
                            contacts[update]["Email"] = new_email
                            emails.add(new_email)
                            print("Email has been updated successfully")
                    else: 
                        print("Wrong Email, please enter correct email")
                elif update1 == 4:
                    current_role = contacts[update]["Role"]
                    print(f"\nYour current role is {current_role}")
                    new_role = input("Please enter new role: ").capitalize()
                    if new_role not in role_list:
                        print("This role isn't available.")
                    elif new_role == current_role:
                        print("This is current role.")
                    else:
                        contacts[update]["Role"] =  new_role
                        print("Role has been updated successfully.")
                else: 
                    print("Invalid option, please select a valid option.")
    # This block is where the deletion of a contact and validation of the contact being deleted is done
    elif action == "3":
        delete = input("\nEnter ID to be deleted: ").upper()
        if delete in contacts:
            delete_email = contacts[delete]["Email"]
            delete_number = contacts [delete]["Phone Number"]
            emails.remove(delete_email)
            phone_numbers.remove(delete_number)
            del contacts[delete]
            print("Contact has been deleted successfully")
        else:
            print("This ID does not exist.")
    # This block is where the search of a contact and validation of the contact being searched is done
    elif action == "4":
        search_id = input("\nSearch ID: ").upper()
        if search_id in contacts:
            contact = contacts[search_id]
            print()
            print(f"\nID: {search_id}")
            for key, value in contact.items():
                print(f"{key}: {value}")
        else:
            print("This ID does not exist")
    # This block is where the viewing of available contacts and validation of the list feature is done
    elif action == "5":
        if not contacts:
            print("\nNo contacts available")
        else:
            for unique_id, contact in contacts.items():
                print(f"\nID: {unique_id}")
                for key, value in contact.items():
                    print(f"{key}: {value}")
    # This is used to exit the loop 
    elif action == "6":
        print("\nThank you for using BLS Contact Manager App")
        start = False
    else:
        print("\nInvalid option, please enter a valid option")







