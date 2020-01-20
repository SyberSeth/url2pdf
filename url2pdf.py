import csv
import subprocess

with open('urls.csv', newline='') as f:
    reader = csv.reader(f)
    url_list = list(reader)
    

with open('names.csv', newline='') as f:
    reader = csv.reader(f)
    name_list = list(reader)
 

for url, name in zip(url_list, name_list):
    arg = [r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe']
    args = arg + url + name
    subprocess.call(args)
   
