undo_stack = []
redo_stack = []
aksi_berikutnya = ""

# aksi 
"menjalankan office word"
"membuka google crome"
"menjalankan visual studio code"

def menu():
    print("\nMenu:")
    print("1. Tambahkan aksi")
    print("2. Undo")
    print("3. Redo")
    print("4. Lihat stack undo dan redo")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan Anda dari 1-5: ")
    return pilihan

# Inisialisasi stack untuk undo dan redo
undo_stack = []
redo_stack = []

while True:
    pilihan = menu()

    if pilihan == "1":
        action = input("Masukkan aksi yang ingin ditambahkan: ")
        undo_stack.append(action)  
        print(f"Aksi: {action}")
        redo_stack.clear()  

    elif pilihan == "2":
        if undo_stack:
            action = undo_stack.pop()  
            redo_stack.append(action)  
            print(f"undo: {action}")
        else:
            print("Tidak ada aksi untuk di undo.")

    elif pilihan == "3":
        if redo_stack:
            action = redo_stack.pop()  
            undo_stack.append(action)   
            print(f"redo: {action}")
        else:
            print("Tidak ada aksi untuk di redo.")

    elif pilihan == "4":
        print("Stack Undo:", undo_stack)
        print("Stack Redo:", redo_stack)

    elif pilihan == "5":
        print("Keluar dari program ")
        break

    else:
        print("Pilihan tidak valid, harap coba lagi")
