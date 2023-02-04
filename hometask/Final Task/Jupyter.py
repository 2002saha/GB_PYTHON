#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.optimize import minimize_scalar


# In[2]:


def f(x):
    return -12*x**4*np.sin(np.cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30


# In[3]:


def find_roots():
    # Определение корней
    roots = fsolve(f, np.array([-3, -2, 0, 2, 3]))
    return roots

def find_intervals(x, y):
    # Нахождение интервалов, на которых функция возрастает и убывает
    intervals = []
    for i in range(len(y) - 1):
        if y[i] < y[i+1]:
            intervals.append([x[i], x[i+1]])
        elif y[i] > y[i+1]:
            intervals.append([x[i+1], x[i]])
    return intervals


# In[4]:


x = np.linspace(-3, 3, 1000)
y = f(x)


# In[5]:


roots = find_roots()
print("Корни функции:", roots)


# In[6]:


intervals = find_intervals(x, y)
print("Интервалы, на которых функция возрастает:", intervals[:int(len(intervals)/2)])


# In[7]:


print("Интервалы, на которых функция убывает:", intervals[int(len(intervals)/2):])


# In[8]:


def find_peak():
    res = minimize_scalar(f)
    peak = res.x
    return res.x


# In[9]:


def find_intervals_pos_neg(x, y):
    # Нахождение промежутков, на которых f > 0 и f < 0
    intervals_pos = []
    intervals_neg = []
    for i in range(len(y) - 1):
        if y[i] > 0 and y[i+1] < 0:
            intervals_neg.append([x[i], x[i+1]])
        elif y[i] < 0 and y[i+1] > 0:
            intervals_pos.append([x[i], x[i+1]])
    return intervals_pos, intervals_neg


# In[10]:


x = np.linspace(-3, 3, 1000)
y = f(x)


# In[11]:


peak = find_peak()
print("Вершина функции:", peak)


# In[12]:


intervals_pos, intervals_neg = find_intervals_pos_neg(x, y)
print("Промежутки, на которых f > 0:", intervals_pos)
print("Промежутки, на которых f < 0:", intervals_neg)


# In[13]:


fig, ax = plt.subplots()

ax.plot(x, y, label='Функция f(x)', color='blue')
ax.axhline(0, color='black', lw=0.5, label='Ось X')
ax.scatter(roots, f(roots), label='Корни', color='red', marker='x')

peak = find_peak()
ax.scatter(peak, f(peak), label='Вершина', color='green', marker='o')

intervals_pos, intervals_neg = find_intervals_pos_neg(x, y)
for interval in intervals_pos:
    ax.axvline(interval[0], color='green', lw=0.5, label='Позитивный интервал' if interval == intervals_pos[0] else '')
    ax.axvline(interval[1], color='green', lw=0.5)
for interval in intervals_neg:
    ax.axvline(interval[0], color='red', lw=0.5, label='Негативный интервал' if interval == intervals_neg[0] else '')
    ax.axvline(interval[1], color='red', lw=0.5)

ax.legend(loc='best', fontsize=12)
ax.grid(True, ls='--', alpha=0.7)
ax.set_title('График функции f(x)', fontsize=16)
ax.set_xlabel('Ось X', fontsize=14)
ax.set_ylabel('Ось Y', fontsize=14)
ax.tick_params(labelsize=12)

plt.tight_layout()
plt.show()

