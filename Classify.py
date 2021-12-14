# import csv
# CONSTANT = "html/map/file/Data.html"

def classify_elements(user_num):
    non_metals = [1, 2, 6, 7, 8, 9, 10, 15, 16, 17, 18, 34, 35, 36, 53, 54, 85, 86, 117, 118]
    metalloids = [5, 14, 32, 33, 51, 52, 84]
    if user_num in non_metals:
        return "This element belongs to non-metals group."
    elif user_num in metalloids:
        return "This element belongs to metalloids group."
    else:
        return "This element belongs to metal group."

def e_config(user_anumber,user_element):
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
    return electro_c.strip()

def valence_electrons(elec_config):
    elec_config_list = elec_config.split(" ")
    energy_level = elec_config_list[-1][0]
    if len(elec_config_list)>1 and elec_config_list[-2][0] == energy_level:
        val_elec= int(elec_config_list[-2][2])+int(elec_config_list[-1][2])
    else:
        val_elec=int(elec_config_list[-1][2])
    return val_elec
