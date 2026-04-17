
import csv

#Open your JSON file
with open('file.json','r') as json_file:
    data = json.load(json_file)
    
#Convert to CSV
with open('output.csv','w', newline='') as csv_file:
    writer = csv.DicWriter(csv_file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
    
print("Converted succeessfully!")