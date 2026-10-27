# 📝 Method Overriding in Python (GeeksforGeeks)

🔗 [Problem Link](https://www.geeksforgeeks.org/problems/method-overriding-in-python/1)

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange) ![Language](https://img.shields.io/badge/Language-Python-blue)

### 💡 Tags
python

### 🚀 Performance
- **Runtime:** Successfully Evaluated
- **Memory:** N/A

---

### 📜 Problem Description

Implement the following classes to understand method overriding in Python:

**Class Name:**   `Employee`

- **Attributes** :

- `id`  (integer)

- `salary`  (integer)

- **Constructor** :

- `__init__(self, id, salary)` : Initializes the  `id`  and  `salary`  attributes with the given values.

- **Methods/Functions** :

1. `get_info(self)` :

- **Parameters** : None

- **Task** : Returns a string formatted as:  `"EmployeeID:{id} Salary:{salary}"` .

**Class Name:**   `SalesEmployee`  (Subclass of  `Employee` )

- **Attributes** :

- Inherited from  `Employee` :  `id` ,  `salary`

- New attribute:  `sales`  (integer, optional, defaults to 0)

- **Constructor** :

- `__init__(self, id, salary, sales=0)` : Calls  `super().__init__(id, salary)`  to initialize the inherited attributes, and initializes the  `sales`  attribute. The  `sales`  parameter defaults to  `0`  if not provided.

- **Methods/Functions** :

1. `get_info(self)` :

- **Parameters** : None

- **Task** :  **Overrides**  the  `get_info`  method to include the  `sales`  attribute in the output.

- **Return Format** :  `"EmployeeID:{id} Salary:{salary} Sales:{sales}"` .

**Examples:**

```
Input: id = 103, salary = 70000, sales = 300
Output: 
EmployeeID:103 Salary:70000
EmployeeID:103 Salary:70000 Sales:300
```