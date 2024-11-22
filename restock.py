def restock_inventory(available_items, inventory_records, current_day):

    import random 
    restocked_units = 0
    if current_day == 0:
        inventory_records.append([0, 0, 2000, 2000])
    if current_day % 7 == 0:
        if current_day !=0:
           restocked_units = 2000 - available_items
           available_items = 2000
           inventory_records.append([current_day, 0, restocked_units, available_items])
    return available_items
