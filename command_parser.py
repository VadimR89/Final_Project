from functions import *
from error_handl_decorator import error_handling_decorator

# commands parser, which calls the functions providing needed arguments
@error_handling_decorator
def parse_input(user_input):
    user_input = check_command(user_input, commands)
    for request in commands:  # dict with commands
        if user_input.startswith(request):
            func = commands[request]

            if func == add_contact:
                name = name_input_for_add()
                new_phone_number = phone_input()
                birth_date = dob_input()
                email = email_input()
                address = input('please provide an address: ')
                note = input('please provide a note: ')
                return func(name, new_phone_number, birth_date, email, address, note)
            
            elif func == show_contact:
                name = input('please provide a contact name: ')
                return func(name)
            
            elif func == change_info:
                name = name_input()
                info_to_amend = input('what type of information will be amended (phone / birthday / email / address / note): ')
                contact = phone_book.get(name) ###

                if info_to_amend == 'phone':
                    print("Please choose index of the phone to be amended:") 
                    old_phone_number = str(phone_index_input(contact)) ###
                    new_phone_number = phone_input()
                    return change_phone(name, new_phone_number, old_phone_number)
                
                elif info_to_amend == 'birthday':
                    birth_date = dob_input()
                    return add_contact(name, birthday=birth_date)
                
                elif info_to_amend == 'email':
                    email == email_input()
                    return add_contact(name, email=email)

                elif info_to_amend == 'address':
                    address = input('please provide the new address: ')
                    return add_contact(name, address=address)

                elif info_to_amend == 'note':
                    note = input('please provide the new note: ')
                    return add_contact(name, note=note)           
                    
                elif info_to_delete != 'phone' and info_to_delete != 'birthday' and info_to_delete != 'email' and info_to_delete != 'address' and info_to_delete != 'note':
                    raise CustomError ("please provide valid field to amend")
                
            

            elif func == show_page:
                page = input('please provide the page to display: ')
                return func(page)
            
            elif func == remove_contact:
                name = name_input()
                return func(name)

            elif func == remove_info: 
                name = name_input()
                contact = phone_book.get(name) ###
                info_to_delete = input('what type of information will be deleted (phone / birthday / email / address / note): ')
                if info_to_delete == 'phone':
                    print("Please choose index of the phone to be removed:")
                    phone_number = str(phone_index_input(contact)) ###
                    return func(name, info_to_delete, phone_number)
                
                elif info_to_delete != 'phone' and info_to_delete != 'birthday' and info_to_delete != 'email' and info_to_delete != 'address' and info_to_delete != 'note':
                    raise CustomError ('please provide valid field to be deleted')
                
                return func(name, info_to_delete)
            
            elif func == search:
                search_word = input('please provide a search request: ')
                return func(search_word)
            
            elif func == dtb:
                name = name_input()
                return func(name)
            
            elif func == show_birthdays_soon:
                  while True:
                    try:
                        days = int(input('Enter the number of days: '))
                        break  # Вихід із циклу, якщо користувач ввів число правильно
                    except ValueError:
                        print("Please enter a valid number.")

                  return func(days)
            
            
            #Notes commands
            elif func == add_note:
                text = input_note_params("text")
                tags = input_note_params("tags")
                return func(text, tags)

            elif func == delete_note:
                id = input_note_params("id")
                return func(id)

            elif func == edit_text:
                id = input_note_params("id")
                text = input_note_params("text")
                return func(id, text)

            elif func == delete_tag:
                id = input_note_params("id")
                tag = input_note_params("tag")
                return func(id, tag)

            elif func == add_tags:
                id = input_note_params("id")
                tags = input_note_params("tags")
                return func(id, tags)
            
            elif func == find_by_tag:
                tags = input_note_params("tags")
                show_desc = input_note_params("show_desc")
                return func(tags, show_desc)
            #end notes commands

            
            elif func == sort_files:
                folder_path = path_input()
                return func(folder_path)

            elif func == send_sms:
                contact_name = name_input()
                contact = phone_book.get(contact_name)
                if contact:
                    message = input("Enter the SMS message: ")
                    
                    phone = phone_index_input(contact)
                    print(f'Sending sms to the number {phone}')
                    result = func(phone, message)
                    print(result)
                    return None
                else:
                    return "Contact not found"
                

            elif func == call:
                contact_name = name_input()
                contact = phone_book.get(contact_name)
                if contact:
                    message = input("Enter the message: ")
                    
                    phone = phone_index_input(contact)
                    print(f'Calling to the number {phone}')
                    result = func(phone, message)
                    print(result)
                    return None
                else:
                    return "Contact not found"


            else:  #run func which don't need args. eg.hello, help, show all
                return func()

    raise CustomError("please provide a valid command")
