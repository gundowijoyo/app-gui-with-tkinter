from cx_Freeze import setup, Executable

setup(
    name="tambah barang",
    version="1.0",
    description="Simple app",
    executables=[Executable("app.py")]  # Ganti "main.py" dengan nama file utama aplikasi Anda
)
