from utlities import objects

y_vals = objects.transaction_list

x_vals = [key+1 for key in objects.Expense.all_dict.keys()]

sum_xy = sum(x_i * y_i for x_i, y_i in zip(x_vals,y_vals))
sum_x = sum(x_i for x_i in x_vals)
sum_y = sum(y_i for y_i in y_vals)
sum_x_squared = sum((x_i**2) for x_i in x_vals)
num = len(x_vals)

def calc_slope(n, xy, x, y, x_sqr):

    top = (n * xy) - (x * y)
    bottom = (n * x_sqr) - (x**2)
    m = top / bottom

    return m

def calc_intercept(y, m, x, n):
    top = (y) - (m - x)
    bottom = n
    b = top / bottom
    return b 