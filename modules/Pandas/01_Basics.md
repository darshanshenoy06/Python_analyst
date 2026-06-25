# 📘 Pandas Basics

> A beginner-friendly guide to the fundamental concepts of Pandas for Business Analysts, Data Analysts, and Python learners.

---

# 📚 Topics Covered

* DataFrame
* shape
* columns
* head()
* tail()
* Selecting Columns
* iloc()
* loc()
* Filtering
* Multiple Conditions
* sort_values()

---

# 1. DataFrame

## 📖 Definition

A **DataFrame** is a two-dimensional tabular data structure in Pandas that stores data in **rows and columns**. It is similar to an **Excel spreadsheet** or a **SQL table**.

---

## 🧠 Why do we use it?

Almost every data analysis task begins by loading data into a DataFrame.

It allows us to:

* Store structured data
* Analyze datasets
* Filter information
* Perform calculations
* Generate reports

---

## 📝 Syntax

```python
import pandas as pd

df = pd.DataFrame({
    "Employee": ["John", "Mike", "Sarah"],
    "Salary": [50000, 60000, 70000]
})
```

---

## 📤 Output

| Employee | Salary |
| -------- | ------ |
| John     | 50000  |
| Mike     | 60000  |
| Sarah    | 70000  |

---

## 💼 Business Use Cases

* Employee Records
* Sales Data
* Customer Database
* Product Inventory
* Financial Reports

---

## 💡 Interview Tip

Almost every Pandas interview starts with a DataFrame.

Understand DataFrames before learning any other Pandas function.

---

## ⚡ Memory Trick

```text
Excel Spreadsheet
        =
Pandas DataFrame
```

---

## 🎯 Quick Revision

✔ Two-dimensional data structure

✔ Rows and Columns

✔ Similar to Excel

✔ Most important Pandas object

---

# 2. shape

## 📖 Definition

Returns the number of **rows and columns** in a DataFrame.

---

## 📝 Syntax

```python
df.shape
```

---

## 📤 Output

```python
(rows, columns)
```

Example

```python
(1000, 5)
```

Meaning

* 1000 Rows
* 5 Columns

---

## 💼 Business Use Cases

* Check dataset size
* Validate imported data
* Compare datasets

---

## 💡 Interview Tip

Remember:

```text
(rows, columns)
```

NOT

```text
(columns, rows)
```

---

## ⚡ Memory Trick

```text
Shape

↓

Dataset Size
```

---

## 🎯 Quick Revision

✔ Returns dataset dimensions

✔ First value → Rows

✔ Second value → Columns

---

# 3. columns

## 📖 Definition

Returns the names of all columns in a DataFrame.

---

## 📝 Syntax

```python
df.columns
```

---

## 📤 Output

```python
Index(['Employee', 'Salary'])
```

---

## 💼 Business Use Cases

* Verify column names
* Detect spelling mistakes
* Explore unknown datasets

---

## 💡 Interview Tip

One of the first commands analysts run after loading a dataset.

---

## ⚡ Memory Trick

```text
columns

↓

Column Names
```

---

## 🎯 Quick Revision

✔ Returns all column names

✔ Useful for dataset exploration

---

# 4. head()

## 📖 Definition

Returns the first **5 rows** of a DataFrame by default.

---

## 📝 Syntax

```python
df.head()
```

or

```python
df.head(10)
```

---

## 📤 Output

Shows the first rows of the dataset.

---

## 💼 Business Use Cases

* Inspect imported data
* Verify columns
* Detect formatting issues

---

## 💡 Interview Tip

Always use `head()` immediately after loading data.

---

## ⚡ Memory Trick

```text
Head

↓

Beginning
```

---

## 🎯 Quick Revision

✔ First 5 rows

✔ Data inspection

---

# 5. tail()

## 📖 Definition

Returns the last **5 rows** of a DataFrame.

---

## 📝 Syntax

```python
df.tail()
```

---

## 📤 Output

Shows the last rows of the dataset.

---

## 💼 Business Use Cases

* Verify latest records
* Check imported data
* Inspect file endings

---

## 💡 Interview Tip

Useful when working with time-series datasets.

---

## ⚡ Memory Trick

```text
Tail

↓

End
```

---

## 🎯 Quick Revision

✔ Last 5 rows

✔ End of dataset

---

# 6. Selecting Columns

## 📖 Definition

Used to retrieve one or more columns from a DataFrame.

---

## 📝 Single Column

```python
df["Salary"]
```

Returns

```text
Series
```

---

## 📝 Multiple Columns

```python
df[["Employee", "Salary"]]
```

Returns

