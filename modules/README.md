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
