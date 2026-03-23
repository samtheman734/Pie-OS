from pathlib import Path
import os
import subprocess
import json

# Define color codes
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Path setup
disk_path = Path("C:/Users/sam44/PIE_OS_DISK")
savefile_path = disk_path / "savefile.json"

# Initialize data structures
general = []
docs = []
home = []

# Define installed apps
installed_apps = {
    "notepad": "C:\\Windows\\System32\\notepad.exe",
    "calculator": "C:\\Windows\\System32\\calc.exe",
}

# Define devices function with color
def devices():
    blue = Colors.OKBLUE
    reset = Colors.ENDC

    print(f'{blue}CPU:{reset} Intel Core i7-10700K')
    print(f'{blue}GPU:{reset} NVIDIA GeForce RTX 3080')
    print(f'{blue}HDD:{reset} Seagate Barracuda 2TB')
    print(f'{blue}SSD:{reset} Samsung 970 EVO 1TB')
    print(f'{blue}RAM:{reset} Corsair Vengeance LPX 32GB')
    print(f'{blue}Motherboard:{reset} ASUS ROG Strix Z490-E')
    print(f'{blue}Power Supply:{reset} Corsair RM750x 750W')
    print(f'{blue}Network Adapter:{reset} Intel Ethernet I225-V')
    print(f'{blue}Sound Card:{reset} Creative Sound Blaster Z')
    print(f'{blue}Optical Drive:{reset} LG Blu-ray Combo Drive')
    print(f'{blue}Cooling System:{reset} Noctua NH-U12S')
    print(f'{blue}Monitor:{reset} Dell UltraSharp U2723QE')
    print(f'{blue}Keyboard:{reset} Logitech MX Keys')
    print(f'{blue}Mouse:{reset} Logitech MX Master 3')
    print(f'{blue}Printer:{reset} HP LaserJet Pro M404dn')

# Load existing data
def load_data():
    filename = 'savefile.json'
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"{Colors.WARNING}Error loading data: {e}{Colors.ENDC}")
    return {
        "general": [],
        "docs": [],
        "home": [],
        "installed_apps": installed_apps,
        "processes": [],
    }

data = load_data()
general = data.get("general", [])
docs = data.get("docs", [])
home = data.get("home", [])
installed_apps = data.get("installed_apps", installed_apps)

# Setup process manager
def load_processes():
    filename = 'savefile.json'
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f).get("processes", [])
        except:
            pass
    return []

process_manager = load_processes()

def start_process(command):
    try:
        proc = subprocess.Popen(command)
        process_manager.append({"pid": proc.pid, "command": command})
        print(f"{Colors.OKGREEN}Started process PID: {proc.pid}{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Failed to start process: {e}{Colors.ENDC}")

def show_processes():
    if not process_manager:
        print(f"{Colors.WARNING}No processes.{Colors.ENDC}")
    else:
        print(f"{Colors.HEADER}Active processes:{Colors.ENDC}")
        for p in process_manager:
            print(f"PID: {p['pid']} | Command: {' '.join(p['command'])}")

def save_processes():
    try:
        with open('savefile.json', 'w') as f:
            json.dump({"processes": process_manager}, f)
        print(f"{Colors.OKGREEN}Processes saved.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Error saving processes: {e}{Colors.ENDC}")

# Fake "system" processes
fake_system_processes = [
    {"pid": 101, "name": "Graphics Driver", "user": "SYSTEM"},
    {"pid": 102, "name": "Network Adapter", "user": "SYSTEM"},
    {"pid": 103, "name": "Display Manager", "user": "SYSTEM"},
    {"pid": 104, "name": "Sound Device", "user": "SYSTEM"},
    {"pid": 105, "name": "USB Controller", "user": "SYSTEM"},
    {"pid": 106, "name": "Storage Driver", "user": "SYSTEM"},
]

def show_fake_system_processes():
    print(f"{Colors.HEADER}Process Manager{Colors.ENDC}")
    for p in fake_system_processes:
        print(f"PID: {p['pid']} | Name: {p['name']} | User: {p['user']}")

