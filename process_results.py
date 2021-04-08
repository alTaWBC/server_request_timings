import os
import numpy as np
import matplotlib.pyplot as plt

folder = r"C:\Users\WilliamCosta\Desktop\tese_repositories\server_request_timings\result_files"
filenames = [os.path.join(folder, filename)
             for filename in os.listdir(folder) if 'min.txt' in filename]

durations = {

}


for filename in filenames:
    time = filename.split('\\')[-1].split('min')[0]
    time_durations = []
    with open(filename) as durations_file:
        lines = durations_file.readlines()
        for line in lines:
            time_durations.append([float(f) for f in line.split(',')])
    durations[time] = np.array(time_durations)
    print(time, durations[time].shape)


fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(
    nrows=2, ncols=2, figsize=(10, 10))

for duration in durations:
    print(duration)
    axis = [ax0, ax1, ax2, ax3][['5', '30', '60', '120'].index(duration)]
    request_times = durations[duration][8:, 1:]
    axis.hist(request_times.flatten(), bins=50)
    axis.set_xlim(0, 4.5)
    axis.set_ylim(0, 900)
    axis.set_ylabel("Number of requests")
    axis.set_xlabel("Round Trip Time (in seconds)")
    axis.set_title(f'{duration} minutes interval')

    mean = np.mean(durations[duration][8:, 1:])
    std = np.std(durations[duration][8:, 1:])
    print(f"60 requests {duration}min interval: {mean:0.3f}ms +-{std:0.3f}ms")
    for interval in range(5, 61, 5):

        mean = np.mean(durations[duration][8:, 1 + interval - 5: interval])
        std = np.std(durations[duration][8:, 1 + interval - 5: interval])
        print(f"\t {interval - 5}-{interval}: {mean:0.3f}ms +-{std:0.3f}ms")

fig.tight_layout()
plt.savefig('requests.jpg')
plt.show()
plt.close()

# %%%
for duration in durations:
    print(duration,"mins interval")
    fig, ((ax0, ax1, ax2), (ax3, ax4, ax5)) = plt.subplots(
        nrows=2, ncols=3, figsize=(10, 10))
    for interval in range(5, 30, 5):
        axis = [ax0, ax1, ax2, ax3, ax4][[5, 10, 15, 20, 25, 30].index(interval)]
        request_times = durations[duration][8:, 1 + interval - 5: interval]
        axis.hist(request_times.flatten(), bins=50)
        axis.set_xlim(0, 4.5)
        axis.set_ylim(0, 50)
        axis.set_ylabel("Number of requests")
        axis.set_xlabel("Round Trip Time (in seconds)")
        axis.set_title(f'Requests {interval-5}-{interval}')
    request_times = durations[duration][8:, 25:]
    ax5.hist(request_times.flatten(), bins=50)
    axis.set_ylim(0, 50)
    axis.set_ylabel("Number of requests")
    axis.set_xlabel("Round Trip Time (in seconds)")
    axis.set_title(f'Requests 25-60')
    plt.show()
    plt.close()
        
        # mean = np.mean(durations[duration][8:, 1 + interval - 5: interval])
        # std = np.std(durations[duration][8:, 1 + interval - 5: interval])
        # print(f"\t {interval - 5}-{interval}: {mean:0.3f}ms +-{std:0.3f}ms")

# 120
# 1121 \pm 763 & 834 \pm 188 & 827 \pm 264 & 847 \pm 232 & 814 \pm 274 & 822 \pm 219 & 796 \pm 186 & 829 \pm 233 & 822 \pm 230 & 758 \pm 162 & 747 \pm 123 & 717 166

# 30
# 732 \pm 247 & 817 \pm 394 & 744 \pm 328 & 711 \pm 237 & 710 \pm 202 & 757 \pm 239 & 734 \pm 231 & 737 \pm 238 & 750 \pm 201 & 708 \pm 167 & 738 \pm 252 & 738 \pm 289 & 702 234

# 5
# 691 \pm 193 & 723 \pm 373 & 691 \pm 183 & 732 \pm 291 & 704 \pm 175 & 702 \pm 156 & 712 \pm 128 & 711 \pm 193 & 688 \pm 133 & 686 \pm 124 & 666 \pm 125 & 675 \pm 168 & 659 187

# 60
# 730 \pm 277 & 826 \pm 382 & 694 \pm 157 & 724 \pm 254 & 717 \pm 201 & 806 \pm 496 & 738 \pm 167 & 715 \pm 182 & 704 \pm 163 & 712 \pm 283 & 744 \pm 317 & 710 \pm 200 & 686 281

# %%
