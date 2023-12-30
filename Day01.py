import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

x_train = np.array([1.0, 2.0, 3.0, 4.0])
y_train = np.array([3.0, 4.0, 5.0, 6.0])

# m is the number of training examples

m = x_train.shape[0]
# m = len (x_train)
def dis_element(x, y, i):
    print(f"Element[{i}]: x_train:{x[i]}  y_train:{y[i]}")
def draw_scat (x, y, title, xlabel, ylabel):
    plt.scatter(x, y, marker = 'o', c = "green")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show ()


def compute_model_output(x, w, b):
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b
    return f_wb

tmp_f_wb = compute_model_output(x_train, 100, 100)
plt.plot (x_train, tmp_f_wb, c = "red", label = "Prediccion")
draw_scat(x_train, y_train, "this is a title", "x_label", "y_label")
#plt.legend()
plt.show()