from netCDF4 import Dataset

# Указываем массив
nc_file = Dataset('cips_sci_3a_2007-335_v05.20_r05.nc', 'r')
# Указываем нужную переменную
data_variable1 = nc_file.variables['KM_PER_PIXEL'][:]
# Выводим результат в консоль компилятора
print("Км в пикселе", data_variable1)
# Закрываем файл
nc_file.close()