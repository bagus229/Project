import re

class Data:
    def __init__(self):
        self.suhu = None
        self.satuan = None

    def set_suhu(self, suhu, satuan):
        self.suhu = suhu
        self.satuan = satuan

    def get_suhu(self):
        return self.suhu

    def get_satuan(self):
        return self.satuan


class Process:
    def __init__(self, data):
        self.data = data

    def konversi(self):
        suhu = self.data.get_suhu()
        satuan = self.data.get_satuan()
        
        if satuan == "Celsius":
            return self.konversi_celsius(suhu)
        elif satuan == "Fahrenheit":
            return self.konversi_fahrenheit(suhu)
        elif satuan == "Kelvin":
            return self.konversi_kelvin(suhu)
    
    def konversi_celsius(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        return celsius, fahrenheit, kelvin 
    
    def konversi_fahrenheit(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        kelvin = celsius + 273.15
        return celsius, fahrenheit, kelvin  
    
    def konversi_kelvin(self, kelvin):
        celsius = kelvin - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return celsius, fahrenheit, kelvin 

class View:
    def tampilkan_tabel(self, suhu_awal, satuan_awal, suhu_celsius, suhu_fahrenheit, suhu_kelvin):
        suhu_awal_str = f"{suhu_awal:.2f} {satuan_awal}" if suhu_awal is not None else "-"
        suhu_celsius_str = f"{suhu_celsius:.2f} C" if suhu_celsius is not None else "-"
        suhu_fahrenheit_str = f"{suhu_fahrenheit:.2f} F" if suhu_fahrenheit is not None else "-"
        suhu_kelvin_str = f"{suhu_kelvin:.2f} K" if suhu_kelvin is not None else "-"
        
        print("\n+-----------------+----------------+")
        print(f"| Input Suhu      | {suhu_awal_str:14} |")
        print("+-----------------+----------------+")
        print(f"| Dalam Celsius   | {suhu_celsius_str:14} |")
        print(f"| Dalam Fahrenheit| {suhu_fahrenheit_str:14} |")
        print(f"| Dalam Kelvin    | {suhu_kelvin_str:14} |")
        print("+-----------------+----------------+")

class InputValidator:
    @staticmethod
    def validasi_input(user_input):
        if re.match(r"^[+-]?([0-9]*[.])?[0-9]+$", user_input):
            return True
        return False

    @staticmethod
    def validasi_satuan(user_input):
        return user_input.lower() in ['celsius', 'fahrenheit', 'kelvin']

def main():
    data = Data()
    process = Process(data)
    view = View()

    while True:
        suhu_input = input("Masukkan suhu: ")
        if InputValidator.validasi_input(suhu_input):
            suhu = float(suhu_input)
            break
        else:
            print("Input tidak valid. Masukkan angka yang benar.")

    while True:
        satuan_input = input("Masukkan satuan suhu (Celsius, Fahrenheit, Kelvin): ").lower()
        if InputValidator.validasi_satuan(satuan_input):
            break
        else:
            print("Satuan tidak valid. Pilih antara 'Celsius', 'Fahrenheit', atau 'Kelvin'.")

    data.set_suhu(suhu, satuan_input.capitalize())

    suhu_terkonversi_1, suhu_terkonversi_2, suhu_terkonversi_3 = process.konversi()

    if satuan_input.lower() == "kelvin":
        view.tampilkan_tabel(suhu, satuan_input.capitalize(), suhu_terkonversi_1, suhu_terkonversi_2, suhu_terkonversi_3)
    elif satuan_input.lower() == "celsius":
        view.tampilkan_tabel(suhu, satuan_input.capitalize(), suhu_terkonversi_1, suhu_terkonversi_2, suhu_terkonversi_3)
    else:
        view.tampilkan_tabel(suhu, satuan_input.capitalize(), suhu_terkonversi_1, suhu_terkonversi_2, suhu_terkonversi_3)


if __name__ == "__main__":
    main()