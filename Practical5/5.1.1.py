import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
city_a = [30, 32, 35, 38, 40, 42, 45, 44, 41, 37, 33, 31]
city_b = [20, 22, 25, 28, 30, 32, 35, 34, 31, 27, 23, 21]
city_c = [10, 12, 15, 18, 20, 22, 25, 24, 21, 17, 13, 11]

plt.stackplot(months, city_a, city_b, city_c, labels=['City A', 'City B', 'City C'])
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.title("Temperature Variation")
plt.legend()
plt.show()