```text
DataFrame
```

---

## 💼 Business Use Cases

* View required columns
* Prepare reports
* Perform calculations

---

## 💡 Interview Tip

Single brackets return a **Series**.

Double brackets return a **DataFrame**.

---

## ⚡ Memory Trick

```text
[]

↓

Series

[[]]

↓

DataFrame
```

---

## 🎯 Quick Revision

✔ Single column → Series

✔ Multiple columns → DataFrame

---

# 7. iloc()

## 📖 Definition

Select rows and columns using **integer positions**.

---

## 📝 Syntax

```python
df.iloc[row, column]
```

Example

```python
df.iloc[0]
```

Returns the first row.

---

## 📤 Example Output

| Employee | Salary |
| -------- | ------ |
| John     | 50000  |

---

## 💼 Business Use Cases

* Retrieve specific rows
* Access records by position
* Data slicing

---

## 💡 Interview Tip

`iloc` is **position-based**.

---

## ⚡ Memory Trick

```text
iloc

↓

Integer Location
```

---

## 🎯 Quick Revision

✔ Position based

✔ Uses integers

---

# 8. loc()

## 📖 Definition

Access or modify rows and columns using **labels**.

---

## 📝 Syntax

```python
df.loc[row_label, column_name]
```

Example

```python
df.loc[0, "Salary"]
```

---

## Updating Values

```python
df.loc[0, "Salary"] = 55000
```

---

## 💼 Business Use Cases

* Update records
* Retrieve values
* Edit datasets

---

## 💡 Interview Tip

`loc` uses **labels**, while `iloc` uses **positions**.

---

## ⚡ Memory Trick

```text
loc

↓

Location by Label
```

---

## 🎯 Quick Revision

✔ Label based

✔ Can retrieve or update values

---

# 9. Filtering

## 📖 Definition

Returns only rows that satisfy a given condition.

---

## 📝 Syntax

```python
df[df["Salary"] > 60000]
```

---

## Internal Logic

Step 1

```python
df["Salary"] > 60000
```

Returns

```text
False
False
True
```

Step 2

Pandas keeps only rows where the condition is **True**.

---

## 💼 Business Use Cases

* High-value customers
* Expensive products
* Employees above salary threshold

---

## 💡 Interview Tip

Filtering always begins with a Boolean condition.

---

## ⚡ Memory Trick

```text
Condition

↓

True

↓

Keep Row
```

---

## 🎯 Quick Revision

✔ Boolean Filtering

✔ Returns matching rows

---

# 10. Multiple Conditions

## 📖 Definition

Apply more than one condition while filtering data.

---

## AND

```python
df[
    (df["Department"] == "HR") &
    (df["Salary"] >= 60000)
]
```

---

## OR

```python
df[
    (df["Department"] == "HR") |
    (df["Department"] == "IT")
]
```

---

## Important

Always wrap each condition inside parentheses.

Correct

```python
(condition1) & (condition2)
```

---

## 💼 Business Use Cases

* HR employees earning above a threshold
* Multiple product categories
* Multi-rule filtering

---

## 💡 Interview Tip

Never forget the parentheses.

---

## ⚡ Memory Trick

```text
AND

&

OR

|
```

---

## 🎯 Quick Revision

✔ Multiple conditions

✔ Use &, |

✔ Always use parentheses

---

# 11. sort_values()

## 📖 Definition

Sorts a DataFrame based on one or more columns.

---

## Ascending Order

```python
df.sort_values("Salary")
```

---

## Descending Order

```python
df.sort_values(
    "Salary",
    ascending=False
)
```

---

## 💼 Business Use Cases

* Highest-paid employees
* Top-selling products
* Highest revenue customers

---

## 💡 Interview Tip

Ascending is the default.

Descending requires

```python
ascending=False
```

---

## ⚡ Memory Trick

```text
Ascending

Small → Large

Descending

Large → Small
```

---

## 🎯 Quick Revision

✔ Sort data

✔ Ascending (default)

✔ Descending → ascending=False

---

# 📌 Chapter Summary

After completing this chapter, you should be able to:

* ✅ Create a DataFrame
* ✅ Understand dataset dimensions
* ✅ View column names
* ✅ Inspect datasets
* ✅ Select rows and columns
* ✅ Filter records
* ✅ Apply multiple conditions
* ✅ Sort data
* ✅ Retrieve data using `iloc` and `loc`

---

# 🚀 What's Next?

Continue to **02_Data_Cleaning.md**, where you'll learn:

* Missing Values
* Null Handling
* Duplicates
* Data Types
* Data Cleaning Techniques
