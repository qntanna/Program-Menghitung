# Program menghitung mean, median, modus, kuartil, range 
# Lintan N. Azhar G - 150021013

import streamlit as st

def hitung_mean(data):
    return sum(data) / len(data)

def hitung_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        return sorted_data[n//2]

def hitung_modus(data):
    count_dict = {}
    for item in data:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    max_count = max(count_dict.values())
    modus = [key for key, value in count_dict.items() if value == max_count]
    return modus

def hitung_kuartil(data, k):
    sorted_data = sorted(data)
    n = len(sorted_data)
    index = k * (n + 1) / 4
    if index.is_integer():
        return sorted_data[int(index) - 1]
    else:
        return (sorted_data[int(index) - 1] + sorted_data[int(index)]) / 2

def hitung_range(data):
    return max(data) - min(data)

st.title("Kalkulator Statistik")

data_string = st.text_input("Masukkan data dipisahkan dengan koma (,)")

if st.button("Hitung"):
  try:
    data = [float(x) for x in data_string.split(",")]
    
    st.write("Data:", data)
    st.write("Mean:", hitung_mean(data))
    st.write("Median:", hitung_median(data))
    st.write("Modus:", hitung_modus(data))
    st.write("Kuartil Q1:", hitung_kuartil(data, 1))
    st.write("Kuartil Q2:", hitung_kuartil(data, 2))
    st.write("Kuartil Q3:", hitung_kuartil(data, 3))
    st.write("Range:", hitung_range(data))
  except ValueError:
    st.error("Input tidak valid. Masukkan angka yang dipisahkan dengan koma (,).")
