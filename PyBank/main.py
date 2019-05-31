#   import modules
import csv
import os 

#  create file path to open csv
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#   open file
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')


#   loop through file to get months, net total amount
    # initiate month
    month = row[0]
    # initiate net total amount
    net_total = row[1]

    # initiate greatest increase in profits amount,month as variable
    maxAmount = 0
    maxDate = ''
    # initiate greatest decrease in profits amount, month as variable
    minAmount = 0
    minDate = ''
    # if month of current row is different than month of next row,
    # add 1 to counter
    
    # if net total amount is positive and greater 
    # than greatest increase in profits, overwrite amount,month

    # if net total amount is positive and greater 
    # than greatest increase in profits, overwrite amount,month

    #   print to console
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: ')
    print(f'Total: $ {}')
    print(f'Average  Change: $'{})
    print(f'Greatest Increase in Profits: {} ({})')
    print(f'Greatest Decrease in Profits: {} ({})')


#   create file path to write csv to
output_path = os.path.join("..", "output", "budget_summary.csv")

#   open the file in 'write' mode
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow([''])

    # Write the second row
    csvwriter.writerow(['])