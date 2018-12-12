import typing
import random
import matplotlib.pyplot as plt
 
 
def predict_next(input_data: list, round_to_int: bool = False) -> typing.Union[float, int]:
    prediction = sum(input_data) / len(input_data) * (random.uniform(0.95, 1.05))
    return int(round(prediction)) if round_to_int else prediction
 
 
#data = [5000, 5000, 7000, 7000]
 
data_1 = [91.25, 92.5, 96.25, 87.5]
p1 = [87.5]
data_2 = [631.25, 587.5, 625.0, 716.25]
p2 = [716.25]
data_3 = [83.75, 89.0, 86.5, 90.5]
p3 = [90.5]
data_4 = [325.0, 310.0, 276.25, 245.5]
p4 = [245.5]
data_5 = [245.5, 245.5, 221.5, 221.5]
p5 = [221.5]

data = []
data.append(data_1)
data.append(data_2)
data.append(data_3)
data.append(data_4)
data.append(data_5)
datap = []
datap.append(p1)
datap.append(p2)
datap.append(p3)
datap.append(p4)
datap.append(p5)

for j in range (0,4):
    for i in range (0,5):
        data[i].append(predict_next(data[i]))
        datap[i].append(predict_next(data[i]))

for p in range (0,5):
    data[p] = data[p][:4]
    print (data[p])

x1 = [1, 2, 3, 4]
x2 = [4, 5, 6, 7, 8]

for g in range (0,5):
    plt.plot(x1, data[g], color='blue')
    plt.plot(x2, datap[g], color='red')
plt.show()
