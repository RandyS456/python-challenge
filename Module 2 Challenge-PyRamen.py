# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('../Resources/menu_data.csv')
sales_filepath = Path('../Resources/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list

with open(menu_filepath) as file:
    menu_csv_reader = csv.reader(file, delimiter=',')
    #Skip header row
    next(menu_csv_reader)

# @TODO: Read in the sales data into the sales list

with open(sales_filepath) as file:
    sales_csv_reader = csv.reader(file, delimiter=',')
    #Skip header row
    next(sales_csv_reader)

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for row in sales_csv_reader:


    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    sales_line_item_ID = row[0]
    sales_date = row[1]
    sales_credit_card_number = row[2]
    sales_quantity = row[3]
    sales_menu_item = row[4]
    

    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    report[sales_menu_item] = {"01-count":0,"02-revenue":0,"03-cogs":0,"04-profit":0}


    # @TODO: For every row in our sales data, loop over the menu records to determine a match


        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        menu_item = record[0]
        menu_category = record[1]
        menu_description = record[2]
        menu_price = float(record[3])
        menu_cost = float(record[4])
        

        # @TODO: Calculate profit of each item in the menu data
        
        item_profit = menu_price - menu_cost

        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        
        if sales_menu_item == menu_item

            # @TODO: Print out matching menu data

            print(menu_item)


            # @TODO: Cumulatively add up the metrics for each item key
            report[sales_menu_item]["01-count"] += int(sales_quantity)
            report[sales_menu_item]["02-revenue"] += menu_price*int(sales_quantity)
            report[sales_menu_item]["03-cogs"] += menu_cost*int(sales_quantity)
            report[sales_menu_item]["04-profit"] += item_profit*int(sales_quantity)

        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match
            else:
                print(f"{sales_menu_item} does not equal {menu_item}! NO MATCH!")


    # @TODO: Increment the row counter by 1
            row_count += 1

# @TODO: Print total number of records in sales data

            print(row_count)


# @TODO: Write out report to a text file (won't appear on the command line output)
            with open("report.txt","w"") as file:
                      for key,