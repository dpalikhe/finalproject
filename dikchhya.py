import csv
def load_elements():
    fv = open("Elements_list.csv", "r")
    dialect = csv.Sniffer().sniff(fv.read(1024))
    fv.seek(0)
    reader = csv.DictReader(fv, delimiter=',')
    elements = list(reader)
    return elements

def anumber(elements_list,user_element):
    for row in elements_list:
        if user_element.lower() == row['Element Name'].lower():
            atomnumber= int(row['ï»¿Atomic Number'])
    return atomnumber

def e_config(user_anumber):
    orbital = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s", "4f", "5d", "6p", "7s", "5f",
               "6d", "7p", "8s"]
    electro_c = ""
    x = 0
    while user_anumber > 0:
        orbit = orbital[x]
        if orbit[-1] == "s":
            n = 2
        elif orbit[-1] == "p":
            n = 6
        elif orbit[-1] == "d":
            n = 10
        else:
            n = 14
        if orbit == "4s" and user_element == "Copper":
            orbit = "3d"
            n = 10
        elif orbit == "3d" and user_element == "Copper":
            orbit = "4s"
            n = 1
        if orbit == "4s" and user_element == "Chromium":
            orbit = "3d"
            n = 5
        elif orbit == "3d" and user_element == "Chromium":
            orbit = "4s"
            n = 1
        if user_anumber > n:
            electro_c = electro_c + " " + orbit + str(n)
        else:
            electro_c = electro_c + " " + orbit + str(user_anumber)
        user_anumber = user_anumber - n
        x += 1
    return electro_c

def formal charges(elec_config):

# print(e_config(user_reader= elements, user_element="Uranium"))
# print(e_config(user_reader= elements, user_element="Iron"))



