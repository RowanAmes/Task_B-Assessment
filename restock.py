def restock_inventory(available_items, inventory_records, current_day):

    import random 

    if current_day % 7 == 0:
        restocked_units = 2000 - available_items
        available_items += restocked_units 
    else:
        restocked_units = 0

    sold_units = random.randint(0,200)

    available_items -= sold_units
    available_items = max(available_items, 0)
    inventory_records.append([current_day, sold_units, restocked_units, available_items])

    
    return available_items

days = 49
available_items = 2000
inventory_records =[[0, 0, 2000, 2000]]

for current_day in range (1, days + 1):
   available_items = restock_inventory(available_items, inventory_records, current_day)
print("day\tsold units\trestocked units\tavailable units")
for record in inventory_records:
    print(f"{record[0]}\t{record[1]}\t\t{record[2]}\t\t{record[3]}")




# if current_day == (0):
     #   inventory_records.append([current_day, 0, 2000, 2000])
    #    available_items = 2000
     #   return available_items