#Lola Weis
#CS-175
#expensePieChart



import matplotlib.pyplot as matplot

def expensePieChart():
    file_name = 'expenses.txt'
    expenses = {}

    try:
        with open(file_name, 'r') as file:
            for line in file:
                data = line.strip().split('\t')
                if len(data) == 2:
                    category, amount = data
                    try:
                        expenses[category] = int(amount)
                    except ValueError:
                        print(f"Invalid value in {category}. Please check data and try again.")
                else:
                    print(f"Invalid format in line {line}, Please check data and try again.")

        name = list(expenses.keys())
        percent = list(expenses.values())

        matplot.figure(figsize=(12, 12))
        matplot.pie(percent, labels=name, startangle=0)
        matplot.axis('equal')
        matplot.title('Expenses Distribution')
        matplot.show()

    except IOError:
        print(f"Error: Could not open the file {file_name}.")

def main():
    expensePieChart()

if __name__ == "__main__":
    main()
