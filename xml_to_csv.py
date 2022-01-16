import xml.etree.ElementTree as Et
import csv
import re

input_file_name = "test.xml"  # Input .XML file address
table_name = "test.csv"  # Output .CSV file address

tree = Et.parse(input_file_name)
root = tree.getroot()

header_from_xml = []
sorted_header_from_xml = []
for child in root:
    for i in child.findall(".//"):
        if re.findall("\A\n", i.text):
            pass
        else:
            header_from_xml.append(i.tag)
for x in header_from_xml:
    if x not in sorted_header_from_xml:
        sorted_header_from_xml.append(x)

with open(table_name, 'w', newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(sorted_header_from_xml)

len_list = len(sorted_header_from_xml)
for child in root:
    body_list = []
    for x in range(len_list):
        tmp = child.find(".//" + sorted_header_from_xml[x])
        if tmp is not None:
            tmp = tmp.text
        else:
            tmp = None
        body_list.append(tmp)

    with open(table_name, 'a+', newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(body_list)
