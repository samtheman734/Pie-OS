from pathlib import Path
import os
import subprocess
import json

# Initialize directory contents
general = []
docs = []
home = []

# Define installed apps with their system paths
installed_apps = {
    "Notepad": "C:\\Windows\\System32\\notepad.exe",
    "Calculator": "C:\\Windows\\System32\\calc.exe",
}

# Load data from savefile.json if it exists
def load_data():
    if os.path.exists('savefile.pie'):
        try:
            with open('savefile.pie', 'r') as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
    # Defaults if no save file or error
    return {
        "general": [],
        "docs": [],
        "home": [],
        "installed_apps": installed_apps,
    }

data = load_data()
general = data["general"]
docs = data["docs"]
home = data["home"]
# installed_apps could be loaded similarly if you want to persist them

# Ensure applications directory exists
Path("applications").mkdir(exist_ok=True)

def display_welcome():
    print("""
                                                                     
                 Welcome to Pie OS!                         
                                                                     
  Boot sequence initiated... Loading core modules and               
  environment. Ready for user commands.                              
  Version: 1.0.0 | Build: Pie-2026                                   
  Status: All systems operational. Ready to accept commands.         
  Note: This is an operating system that                             
  runs entirely in user space, designed for learning,                
  experimentation, and development.                                  
                                                                     
  Available Commands:                                                
    - help                  : Show this help message                
    - mk file               : Create a new file                     
    - open file             : Open and display a file               
    - list [directory]      : List files in a directory           
    - delete file           : Delete a specified file               
    - rename file           : Rename a file                         
    - search                : Search for text within files        
    - info                  : Show info about a file                
    - clear                 : Clear the terminal screen             
    - exit                  : Exit the system                       
    - applications          : List and launch apps                  
    - neutron               : Neutron Programming Language      
    - launch app            : Launch a real installed app
    - python                : Launch the python interpreter
                                                                     

""")

def list_directory(target):
    if target == "general":
        print("General directory files:", general)
    elif target == "documents":
        print("Documents directory files:", docs)
    elif target == "home":
        print("Home directory files:", home)
    else:
        print("Unknown directory.")

def show_help():
    print("""
Available commands:
- help                        : Show this help message
- mk file                     : Create a new file
- open file                   : Open and display a file
- list [directory]            : List files in a directory (general, documents, home)
- delete file                 : Delete a specified file
- rename file                 : Rename a file
- search                      : Search for text within files
- info                        : Show info about a file
- clear                       : Clear the terminal screen
- exit                        : Exit the program
- applications                : List installed apps and launch
- install app                 : Install a new app via Chocolatey
- launch app                  : Launch a real application
""")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def delete_file():
    filename = input("Enter filename to delete: ").strip()
    targetdir = input("Enter directory (general, documents, home): ").strip().lower()

    if targetdir == "general":
        dir_path = Path("general")
        if filename in general:
            general.remove(filename)
        else:
            print("File not listed in memory.")
    elif targetdir == "documents":
        if filename in docs:
            docs.remove(filename)
        else:
            print("File not listed in memory.")
        dir_path = Path("documents")
    elif targetdir == "home":
        if filename in home:
            home.remove(filename)
        else:
            print("File not listed in memory.")
        dir_path = Path("home")
    else:
        print("Unknown directory.")
        return

    file_path = dir_path / filename
    if file_path.exists():
        file_path.unlink()
        print(f"File '{filename}' deleted successfully.")
    else:
        print("File not found on disk.")

def rename_file():
    old_name = input("Enter current filename: ").strip()
    targetdir = input("Enter directory (general, documents, home): ").strip().lower()
    new_name = input("Enter new filename: ").strip()

    if targetdir == "general":
        dir_path = Path("general")
        if old_name in general:
            general.remove(old_name)
            general.append(new_name)
        else:
            print("File not listed in memory.")
    elif targetdir == "documents":
        if old_name in docs:
            docs.remove(old_name)
            docs.append(new_name)
        else:
            print("File not listed in memory.")
        dir_path = Path("documents")
    elif targetdir == "home":
        if old_name in home:
            home.remove(old_name)
            home.append(new_name)
        else:
            print("File not listed in memory.")
        dir_path = Path("home")
    else:
        print("Unknown directory.")
        return

    old_file = dir_path / old_name
    new_file = dir_path / new_name
    if old_file.exists():
        old_file.rename(new_file)
        print(f"File renamed from '{old_name}' to '{new_name}'.")
    else:
        print("Original file does not exist on disk.")

def search_in_files():
    search_term = input("Enter search term: ")
    found_files = []

    for dir_name, file_list in [("general", general), ("documents", docs), ("home", home)]:
        dir_path = Path(dir_name)
        for filename in file_list:
            file_path = dir_path / filename
            if file_path.exists():
                with file_path.open('r') as f:
                    contents = f.read()
                    if search_term in contents:
                        print(f"Found in {filename} ({dir_name})")
                        found_files.append((filename, dir_name))
    if not found_files:
        print("Search term not found in any files.")

