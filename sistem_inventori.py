#REIVAN NAUFAL ARDHIANSYAH
#25416255201130
#IF25D

import csv

# ==========================
# Struktur Data: Linked List
# ==========================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

# ==========================
# Struktur Data: Hash Map
# ==========================
class InventoryHashMap:
    def __init__(self):
        self.map = {}

    def add(self, item_id, data):
        self.map[item_id] = data

    def get(self, item_id):
        return self.map.get(item_id, None)

    def update(self, item_id, new_data):
        if item_id in self.map:
            self.map[item_id] = new_data
            return True
        return False

    def delete(self, item_id):
        if item_id in self.map:
            del self.map[item_id]
            return True
        return False

# ==========================
# Fungsi CSV
# ==========================
def load_csv(filename):
    linked_list = LinkedList()
    hashmap = InventoryHashMap()
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                linked_list.append(row)
                hashmap.add(row['ID'], row)
    except FileNotFoundError:
        # Jika file belum ada, buat dengan data awal
        print("File tidak ditemukan, membuat baru dengan data inventori awal...")
        initial_data = [
            {"ID": "B001", "Nama": "Mouse Wireless", "Jumlah": "25", "Harga": "150000"},
            {"ID": "B002", "Nama": "Keyboard Mechanical", "Jumlah": "15", "Harga": "450000"},
            {"ID": "B003", "Nama": "Monitor 24 Inch", "Jumlah": "10", "Harga": "1750000"},
            {"ID": "B004", "Nama": "Flashdisk 32GB", "Jumlah": "40", "Harga": "85000"},
            {"ID": "B005", "Nama": "Laptop Stand", "Jumlah": "20", "Harga": "120000"},
            {"ID": "B006", "Nama": "Headset Gaming", "Jumlah": "12", "Harga": "350000"},
            {"ID": "B007", "Nama": "Webcam HD", "Jumlah": "8", "Harga": "250000"},
            {"ID": "B008", "Nama": "Harddisk 1TB", "Jumlah": "5", "Harga": "950000"},
            {"ID": "B009", "Nama": "USB Hub 4 Port", "Jumlah": "30", "Harga": "65000"},
            {"ID": "B010", "Nama": "Powerbank 10000mAh", "Jumlah": "18", "Harga": "220000"}
        ]
        for row in initial_data:
            linked_list.append(row)
            hashmap.add(row['ID'], row)
        save_csv(filename, hashmap)
    return linked_list, hashmap

def save_csv(filename, hashmap):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['ID', 'Nama', 'Jumlah', 'Harga']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in hashmap.map.values():
            writer.writerow(item)

# ==========================
# Searching
# ==========================
def linear_search(data_list, key):
    for item in data_list:
        if item["ID"] == key:
            return item
    return None

def binary_search(sorted_list, key):
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid]["ID"] == key:
            return sorted_list[mid]
        elif sorted_list[mid]["ID"] < key:
            low = mid + 1
        else:
            high = mid - 1
    return None

# ==========================
# Sorting
# ==========================
def bubble_sort(data_list, key="Harga"):
    n = len(data_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if int(data_list[j][key]) > int(data_list[j+1][key]):
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
    return data_list

def quick_sort(data_list, key="Harga"):
    if len(data_list) <= 1:
        return data_list
    pivot = data_list[len(data_list)//2]
    left = [x for x in data_list if int(x[key]) < int(pivot[key])]
    middle = [x for x in data_list if int(x[key]) == int(pivot[key])]
    right = [x for x in data_list if int(x[key]) > int(pivot[key])]
    return quick_sort(left, key) + middle + quick_sort(right, key)

# ==========================
# Main Program CLI
# ==========================
def main():
    filename = "inventori.csv"
    linked_list, hashmap = load_csv(filename)

    while True:
        print("\n=== Sistem Inventori ===")
        print("1. Tambah Barang")
        print("2. Lihat Barang")
        print("3. Update Barang")
        print("4. Hapus Barang")
        print("5. Cari Barang")
        print("6. Urutkan Barang")
        print("7. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            item_id = input("ID: ")
            nama = input("Nama: ")
            jumlah = input("Jumlah: ")
            harga = input("Harga: ")
            data = {"ID": item_id, "Nama": nama, "Jumlah": jumlah, "Harga": harga}
            hashmap.add(item_id, data)
            save_csv(filename, hashmap)
            print("Barang berhasil ditambahkan!")

        elif pilihan == "2":
            linked_list.display()

        elif pilihan == "3":
            item_id = input("Masukkan ID barang yang ingin diupdate: ")
            if hashmap.get(item_id):
                nama = input("Nama baru: ")
                jumlah = input("Jumlah baru: ")
                harga = input("Harga baru: ")
                new_data = {"ID": item_id, "Nama": nama, "Jumlah": jumlah, "Harga": harga}
                hashmap.update(item_id, new_data)
                save_csv(filename, hashmap)
                print("Barang berhasil diupdate!")
            else:
                print("Barang tidak ditemukan.")

        elif pilihan == "4":
            item_id = input("Masukkan ID barang yang ingin dihapus: ")
            if hashmap.delete(item_id):
                save_csv(filename, hashmap)
                print("Barang berhasil dihapus!")
            else:
                print("Barang tidak ditemukan.")

        elif pilihan == "5":
            key = input("Masukkan ID barang yang dicari: ")
            data_list = list(hashmap.map.values())
            result = linear_search(data_list, key)
            if result:
                print("Barang ditemukan:", result)
            else:
                print("Barang tidak ditemukan.")

        elif pilihan == "6":
            print("1. Bubble Sort")
            print("2. Quick Sort")
            sort_choice = input("Pilih metode: ")
            data_list = list(hashmap.map.values())
            if sort_choice == "1":
                sorted_data = bubble_sort(data_list, key="Harga")
            else:
                sorted_data = quick_sort(data_list, key="Harga")
            for item in sorted_data:
                print(item)

        elif pilihan == "7":
            print("Keluar program...")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
