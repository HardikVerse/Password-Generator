import random
import string




print("Value must be between 3 and 128. Use 14 characters or more to generate a strong password.\n")



user_input = int(input("Enter length of password: "))
        

if user_input not in range(3, 129):
    print("\nPlease, enter length in between 3 and 128.")


else:
    if user_input < 8:
        print("Strength: Weak")
    elif user_input < 14:
        print("Strenght: Medium")
    else:
        print("Strength: Strong")

    print("\nPress 1 to Select and 0 to Deselect\n")

    A_to_Z = int(input("A-Z in password: "))
    a_to_z = int(input("a-z in password: "))
    numbers = int(input("0-9 in password: "))
    special_word = int(input("!@#$%^&* in password: "))


    if not all(x in (0,1) for x in [A_to_Z, a_to_z, numbers, special_word]):
            print("\nPlease enter digit either 1 or 0.\n")

        
    elif all(x == 0 for x in [A_to_Z, a_to_z, numbers, special_word]):
            print("\nPlease select atleast one option.")
            
    else:

        option = {
            string.ascii_uppercase: A_to_Z,
            string.ascii_lowercase: a_to_z,
            string.digits: numbers,
            "!@#$%^&*": special_word
        }


        selected_option = [key for key, value in option.items() if value == 1]
        final_string = "".join(selected_option)


        def pass_generator(character, length):
            password = random.choices(character, k=length)
            result = "".join(password)
            return f"\nHere is your password: {result}\n"
        while True:
            print(pass_generator(final_string, user_input))
            gen_again = input("Generate another password? (y/n):" )
            if gen_again == "n":
                break
            

