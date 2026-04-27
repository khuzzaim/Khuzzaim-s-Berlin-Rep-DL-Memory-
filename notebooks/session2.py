# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python [conda env:conda_envs-computelab-2025-2]
#     language: python
#     name: conda-env-conda_envs-computelab-2025-2-py
# ---

# %% [markdown]
# # Session 2
# Basic Python in Jupyter Notebook

# %%
print("Hello World")

# %%
a = 5
b = 3.2
c = True
d = None

print(a, b, c, d)

# %%
x = 10
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x**y)

# %%
planet = "Mars"
gravity = 3.73

print(planet)
print(gravity)

# %%
a = 10
b = 3.14
c = "hello"

print(type(a))
print(type(b))
print(type(c))

# %%
name = "Khuzzaim"

print(name)
print(name.upper())
print(name.lower())

# %%
age = 25

# %%
name = "Khuzzaim"

# %%
print(name)

# %%
print("Hello")

# %%
print(f"{name} is {age} years old")

# %%
a = 5
b = 3

print(a + b)

# %%
alist = [10, 20, 30]

# %%
alist[1]

# %%
alist.append(10)

# %%
alist.append("hello")
alist.append(True)

# %%
alist

# %%
alist[2] = "world"

# %%
alist

# %%
t = (1, 2, 3)

# %%
t

# %%
person = {"name": "Khuzzaim", "age": 25}

# %%
person["name"]

# %%
planet_gravity = {"Earth": 9.81, "Moon": 1.62, "Mars": 3.71}

# %%
planet_gravity["Mars"]

# %%
for x in [1, 2, 3]:
    print(x)

# %%
