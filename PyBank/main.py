#\Rutgers\Homework\Due 8-25\Resources

import os
import csv
import operator

filename = os.path.join("../../../", "Rutgers", "Homework", "Due 8-25", "Resources", "budget_data.csv")

with open(filename, "r") as bank_infile:
    csv_reader = csv.reader(bank_infile, delimiter= ",")
    next(csv_reader, None) #skip the headers

    #store all the records into a list for manipulation
    #columns
    #Date	Profit/Losses
    monthly_budgets = [budget for budget in csv_reader]

    #store relevant values
    count_of_months = len(monthly_budgets)
    net_budget = sum([float(budget[1]) for budget in monthly_budgets])

    #calculate the montly changes and derive the average change
    montly_changes = [float(monthly_budgets[i+1][1])-float(monthly_budgets[i][1]) for i in range(count_of_months-1)]
    average_change = sum(montly_changes)/(len(montly_changes))
    greatest_increase = max(montly_changes)
    greatest_decrease = min(montly_changes)

    #format results for output
    report_lines = []
    report_lines.append(f"\n\nFinancial Analysis")
    report_lines.append(f"----------------------------")
    report_lines.append(f"Total Months: {count_of_months}")
    report_lines.append(f"Total: ${net_budget}")
    report_lines.append("Average  Change: ${:.{}f}".format(average_change,2))
    report_lines.append(f"Greatest Increase in Profits: {monthly_budgets[montly_changes.index(greatest_increase) + 1][0]} (${greatest_increase})")
    report_lines.append(f"Greatest Decrease in Profits: {monthly_budgets[montly_changes.index(greatest_decrease) + 1][0]} (${greatest_decrease})\n")

    #print results to the terminal
    for line in report_lines:
        print(line)

    #print results to file
    filename = os.path.join("./", "bank_analysis.txt")
    bank_outfile = open(filename, "w") 
    for line in report_lines:
        bank_outfile.write(line + "\n")
    bank_outfile.close()


    