# Pandas Basics Notes

## 1. DataFrame

### Definition

A DataFrame is a 2-dimensional table in Pandas consisting of rows and columns.

### Syntax

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["Darshan", "Rahul", "Priya"],
    "Age": [25, 28, 24]
})
```

### Use Case

Store and analyze tabular data.

---

## 2. shape

### Syntax

```python
df.shape
```

### Output

```python
(rows, columns)
```

Example:

```python
(3, 2)
```

### Use Case

Find the size of the dataset.

---

## 3. columns

### Syntax

```python
df.columns
```

### Output

```python
Index(['Name', 'Age'])
```

### Use Case

View all column names.

---

## 4. head()

### Syntax

```python
df.head(5)
```

### Output

Returns the first 5 rows.

### Use Case

Quickly inspect loaded data.

---

## 5. tail()

### Syntax

```python
df.tail(5)
```

### Output

Returns the last 5 rows.

### Use Case

Inspect the ending records.

---

## 6. Selecting Columns

### Single Column

```python
df["Salary"]
```

### Returns

```python
Series
```

### Multiple Columns

```python
df[["Employee", "Salary"]]
```

### Returns

```python
DataFrame
```

### Use Case

Retrieve required columns for analysis.

---

## 7. iloc()

### Syntax

```python
df.iloc[0]
```

### Output

Returns the entire first row.

Example:

```python
Employee    John
Salary      50000
Department  IT
```

### Use Case

Select rows using index positions.

---

## 8. Filtering

### Syntax

```python
df[df["Salary"] > 60000]
```

### Internal Logic

Step 1:

```python
df["Salary"] > 60000
```

Returns:

```python
False
False
True
False
```

Step 2:

Pandas keeps only rows where the value is `True`.

### Use Case

Filter records based on business conditions.

---

## 9. Multiple Conditions

### AND

```python
df[
    (df["Department"] == "HR") &
    (df["Salary"] >= 60000)
]
```

### OR

```python
df[
    (df["Department"] == "HR") |
    (df["Department"] == "IT")
]
```

### Important

Always use brackets.

```python
(condition1) & (condition2)
```

### Use Case

Filter data using multiple business rules.

---

## 10. Sorting

### Ascending Order

```python
df.sort_values("Salary")
```

Smallest → Largest

### Descending Order

```python
df.sort_values("Salary", ascending=False)
```

Largest → Smallest

### Use Cases

* Top vendors by spend
* Top customers by revenue
* Highest-paid employees

---

## 11. isnull()

### Syntax

```python
df.isnull()
```

### Output

```python
True
False
```

### Meaning

* `True` → Missing value exists
* `False` → Value exists

### Use Case

Identify missing values.

---

## 12. isnull().sum()

### Syntax

```python
df.isnull().sum()
```

### Output

```python
Employee      0
Salary        2
Department    0
```

### Meaning

Counts missing values in each column.

### Use Case

Data quality validation.

---

## 13. fillna()

### Syntax

```python
df["Salary"] = df["Salary"].fillna(0)
```

### Meaning

Replace missing values.

### Examples

```python
df["Salary"].fillna(0)

df["Salary"].fillna(df["Salary"].mean())

df["Salary"].fillna(df["Salary"].median())
```

### Important

This DOES NOT save changes:

```python
df["Salary"].fillna(0)
```

This DOES save changes:

```python
df["Salary"] = df["Salary"].fillna(0)
```

### Use Case

Handle missing values while preserving records.

---

## 14. dropna()

### Syntax

```python
df.dropna()
```

### Meaning

Removes rows containing null values.

### Use Case

Remove incomplete records.

### Analyst Thinking

Before using:

```python
dropna()
```

Always investigate why the data is missing.

---

## 15. duplicated()

### Syntax

```python
df.duplicated()
```

### Output

```python
False
False
True
False
```

### Meaning

Checks whether a row has appeared before.

### Use Case

Identify duplicate records.

---

## 16. duplicated(subset=[])

### Syntax

```python
df.duplicated(subset=["Employee"])
```

### Meaning

Checks duplicates only within the specified column(s).

### Use Case

Find duplicate employees, customers, vendors, etc.

---

## 17. drop_duplicates()

### Syntax

```python
df.drop_duplicates()
```

### Meaning

Removes duplicate rows.

### Save Changes

```python
df = df.drop_duplicates()
```

### Use Case

Data cleaning and deduplication.

---

# Business Analyst Workflow

```text
1. Load Data
2. head()
3. shape
4. columns
5. isnull().sum()
6. duplicated()
7. Filtering
8. Sorting
9. Cleaning
10. Analysis
```

# Topics Completed

* DataFrame
* shape
* columns
* head()
* tail()
* Column Selection
* iloc()
* Filtering
* Multiple Conditions
* Sorting
* isnull()
* isnull().sum()
* fillna()
* dropna()
* duplicated()
* duplicated(subset=[])
* drop_duplicates()


# Pandas Basics - Part 2

---

# 18. dtypes

## Definition

Returns the datatype of every column in a DataFrame.

## Syntax

```python
df.dtypes
```

## Example

```python
import pandas as pd

