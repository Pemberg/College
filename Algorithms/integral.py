import numpy as np
import pandas as pd

# Definicje stałych
prismBase = 1000  # [m] długość boku prostopadłościanu
G = 6.67259 * 10 ** (-11)  # [m^3*kg^-1*s^-2] stała grawitacji
ro = 2670  # [g*cm^-3] gęstość

# Wczytanie danych z pliku Excel
excel_file_path = r'C:\Users\szatr\OneDrive\Pulpit\Studia\V semestr\Geostata\Dane.xlsx'
df_data = pd.read_excel(excel_file_path, sheet_name='Graw_dane_17')
df_NMT = pd.read_excel(excel_file_path, sheet_name='Graw_NMT')

# Utworzenie pliku wynikowego
results_file = 'results.txt'


# Definicje funkcji potrzebnych do obliczenia poprawki terenowej
# Definicja funkcji l
def l(x, y, z):
    return np.sqrt(x ** 2 + y ** 2 + z ** 2)


# Definicja funkcji f
def f(x, y, z):
    return -x * np.log(y + l(x, y, z)) - y * np.log(x + l(x, y, z)) + z * np.arctan((x * y) / (z * l(x, y, z)))


terrain_correction = []

# Dla każdego punktu pomiarowego
for i in range(len(df_data)):
    delta_g_ter = 0  # Poprawka terenowa dla danego punktu pomiarowego

    # Dla każdego punktu siatki
    for k in range(len(df_NMT)):
        distance = np.sqrt((df_NMT['NCN'].iloc[k] - df_data['NG'].iloc[i]) ** 2 + (
                    df_NMT['NCE'].iloc[k] - df_data['EG'].iloc[i]) ** 2 + (
                                       df_NMT['Hnorm'].iloc[k] - df_data['H'].iloc[i]) ** 2)

        if distance <= 1200:
            # Ograniczenia prostopadłościanu
            x_1 = np.abs(df_NMT['NCN'].iloc[k] - df_data['NG'].iloc[i]) - prismBase / 2
            x_2 = np.abs(df_NMT['NCN'].iloc[k] - df_data['NG'].iloc[i]) + prismBase / 2
            y_1 = np.abs(df_NMT['NCE'].iloc[k] - df_data['EG'].iloc[i]) - prismBase / 2
            y_2 = np.abs(df_NMT['NCE'].iloc[k] - df_data['EG'].iloc[i]) + prismBase / 2

            # Obliczenie wysokości graniastosłupa
            if df_data['H'].iloc[i] < df_NMT['Hnorm'].iloc[k]:
                z_1 = df_data['H'].iloc[i]
                z_2 = df_NMT['Hnorm'].iloc[k]
            else:
                z_1 = df_NMT['Hnorm'].iloc[k]
                z_2 = df_data['H'].iloc[i]

            # Unikanie dzielenia przez zero lub logarytm wartości niedodatnej
            if l(x_1, y_2, z_2) == 0 or l(x_2, y_1, z_2) == 0 or l(x_2, y_2, z_1) == 0:
                continue

            # Obliczenie poprawki terenowej dla pojedynczego prostopadłościanu
            delta_g_T = f(x_2, y_2, z_2) - f(x_1, y_2, z_2) - f(x_2, y_1, z_2) + f(x_1, y_1, z_2) - f(x_2, y_2, z_1) + f(x_1, y_2, z_1) + f(x_2, y_1, z_1) - f(x_1, y_1, z_1)
            delta_g_ter += delta_g_T

    # Pomnożenie wyniku przez stałe i zamiana jednostek
    delta_g_ter *= G * ro * 100000  # ro zamieniamy na [kg * m^3]
    terrain_correction.append(delta_g_ter)

with open(results_file, 'w') as plik:
    for wynik in terrain_correction:
        plik.write(str(wynik) + "\n")
# Zamknięcie pliku wynikowego
print(sum(terrain_correction))