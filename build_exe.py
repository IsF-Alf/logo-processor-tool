import PyInstaller.__main__
import os
import shutil

# Define the project directory
project_dir = os.path.dirname(os.path.abspath(__file__))

# Create a build directory if it doesn't exist
build_dir = os.path.join(project_dir, 'build')
if not os.path.exists(build_dir):
    os.makedirs(build_dir)

# PyInstaller command line arguments
pyinstaller_args = [
    'logo_gui.py',                      # Your script
    '--name=LogoProcessorTool',         # Name of the executable
    '--onefile',                        # Create a single executable file
    '--windowed',                       # Hide the console window
    '--icon=NONE',                      # No icon (you can specify an .ico file here)
    '--add-data=README.md;.',           # Include README
    '--add-data=LICENSE;.',             # Include LICENSE
    f'--distpath={os.path.join(project_dir, "dist")}',  # Output directory
    f'--workpath={os.path.join(project_dir, "build")}', # Working directory
    '--clean',                          # Clean PyInstaller cache
]

# Run PyInstaller
PyInstaller.__main__.run(pyinstaller_args)

print("Build completed successfully!")
print(f"Executable can be found in: {os.path.join(project_dir, 'dist')}")
