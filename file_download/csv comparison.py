import csv
with open('English.csv', 'rb') as csvfile1:
    with open ("Dictionary.csv", "rb") as csvfile2:
        reader1 = csv.reader(csvfile1)
        reader2 = csv.reader(csvfile2)
        rows1 = [row for row in reader1]
        rows2 = [row for row in reader2]
        col_a = [row1[0] for row1 in rows1]
        col_b = [row2[0] for row2 in rows2]
        col_c = [row2[1] for row2 in rows2]
        only_b = [text for text in col_b if not text in col_a]