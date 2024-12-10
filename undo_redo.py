def menu():
    print("1. tambahkan aksi")
    print("2. undo")
    print("3. redo")
    print("4. stack undo and redo")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan Anda: ")
    return pilihan

while True:
    pilihan = menu()

    if pilihan == "1":
        print("menjalankan office word")
    
    elif pilihan == "2":
       print("membuka google crome")
    
    elif pilihan == "3":
        print("menjalankan visual studio code")
        break
    
    else:
        print("Pilihan tidak valid,harap coba lagi")
