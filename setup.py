from cx_Freeze import setup, Executable

# Archivos y carpetas que quieres incluir
include_files = [
    ("PLUGINS", "PLUGINS"),
    ("TOOLS", "TOOLS"),
    ("pingu.ico", "pingu.ico")
]

# Modo consola (no ocultar ventana)
base = None

executables = [
    Executable(
        script="Pingu.py",
        base=base,
        icon="pingu.ico",
        target_name="Pingu.exe"
    )
]

setup(
    name="Pingu",
    version="1.0",
    description="Herramienta Pingu CLI con PIL y Colorama",
    options={
        "build_exe": {
            "packages": ["os", "sys", "platform", "colorama", "PIL"],
            "include_files": include_files,
            "include_msvcr": True  # 👈 importante, explicado abajo
        }
    },
    executables=executables
)
