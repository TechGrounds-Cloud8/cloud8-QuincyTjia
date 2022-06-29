#I had to import the csv package. I also made a dictionary where you have user input and saves it in the dictionary.
import csv

info = {
    "First name": input("First name? "),
    "Last name": input("Last name? "),
    "Job title": input("Job title? "),
    "Company": input("Company? ")
}

for key, value in info.items():
     print(key, ':', value)  

keys = info.keys()

#I opened a csv file named test, you have to use a (append) instead of w (write).
#Otherwise it will rewrite every time you place someting in the dicionary.
with open('test.csv', 'a') as csv_file:

    writer = csv.DictWriter(csv_file, fieldnames = keys)
    #This writes the collumns.
    writer.writeheader()
    #This writes the values.
    writer.writerow(info)

