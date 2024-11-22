import random

def daily_sales(available_items, inventory_records, current_day):
    sales_daily = 0
    if current_day % 7 != 0:
        sales_daily = random.randint(0, 200)
        available_items = available_items - sales_daily
        inventory_records.append((current_day, sales_daily,0 , available_items))
    elif current_day % 7 == 0:
        available_items = 2000
    return available_items


