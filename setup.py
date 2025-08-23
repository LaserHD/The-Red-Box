from cx_Freeze import setup, Executable
import sys

version = "1.1"

build_options = {
    "packages": ["pygame"],
    "excludes": [],
    "include_files": ["Textures/","sounds/"],
}

base = "Win32GUI" if sys.platform == "win32" else None

executables = [Executable("main.py", base=base, target_name="The Red Box")]

setup(
    name="The Red Box",
    version=version,
    description="The Red Box game",
    options={"build_exe": build_options},
    executables=executables,
)