df = pd.DataFrame({
    "Employee":["John","Mike","Sarah"],
    "Age":[25,28,24],
    "Salary":[50000.5,60000.5,70000.5]
})

df.dtypes
```

Output

```text
Employee    object
Age         int64
Salary      float64
dtype: object
```

## Common Data Types

| Datatype | Meaning | Example |
|-----------|---------|---------|
| object | String/Text | John |
| int64 | Integer | 25 |
| float64 | Decimal | 25.5 |
| bool | Boolean | True |
| datetime64 | Date & Time | 2026-06-25 |

## Use Cases

- Verify imported data
- Detect incorrect datatypes
- Debug calculation errors

---

# 19. Creating New Columns

## Definition

Create a new column using existing columns and calculations.

## Syntax

```python
df["New_Column"] = calculation
```

## Example 1

```python
df["Bonus"] = df["Salary"] * 0.10
```

## Example 2

```python
df["Profit"] = df["Revenue"] - df["Cost"]
```

## Example 3

```python
df["Net_Salary"] = df["Salary"] * 0.90
```

## Use Cases

- Bonus Calculation
- Profit Calculation
- Discounts
- KPI Creation
- Business Metrics

---

# 20. np.where()

## Definition

Returns one value if a condition is True and another value if False.

Think of it as:

```
IF
ELSE
```

## Syntax

```python
import numpy as np

np.where(
    condition,
    value_if_true,
    value_if_false
)
```

## Example

```python
df["Eligibility"] = np.where(
    df["Salary"] >= 60000,
    "Eligible",
    "Not Eligible"
)
```

Output

| Salary | Eligibility |
|---------|-------------|
| 50000 | Not Eligible |
| 60000 | Eligible |
| 70000 | Eligible |

## Use Cases

- Eligible / Not Eligible
- High / Low Salary
- Fraud / Non Fraud
- Premium / Free Customer

---

# 21. apply()

## Definition

Applies a function to every value in a column.

Think:

```
For Every Row
Apply Function
```

## Syntax

```python
df["Column"].apply(function)
```

## Example 1

```python
df["Employee"] = df["Employee"].apply(str.upper)
```

Output

```
JOHN
MIKE
SARAH
```

## Example 2

```python
def add_bonus(x):
    return x + 5000

df["Salary"] = df["Salary"].apply(add_bonus)
```

## Example 3

```python
def experience(x):

    if x >= 60000:
        return "Senior"

    else:
        return "Junior"

df["Experience"] = df["Salary"].apply(experience)
```

## Use Cases

- Uppercase Text
- Lowercase Text
- Custom Business Logic
- Salary Calculations
- Data Formatting

---

# 22. value_counts()

## Definition

Counts the frequency of each unique value.

## Syntax

```python
df["Department"].value_counts()
```

## Example

Department

```
IT
HR
IT
Finance
HR
IT
```

Output

```
IT         3
HR         2
Finance    1
```

## Use Cases

- Customers by Country
- Orders by Category
- Employees by Department
- Transactions by Status

---

# 23. unique()

## Definition

Returns all unique values from a column.

## Syntax

```python
df["Department"].unique()
```

## Output

```python
array(['IT','HR','Finance'])
```

## Use Cases

- Distinct Cities
- Distinct Departments
- Distinct Products

---

# 24. nunique()

## Definition

Returns the count of unique values.

## Syntax

```python
df["Department"].nunique()
```

## Output

```python
3
```

Because

```
IT
HR
Finance
```

are the only unique values.

## Use Cases

- Count Departments
- Count Countries
- Count Product Categories

---

# 25. describe()

## Definition

Provides descriptive statistics for numerical columns.

## Syntax

```python
df.describe()
```

## Example

```python
df = pd.DataFrame({
    "Salary":[50000,60000,70000]
})