def show_file_info():
    filename = input("Enter filename: ").strip()
    targetdir = input("Enter directory (general, documents, home): ").strip().lower()

    if targetdir == "general":
        dir_path = Path("general")
        list_ref = general
    elif targetdir == "documents":
        dir_path = Path("documents")
        list_ref = docs
    elif targetdir == "home":
        dir_path = Path("home")
        list_ref = home
    else:
        print("Unknown directory.")
        return

    if filename in list_ref:
        file_path = dir_path / filename
        if file_path.exists():
            size = file_path.stat().st_size
            print(f"File: {filename}")
            print(f"Size: {size} bytes")
            print(f"Path: {file_path.resolve()}")
        else:
            print("File does not exist on disk.")
    else:
        print("File not listed in memory.")

def list_apps():
    apps = os.listdir("applications")
    if apps:
        print("Installed applications:")
        for app in apps:
            print(f" - {app}")
    else:
        print("No applications installed.")

def install():
    app = input("Enter name of app you want to install: ").strip()
    # Run Chocolatey command
    result = subprocess.run(["choco", "install", app, "-y"], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{app} installed successfully.")
    else:
        print(f"Failed to install {app}.")
        print(result.stderr)

def launch_real_app():
    print("Available apps:")
    for app in installed_apps:
        print(f" - {app}")
    app_name = input("Enter app name to launch: ").strip().lower()
    app_path = installed_apps.get(app_name)
    if app_path:
        try:
            subprocess.Popen([app_path])
            print(f"Launching {app_name}...")
        except Exception as e:
            print(f"Failed to launch {app_name}: {e}")
    else:
        print("App not found in registered applications.")
        
def save_data():
    try:
        with open('savefile.pie', 'w') as f:
            json.dump({
                "general": general,
                "docs": docs,
                "home": home,
            }, f)
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")

# Start your program
display_welcome()

while True:
    command_input = input("[Command]: ").strip().lower()
    parts = command_input.split()

    if not parts:
        continue

    cmd = parts[0]

    if cmd == "help":
        show_help()

    elif cmd == "list" and len(parts) >= 2:
        list_directory(parts[1])

    elif cmd == "mk" and len(parts) >= 2 and parts[1] == "file":
        filename = input("Type name of file: ").strip()
        content = input("Type file contents: ")
        targetdir = input("Save to dir (general, documents, home): ").strip().lower()

        dir_path = Path(targetdir)
        if targetdir == "general":
            general.append(filename)
        elif targetdir == "documents":
            docs.append(filename)
        elif targetdir == "home":
            home.append(filename)
        else:
            print("Unknown directory. File not saved.")
            continue

        dir_path.mkdir(exist_ok=True)
        try:
            with (dir_path / filename).open('w') as f:
                f.write(content)
            print(f"File '{filename}' created successfully in '{targetdir}' directory.")
        except Exception as e:
            print(f"Error creating file: {e}")

    elif cmd == "open" and len(parts) >= 2 and parts[1] == "file":
        filename = input("Enter filename to open: ").strip()
        targetdir = input("Enter directory (general, documents, home): ").strip().lower()

        if targetdir == "general":
            dir_path = Path("general")
        elif targetdir == "documents":
            dir_path = Path("documents")
        elif targetdir == "home":
            dir_path = Path("home")
        else:
            print("Unknown directory.")
            continue

        file_path = dir_path / filename
        if file_path.exists():
            try:
                with file_path.open('r') as f:
                    print(f.read())
            except Exception as e:
                print(f"Error reading file: {e}")
        else:
            print("File not found.")

    elif cmd == "delete" and len(parts) >= 2 and parts[1] == "file":
        delete_file()

    elif cmd == "rename" and len(parts) >= 2 and parts[1] == "file":
        rename_file()
        
    elif cmd == "BASIC":
        interp.run()
        
    elif cmd == "search":
        search_in_files()

    elif cmd == "info":
        show_file_info()

    elif cmd == "clear":
        clear_screen()

    elif cmd == "python":
    # Python interactive shell
        code = input("Enter Python code to run (or 'exit' to stop):\n")
        while code.lower() != "exit":
            try:
                exec(code)
            except Exception as e:
                print(f"Error: {e}")
            code = input(">>> ")

    elif cmd == "neutron":
        try:
            exec(open("Neutron.py", encoding="utf-8").read())
        except Exception:
            print("Neutron closed.")

    elif cmd in ("exit", "quit"):
        print("Exiting program.")
        save_data()
        break

    elif cmd == "launch" and len(parts) >= 2 and parts[1] == "app":
        launch_real_app()

    else:
        print("Unknown command. Type 'help' for a list of commands.")
