import pyodbc

# Informasi koneksi ke SQL Server
server = 'KKI-NB-001\SQLEXPRESS'  # Nama server SQL Server
database = 'DemoDB'  # Nama database yang ingin Anda akses
# username = 'nama_pengguna'  # Nama pengguna SQL Server
# password = 'password_anda'  # Kata sandi SQL Server

# Membuat connection string
conn_str = (
    f'DRIVER={{SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    # f'UID={username};'
    # f'PWD={password};'
)

# Membuat koneksi
conn = pyodbc.connect(conn_str)

# Membuat cursor untuk melakukan query
cursor = conn.cursor()

# Contoh query SQL
cursor.execute('SELECT * FROM demo_table')

# Mendapatkan hasil query
for row in cursor.fetchall():
    print(row)

# Menutup koneksi
conn.close()