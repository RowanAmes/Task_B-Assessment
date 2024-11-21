import random

def daily_sales(available_items, inventory_records, current_day):
    sales = random.randint(0, available_items)
    available_items -= sales

    restocked_units = 0
    if available_items < 500:
        restocked_units = 2000 - available_items
        available_items = 2000

    inventory_records.append((current_day, sales, restocked_units, available_items))

    return available_items


