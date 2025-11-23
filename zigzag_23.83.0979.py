import time, sys

# --- ANSI COLOR CODES ---
COLORS = [
    '\033[31m', # Merah
    '\033[33m', # Kuning
    '\033[32m', # Hijau
    '\033[36m'  # Cyan
]
RESET = '\033[0m'
color_index = 0
# ------------------------

# --- INPUT PENGGUNA ---
print("====================================")
text_to_print = input("Masukkan teks yang ingin di-zig-zag: ")

try:
    max_cycles = int(input("Masukkan jumlah siklus zig-zag (e.g., 5): "))
except ValueError:
    print("Input siklus tidak valid, menggunakan 3 siklus secara default.")
    max_cycles = 3
    
# --- FITUR BARU: INPUT LEBAR ZIG-ZAG ---
try:
    # Minta input untuk lebar maksimal indentasi
    user_max_indent = int(input("Masukkan lebar maksimal zig-zag (indentasi, e.g., 20): "))
    if user_max_indent <= 0:
        print("Lebar harus lebih dari 0. Menggunakan 20 secara default.")
        MAX_INDENT = 20
    else:
        MAX_INDENT = user_max_indent
except ValueError:
    print("Input lebar tidak valid, menggunakan 20 secara default.")
    MAX_INDENT = 20

# --- Peningkatan: Input Kecepatan Animasi (0.1 detik) ---
try:
    animation_speed = float(input("Masukkan jeda waktu (detik) untuk animasi (e.g., 0.1): "))
    if animation_speed <= 0:
        print("Jeda harus lebih dari 0. Menggunakan 0.1 detik secara default.")
        animation_speed = 0.1
except ValueError:
    print("Input jeda waktu tidak valid, menggunakan 0.1 detik secara default.")
    animation_speed = 0.1

print("====================================")
print(f"Mulai zig-zag teks '{text_to_print}' sebanyak {max_cycles} siklus.")
print(f"Lebar pergerakan maksimal diatur ke: {MAX_INDENT}.")
print("Tekan Ctrl+C untuk menghentikan kapan saja.")
print("====================================")

# --- VARIABEL INTI ---
indent = 0 
indentIncreasing = True 
cycles_done = 0
# ---------------------

try:
    while True: 
        # --- LOGIKA WARNA ---
        current_color = COLORS[color_index % len(COLORS)]
        
        # Mencetak teks dengan kode warna dan indentasi
        print(current_color + ' ' * indent + text_to_print + RESET) 
        
        # Pindah ke warna selanjutnya
        color_index += 1
        # --------------------
        
        time.sleep(animation_speed) # Menggunakan kecepatan yang diinput
        
        # --- LOGIKA INDENTASI ---
        if indentIncreasing:
            indent = indent + 1
            # Menggunakan MAX_INDENT yang diinput
            if indent >= MAX_INDENT:
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent <= 0:
                indentIncreasing = True
                
                # --- LOGIKA PENGHENTIAN ---
                cycles_done = cycles_done + 1 
                print(f"--- Siklus Selesai: {cycles_done}/{max_cycles} ---")
                
                if cycles_done >= max_cycles:
                    print("Batas siklus telah tercapai. Program berhenti otomatis.")
                    break 

except KeyboardInterrupt:
    print("\nProgram dihentikan secara manual.")
    sys.exit()

sys.exit()