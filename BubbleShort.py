
# Mengurutkan nilai mahasiswa menggunakan Bubble Sort

nilai = [85, 70, 90, 60, 75]

print("Nilai sebelum diurutkan:", nilai)

for i in range(len(nilai)):
    for j in range(len(nilai) - 1 - i):
        if nilai[j] > nilai[j + 1]:
            nilai[j], nilai[j + 1] = nilai[j + 1], nilai[j]

print("Nilai setelah diurutkan:", nilai)
