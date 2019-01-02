import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 4]

x2 = [1, 2, 3]
y2 = [10, 14, 12]


# part one
"""
plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Secound Line')
plt.xlabel('Plot number')
plt.ylabel('Important var')
plt.title('Interesting Graph\nCheck it out')
# adds a legend with the different labels
plt.legend()
"""

# part 2
"""
x = [2, 4, 6, 8, 10]
y = [6, 7, 8, 2, 4]

x2 = [1, 3, 5, 7, 9]
y2 = [7, 8, 2, 4, 2]

plt.bar(x, y, label='Bars1', color='blue')
plt.bar(x2, y2, label='Bars2', color='r')
"""

population_ages = [22, 44, 55, 2, 3, 50, 5, 7, 89, 12,
                   14, 15, 64, 78, 80, 20, 16, 18, 79, 49, 46, 13, 23]
"""
ids = [x for x in range(len(population_ages))]
plt.bar(ids, population_ages)
"""
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
# plt.legend()
plt.show()
