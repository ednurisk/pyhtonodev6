import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Adım: Rastgele Koordinatlar Üretme ve Excel Dosyasına Kaydetme
num_points = 500
x_coords = np.random.randint(0, 1001, num_points)
y_coords = np.random.randint(0, 1001, num_points)

# Bu koordinatları bir DataFrame'e koy
df = pd.DataFrame({
    'X Koordinatları': x_coords,
    'Y Koordinatları': y_coords
})

# DataFrame'i bir Excel dosyasına kaydet
excel_path = 'koordinatlar.xlsx'
df.to_excel(excel_path, index=False)
print(f"Excel dosyası '{excel_path}' olarak kaydedildi.")

# 2. Adım: Excel Dosyasını Okuma ve Görselleştirme
# Excel dosyasını oku
df = pd.read_excel(excel_path)

# Koordinatları al
x_coords = df['X Koordinatları']
y_coords = df['Y Koordinatları']

# 200x200 ızgaralara böl ve her ızgaraya rastgele bir renk ata
grid_size = 200
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'cyan', 'magenta', 'brown', 'pink']

plt.figure(figsize=(10, 10))

for x in range(0, 1000, grid_size):
    for y in range(0, 1000, grid_size):
        # Bu ızgaraya düşen noktaları seç
        mask = (x_coords >= x) & (x_coords < x + grid_size) & (y_coords >= y) & (y_coords < y + grid_size)
        points = df[mask]
        color = np.random.choice(colors)
        plt.scatter(points['X Koordinatları'], points['Y Koordinatları'], color=color)

plt.xlabel('X Koordinatları')
plt.ylabel('Y Koordinatları')
plt.title('Rastgele Noktaların Görselleştirilmesi')
plt.show()
