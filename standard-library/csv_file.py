import csv

# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Transaction_id", "Product_id", "Price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1001, 2, 15])


with open("data.csv",) as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
