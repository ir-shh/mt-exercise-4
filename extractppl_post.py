#By: Cui Ding & Irma Krob

import re
import csv

filepath = "err"
#this code works for the log results of the Postnorm model, in order for it to work on
#the other 2 models we have to change  the filepath and the header in row 9
#it is important to be in the right directory when running this code
with open(filepath, 'r', encoding='utf-8') as file, open('ppl_post.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Postnorm']) #to write the header

    for line in file:
        match = re.search(r'ppl:\s*(\d+\.\d+)', line)
        if match:
            writer.writerow([match.group(1)])