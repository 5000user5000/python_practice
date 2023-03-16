import matplotlib.pyplot as plt

# 這裡是數據，你需要換成你自己的數據
x_values1_up = [1.4,2.83,2.88,4.23,5.75,6.1,6.07,6.08,6.54] #duty15
x_values1_down = [1.26,0.85,0.72,0.76,1.09,6.09,7.59,7.19,7.09] #duty15

x_values2_up = [2.86,1.83,2.19,3.48,4.87,6.13,6.78,7.29,7.4] #duty17
x_values2_down = [1.23,1.16,1.5,1.01,1.56,6.27,8.66,8.43,8.16] #duty17

x_values3_up = [2.55,2.5,5.03,7.45,7.72,8.17,8.41,8.55,8.68] #duty20
x_values3_down = [1.48,1.44,1.51,1.47,1.36,3.22,9.16,9.88,9.78] #duty20

y_values = [0,4,8,12,16,20,24,28,30] #height

# 設置圖表的標題和軸標籤
plt.title('downstream and upstream velocity distribution under different fan duties')
plt.xlabel('velocity (m/s)')
plt.ylabel('height (cm)')

# 將數據繪製成折線圖
plt.plot(x_values1_up, y_values, label='duty 15 upstream vel', marker='o')
plt.plot(x_values1_down, y_values, label='duty 15 downstream vel', marker='o')
plt.plot(x_values2_up, y_values, label='duty 17 upstream vel', marker='o')
plt.plot(x_values2_down, y_values, label='duty 17 downstream vel', marker='o')
plt.plot(x_values3_up, y_values, label='duty 20 upstream vel', marker='o')
plt.plot(x_values3_down, y_values, label='duty 20 downstream vel', marker='o')


# 設置圖例字體大小
plt.rcParams.update({'font.size': 8})

# 添加圖例
plt.legend()

# 顯示圖表
plt.show()
