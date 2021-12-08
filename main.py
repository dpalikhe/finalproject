from dikchhya import load_elements, anumber
from Classify import e_config, valence_electrons, classify_elements
if __name__ == "__main__":
    command=""
    while command!="quit":
        command=""
        e_name = input("Please enter the element name: ")
        if anumber(load_elements(),e_name)>0:
            while command not in ["classification", "electronic configuration", "valence electrons", "quit"]:
                command = input(
                    f"What do you want to learn about {e_name}: classification, electronic configuration or valence electrons? Enter 'quit' to exit: ")
                if command.lower() == "classification":
                    print(classify_elements(anumber(load_elements(),e_name)))
                elif command.lower() == "electronic configuration":
                    print(e_config(anumber(load_elements(),e_name), e_name))
                elif command.lower() == "valence electrons":
                    print(valence_electrons(e_config(anumber(load_elements(),e_name), e_name)))
                elif command != "quit":
                    print("INVALID COMMAND")
