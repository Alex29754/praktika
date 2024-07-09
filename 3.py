import matplotlib.pyplot as plt #используется для построения графиков.
import numpy as np # используется для работы с числовыми массивами и различными математическими операциями.

def plot_function(func, x_range):
    x = np.linspace(x_range[0], x_range[1], 400) # создает массив из 400 равномерно распределенных точек между
    y = func(x)
    plt.plot(x, y)
    plt.xlabel('x') # устанавливает метку для оси x
    plt.ylabel('f(x)')
    plt.title('График функции')
    plt.grid(True) #включает отображение сетки на графике.
    plt.show()

func = lambda x: x**2
x_range = (-np.pi, np.pi)
plot_function(func, x_range)
