from loading import load_elements, anumber, load_number
from functions import e_config, valence_electrons, classify_elements, trim_zero, decimal_num, non_decimal
if __name__ == "__main__":
    command = ""
    while command != "quit":
        command = ""
        user_r = input("What do you want to learn about? elements or significant numbers:")
        if user_r == "elements":
            e_name = input("Please enter the element name: ")
            if anumber(load_elements(), e_name) > 0:
                while command not in ["classification", "electronic configuration", "valence electrons", "quit"]:
                    command = input(f"What do you want to learn about {e_name} : classification, electronic configuration, valence electrons ? Enter 'quit' to exit : ")
                    if command.lower() == "classification":
                        print(classify_elements(anumber(load_elements(), e_name)))
                    elif command.lower() == "electronic configuration":
                        print(e_config(anumber(load_elements(), e_name), e_name))
                    elif command.lower() == "valence electrons":
                        print(valence_electrons(e_config(anumber(load_elements(), e_name), e_name)))
                    elif command != "quit":
                        print("INVALID COMMAND")
        elif user_r == "significant numbers":
            nums = input("Type the number whose significant digit you want to find:")
            num = load_number(nums)
            if "." in num:
                print(decimal_num(trim_zero(num)))
            elif "." not in num:
                print(non_decimal(trim_zero(num)))