# Display welcome message
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
    - startproc             : Start a new process
    - listprocs             : List all current processes
                                                                     
""" + Colors.ENDC)

# Directory listing
def list_directory(target):
    if target == "general":
        print(f"{Colors.OKBLUE}General directory files:{Colors.ENDC} {general}")
    elif target == "documents":
        print(f"{Colors.OKBLUE}Documents directory files:{Colors.ENDC} {docs}")
    elif target == "home":
        print(f"{Colors.OKBLUE}Home directory files:{Colors.ENDC} {home}")
    else:
        print(f"{Colors.WARNING}Unknown directory.{Colors.ENDC}")

# Help info
def show_help():
    print(Colors.OKBLUE + """
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
- startproc                   : Start a new process
- listprocs                   : List all current processes
""".replace('\n', '\n' + Colors.OKBLUE).replace('  ', '    ') + Colors.ENDC)

# Clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main command loop
if __name__ == "__main__":
    display_welcome()

    while True:
        command_input = input(Colors.OKGREEN + "[Command]: " + Colors.ENDC).strip().lower()
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

            if targetdir == "general":
                dir_path = Path("general")
                general.append(filename)
            elif targetdir == "documents":
                dir_path = Path("documents")
                docs.append(filename)
            elif targetdir == "home":
                dir_path = Path("home")
                home.append(filename)
            else:
                print(f"{Colors.WARNING}Unknown directory. File not saved.{Colors.ENDC}")
                continue

            try:
                dir_path.mkdir(parents=True, exist_ok=True)
                with (dir_path / filename).open('w') as f:
                    f.write(content)
                print(f"{Colors.OKGREEN}File '{filename}' created successfully in '{targetdir}' directory.{Colors.ENDC}")
            except Exception as e:
                print(f"{Colors.FAIL}Error creating file: {e}{Colors.ENDC}")

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
                print(f"{Colors.WARNING}Unknown directory.{Colors.ENDC}")
                continue

            file_path = dir_path / filename
            if file_path.exists():
                try:
                    with file_path.open('r') as f:
                        print(f.read())
                except Exception as e:
                    print(f"{Colors.FAIL}Error reading file: {e}{Colors.ENDC}")
            else:
                print(f"{Colors.WARNING}File not found.{Colors.ENDC}")

        elif cmd == "delete" and len(parts) >= 2 and parts[1] == "file":
            # You can replace the function call with the code directly if preferred.
            # For brevity, I am calling the existing function.
            # Make sure the delete_file() function is included above.
            delete_file()

        elif cmd == "rename" and len(parts) >= 2 and parts[1] == "file":
            rename_file()

        elif cmd == "search":
            search_in_files()

        elif cmd == "info":
            show_file_info()

        elif cmd == "clear":
            clear_screen()

        elif cmd == "devicemanager":
            devices()

        elif cmd == "python":
            code = input("Enter Python code to run (or 'exit' to stop):\n")
            while code.lower() != "exit":
                try:
                    exec(code)
                except Exception as e:
                    print(f"{Colors.FAIL}Error: {e}{Colors.ENDC}")
                code = input(">>> ")

        elif cmd == "neutron":
            try:
                exec(open("Neutron.py", encoding="utf-8").read())
            except:
                print(f"{Colors.WARNING}Neutron closed.{Colors.ENDC}")

        elif cmd == "launch" and len(parts) >= 2 and parts[1] == "app":
            launch_real_app()

        elif cmd == "startproc":
            proc_cmd = input("Enter command args separated by space: ").split()
            start_process(proc_cmd)

        elif cmd == "listprocs":
            show_fake_system_processes()

        elif cmd in ("exit", "quit"):
            save_processes()
            print(f"{Colors.HEADER}Exiting...{Colors.ENDC}")
            break

        else:
            print(f"{Colors.WARNING}Unknown command. Type 'help' for a list of commands.{Colors.ENDC}")

