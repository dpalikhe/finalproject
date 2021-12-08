import csv
def load_elements():
    fv = open("Elements_list.csv", "r")
    dialect = csv.Sniffer().sniff(fv.read(1024))
    fv.seek(0)
    reader = csv.DictReader(fv, delimiter=',')
    elements = list(reader)
    return elements

def anumber(elements_list,user_ele):
    atomnumber=-1
    for row in elements_list:
        if user_ele.lower() == row['Element Name'].lower():
            atomnumber = int(row['Atomic Number'])
    if atomnumber == -1:
        print("Wrong Element Name")
    return atomnumber



