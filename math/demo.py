import numpy as np
import matplotlib.pyplot as plt

def f1():
    # 生成 x 的取值范围 (-2*pi, 2*pi)，间隔为 0.01
    x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)

    # 定义 y 的函数值
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    # 绘图
    plt.figure(figsize=(8, 6))  # 设置画布大小
    plt.plot(x, y_sin, label="y = sin(x)", color="blue", linewidth=2)  # 绘制正弦函数
    plt.plot(x, y_cos, label="y = cos(x)", color="red", linestyle="--", linewidth=2)  # 绘制余弦函数

    # 图例、标题和网格
    plt.title("Sin and Cos Functions", fontsize=16)
    plt.xlabel("x-axis", fontsize=12)
    plt.ylabel("y-axis", fontsize=12)
    plt.legend(loc="upper right")  # 设置图例位置
    plt.grid(True)  # 显示网格

    # 显示图形
    plt.show()

def f2():
    # x 的范围
    x = np.linspace(-2 * np.pi, 2 * np.pi, 500)

    # 函数列表
    functions = [("sin(x)", np.sin), ("cos(x)", np.cos), ("sin(x) + cos(x)", lambda x: np.sin(x) + np.cos(x))]

    # 绘制多个函数
    plt.figure(figsize=(10, 6))
    for label, func in functions:
        plt.plot(x, func(x), label=f"y = {label}")

    # 添加装饰
    plt.title("Multiple Functions", fontsize=16)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.legend()
    plt.grid()
    plt.show()

