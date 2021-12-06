import csv
CONSTANT = "html/map/file/Data.html"
if __name__ == '__main__':
    fv = open("Elements_list.csv", "r")
    dialect = csv.Sniffer().sniff(fv.read())
    fv.seek(0)
    reader = csv.DictReader(fv, dialect=dialect)

    def classify_elements(user_element):
        non_metals = [1, 2, 6, 7, 8, 9, 10, 15, 16, 17, 18, 34, 35, 36, 53, 54, 85, 86, 117, 118]
        metalloids = [5, 14, 32, 33, 51, 52, 84]
        for row in reader:
            if user_element == row['Element Name']:
                atomic_num = row['ï»¿Atomic Number']
                if atomic_num in non_metals:
                    return "This element belongs to non-metals group."
                elif atomic_num in metalloids:
                    return "This element belongs to metalloids group."
                else:
                    return "This element belongs to metal group."
    print(classify_elements(user_element=1))


