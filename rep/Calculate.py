import cv2
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog, Tk
import os

fractions = 12
inner_radius = 40  # Внутренний радиус кольца
outer_radius = 535  # Внешний радиус кольца

# Создание маски
def slice_mask(image, center, inner_radius, outer_radius, start_angle, end_angle):
    h, w = image.shape[:2]
    mask = np.zeros((h, w), dtype=np.uint8)

    # Расчёт начальной и конечной точек для каждого угла
    start_point = (int(center[0] + outer_radius * np.cos(np.radians(start_angle))),
                   int(center[1] + outer_radius * np.sin(np.radians(start_angle))))
    end_point = (int(center[0] + outer_radius * np.cos(np.radians(end_angle))),
                 int(center[1] + outer_radius * np.sin(np.radians(end_angle))))

    # Рисуем линии от центра к краю маски
    cv2.line(mask, center, start_point, 255, 1)
    cv2.line(mask, center, end_point, 255, 1)

    # Рисуем два дуги для внешнего и внутреннего радиуса
    cv2.ellipse(mask, center, (outer_radius, outer_radius), 0, start_angle, end_angle, 255, -1)
    cv2.ellipse(mask, center, (inner_radius, inner_radius), 0, start_angle, end_angle, 0, -1)
    return mask

# Настройка интерфейса пользователя для выбора директории
root = tk.Tk()
root.withdraw()  # Не показываем основное окно Tkinter
folder_selected = filedialog.askdirectory()  # Пользователь выбирает папку
root.destroy()  # Закрыть окно после выбора


# Создание окна с выбором фонового изображения
def choose_background():
    def set_north():
        global background_path
        background_path = 'without_pmc.png'
        selection_window.destroy()

    def set_south():
        global background_path
        background_path = 'without_pmc_south.png'
        selection_window.destroy()

    selection_window = tk.Tk()
    selection_window.title("Выбор фона")

    label = tk.Label(selection_window, text="Выберите фон: ")
    label.pack(pady=10)

    button_north = tk.Button(selection_window, text="Север", command=set_north)
    button_north.pack(side="left", padx=20, pady=20)

    button_south = tk.Button(selection_window, text="Юг", command=set_south)
    button_south.pack(side="right", padx=20, pady=20)

    selection_window.mainloop()


# Запуск выбора фонового изображения
choose_background()

# Загрузка выбранного фонового изображения
background = cv2.imread(background_path, cv2.IMREAD_GRAYSCALE)
# Множитель для преобразования пикселей в квадратные километры
PIXEL_TO_KM2 = 7.5

# Функция для расчёта площади секторов
def calculate_sector_areas(image, background):
    # Применение алгоритма вычитания фона
    foreground = cv2.absdiff(image, background)
    # Конвертация изображения в бинарный формат
    _, thresh = cv2.threshold(foreground, 20, 255, cv2.THRESH_BINARY)
    # Вычисление координат центра изображения и радиуса
    center = (int(image.shape[0] / 2), int(image.shape[1] / 2))
    radius = min(center)

    sector_areas = np.zeros(12)
    for i in range(12):
        start_angle = 90 - (i + 1) * 30  # Начальный угол сектора
        end_angle = 90 - (i) * 30  # Конечный угол сектора

        # Создание маски для сектора
        sector_mask = slice_mask(image, center, inner_radius, outer_radius, start_angle, end_angle)

        # Применение маски и вычисление количества пикселей
        sector_pixels = np.sum(cv2.bitwise_and(thresh, thresh, mask=sector_mask) > 0)

        # Преобразование пикселей в площадь
        sector_area = sector_pixels * PIXEL_TO_KM2
        sector_areas[i] = sector_area

    return sector_areas


# DataFrame для результатов
results_df = pd.DataFrame(columns=[f'Sector {i+1}' for i in range(fractions)])

# Чтение и обработка изображений
image_filenames = [filename for filename in os.listdir(folder_selected) if filename.endswith(".png")]
image_filenames.sort()  # Сортировка имен файлов, если требуется

for index, filename in enumerate(image_filenames, start=1):
    filepath = os.path.join(folder_selected, filename)
    image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    sector_areas = calculate_sector_areas(image, background)  # Убедитесь, что функция принимает нужные аргументы

    # Добавляем результаты для каждого изображения как новую строку в DataFrame
    results_df.loc[f'№ {index}'] = sector_areas

# Сохранение результатов в Excel файл
excel_path = os.path.join(folder_selected, 'surface_area.xlsx')
results_df.to_excel(excel_path, index_label='№')

# Выводим путь к сохраненному Excel файлу
print(f'Results saved to {excel_path}')
