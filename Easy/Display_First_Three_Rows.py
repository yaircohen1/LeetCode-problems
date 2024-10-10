# Display the first 3 rows of a DataFrame

"""""
DataFrame: employees
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| employee_id | int    |
| name        | object |
| department  | object |
| salary      | int    |
+-------------+--------+
Write a solution to display the first 3 rows of this DataFrame.

Example 1:

Input:
DataFrame employees
+-------------+-----------+-----------------------+--------+
| employee_id | name      | department            | salary |
+-------------+-----------+-----------------------+--------+
| 3           | Bob       | Operations            | 48675  |
| 90          | Alice     | Sales                 | 11096  |
| 9           | Tatiana   | Engineering           | 33805  |
| 60          | Annabelle | InformationTechnology | 37678  |
| 49          | Jonathan  | HumanResources        | 23793  |
| 43          | Khaled    | Administration        | 40454  |
+-------------+-----------+-----------------------+--------+
Output:
+-------------+---------+-------------+--------+
| employee_id | name    | department  | salary |
+-------------+---------+-------------+--------+
| 3           | Bob     | Operations  | 48675  |
| 90          | Alice   | Sales       | 11096  |
| 9           | Tatiana | Engineering | 33805  |
+-------------+---------+-------------+--------+
Explanation:
Only the first 3 rows are displayed.

"""
# Solution: without using head() function and pandas

employees = {
    'employee_id': [3, 90, 9, 60, 49, 43],
    'name': ['Bob', 'Alice', 'Tatiana', 'Annabelle', 'Jonathan', 'Khaled'],
    'department': ['Operations', 'Sales', 'Engineering', 'InformationTechnology', 'HumanResources', 'Administration'],
    'salary': [48675, 11096, 33805, 37678, 23793, 40454]
}


# Function to display the first n rows of a DataFrame
def display_first_n_rows(data, n):
    keys = list(data.keys())  # list of column names
    # print the column names
    print(f"| {keys[0]:<11} | {keys[1]:<10} | {keys[2]:<20} | {keys[3]:<6} |")
    print("-" * 60)

    # check if n is greater than the number of rows
    if n > len(data['employee_id']):
        n = len(data['employee_id'])

    # print the first n rows
    for i in range(n):
        print(f"| {data['employee_id'][i]:<11} | {data['name'][i]:<10} | {data['department'][i]:<20} | {data['salary'][i]:<6} |")

    # print the bottom line separator and an empty line
    print("-" * 60)
    print()



# Function to display columns of a DataFrame
def display_column(data, name_of_colum):
    if name_of_colum in data.keys():
        print(f"| {name_of_colum:<11} |")
        print("-" * 15)
        for i in range(len(data[name_of_colum])):
            print(f"| {data[name_of_colum][i]:<11} |")
        print("-" * 15)
        print()
    else:
        print(f"Column {name_of_colum} does not exist in the DataFrame.")




# Test the function
display_first_n_rows(employees, 4)
display_first_n_rows(employees, 7)
display_column(employees, 'name')
display_column(employees, 'salary')
display_column(employees, 'age')
