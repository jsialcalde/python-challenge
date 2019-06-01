#   import modules
import csv
import os 

#  create file path to open csv
csvpath = os.path.join( 'Resources', 'budget_data.csv')

#   open file
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # initiate greatest increase in profits amount,month as variable
    maxAmount = 0
    maxDate = ''
    # initiate greatest decrease in profits amount, month as variable
    minAmount = 0
    minDate = ''

    # initiate # of months counter
    count_months = 0
    
    # initiate total balance
    total_balance = 0

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
    #initiate net total,net change, total net change
    net_total = 0
    net_change = 0
    total_net_change = 0

#   loop through file to get months, net total amount
    for i,row in enumerate(csvreader):
        
        # initiate month
        month = row[0]
        
        # assign net change (current net total - previous net total), only calculate for second row onwards
        if(i>0):
            net_change = float(row[1]) - net_total

        # set net total amount
        net_total = float(row[1])

        # add 1 to month counter
        count_months += 1

        # add net total to total balance
        total_balance += net_total    

        # if net total amount is positive and greater 
        # than greatest increase in profits, overwrite amount,month
        if (net_change>maxAmount):
            maxAmount = net_change
            maxDate = month

        # if net total amount is positive and greater 
        # than greatest increase in profits, overwrite amount,month
        if (net_change<minAmount):
            minAmount = net_change
            minDate = month

        #add net change to total cumulative net change
        total_net_change += net_change
    
    # calculate avg change, account for net change being 0 in first row
    avg_change = (total_net_change)/(count_months-1)        
    #   print to console
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {count_months}')
    print(f'Total: $ {int(round(total_balance,0))}')
    print(f'Average  Change: ${round(avg_change,2)}')
    print(f'Greatest Increase in Profits: {maxDate} (${int(round(maxAmount,0))})')
    print(f'Greatest Decrease in Profits: {minDate} (${int(round(minAmount,0))})')


#   create file path to write txt to
output_path = os.path.join("output", "budget_summary.txt")

#   open the file in 'write' mode
with open(output_path, 'w', newline='') as csvfile:

    #Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the to the file
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow([f'Total Months: {count_months}'])
    csvwriter.writerow([f'Total: $ {int(round(total_balance,0))}'])
    csvwriter.writerow([f'Average  Change: ${round(avg_change,2)}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {maxDate} (${int(round(maxAmount,0))})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {minDate} (${int(round(minAmount,0))})'])