df.describe()
```

Output

```text
count
mean
std
min
25%
50%
75%
max
```

## Meaning

| Metric | Meaning |
|----------|----------|
| count | Number of non-null values |
| mean | Average |
| std | Standard Deviation |
| min | Smallest value |
| 25% | First Quartile |
| 50% | Median |
| 75% | Third Quartile |
| max | Largest value |

---

# 26. groupby()

## Definition

Groups data based on one or more columns before performing calculations.

Think:

```
Group
Then
Calculate
```

## Syntax

```python
df.groupby("Department")["Salary"].sum()
```

## Example

| Employee | Department | Salary |
|-----------|------------|---------|
| John | IT | 50000 |
| Mike | HR | 60000 |
| Sarah | IT | 70000 |
| Tom | Finance | 55000 |

Output

```
Department

Finance    55000
HR         60000
IT        120000
```

---

# 27. GroupBy Aggregations

## Sum

```python
df.groupby("Department")["Salary"].sum()
```

Returns total salary.

---

## Mean

```python
df.groupby("Department")["Salary"].mean()
```

Returns average salary.

---

## Count

```python
df.groupby("Department")["Employee"].count()
```

Returns number of employees.

---

## Max

```python
df.groupby("Department")["Salary"].max()
```

Returns highest salary.

---

## Min

```python
df.groupby("Department")["Salary"].min()
```

Returns lowest salary.

---

# 28. agg()

## Definition

Performs multiple aggregations in one statement.

## Syntax

```python
df.groupby("Department")["Salary"].agg(
    ["sum","mean","max","min","count"]
)
```

Output

| Department | sum | mean | max | min | count |
|------------|-----|------|-----|-----|-------|

---

## Custom Column Names

```python
df.groupby("Department").agg(
    Mean_Salary=("Salary","mean"),
    Max_Salary=("Salary","max"),
    Employee_Count=("Employee","count")
)
```

Output

| Department | Mean_Salary | Max_Salary | Employee_Count |
|------------|-------------|------------|----------------|

---

# 29. Multiple GroupBy

## Syntax

```python
df.groupby(
    ["Department","Gender"]
)["Salary"].mean()
```

Output

| Department | Gender | Mean Salary |
|------------|--------|-------------|
| Finance | M | 55000 |
| HR | M | 62500 |
| IT | F | 75000 |
| IT | M | 50000 |

---

# 30. reset_index()

## Definition

Converts grouped indexes back into normal columns.

## Syntax

```python
df.groupby(
    ["Department","Gender"]
)["Salary"].mean().reset_index()
```

Before

```
Department
Gender
```

After

| Department | Gender | Salary |
|------------|--------|---------|

## Why Use It?

- Better for Dashboards
- Better for Excel Export
- Better for Merge Operations
- Easier to Read

---

# Business Analyst Workflow

```text
1. Load Data
2. head()
3. shape
4. columns
5. dtypes
6. isnull().sum()
7. duplicated()
8. Filtering
9. GroupBy
10. Aggregation
11. reset_index()
12. Dashboard / Reporting
```

---

# Topics Completed ✅

- DataFrame
- shape
- columns
- head()
- tail()
- Column Selection
- iloc()
- Filtering
- Multiple Conditions
- sort_values()
- isnull()
- isnull().sum()
- fillna()
- dropna()
- duplicated()
- drop_duplicates()
- dtypes()
- Creating Columns
- np.where()
- apply()
- value_counts()
- unique()
- nunique()
- describe()
- groupby()
- sum()
- mean()
- count()
- max()
- min()
- agg()
- Multiple GroupBy
- reset_index()

