from matplotlib import pyplot as plt
from utlities.algorithms.linearregression import *

m = (calc_slope(num, sum_xy, sum_x, sum_y, sum_x_squared))
b = (calc_intercept(sum_y,calc_slope(num, sum_xy, sum_x, sum_y, sum_x_squared), sum_x, num))

linx_line = x_vals
liny_line = [((m * xi) + b) for xi in x_vals]

if m > 0:
    statement = "Expenses are projected to go up next month"
elif m < 0:
    statement = "Expenses are projected to go down next month"
else:
    statement = "Expenses seem steady"

plt.scatter(x_vals, y_vals, color="red", label="Transactions")
plt.plot(linx_line, liny_line, color="blue", label="Projection Line")
plt.text(x_vals[0], max(y_vals)/2, statement, fontsize=12, color="black")

plt.xlabel("Transaction #")
plt.ylabel("$ Amount")
plt.title("July Transactions with Projections")
plt.legend()
plt.grid(True)