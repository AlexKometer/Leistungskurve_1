from sort import bubblesort
from load_data import load_data
import matplotlib.pyplot as plt

if __name__ == "__main__":
    data = load_data('activity.csv')
    power_W = data['PowerOriginal']
    print(power_W)
    sorted_power_W = bubblesort(power_W)
    print(sorted_power_W)

    plt.plot(sorted_power_W)
    plt.title('Power Curve')
    plt.xlabel('Time (s)')
    plt.ylabel('Power (W)')
    plt.savefig('power_curve.png')
    plt.show()