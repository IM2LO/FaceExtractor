import config_manager

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

config = config_manager.read_config()

interval = int(config.get('interval', '10'))
margin = int(config.get('margin', '50'))
size = int(config.get('size', '512'))

print()
print()
print(f"{bcolors.CYAN}##################################")
print()
print(f"{bcolors.CYAN}{bcolors.BOLD}{bcolors.UNDERLINE}FACE EXTRACTOR v1.0{bcolors.END}")
print()
print(f"{bcolors.BLUE}RUNNING CONFIGURATION")
print("Capture every " + str(interval) + " frames.")
print(str(margin) + "px margin around faces.")
print("Outputting " + str(size) + "x" + str(size) + f"px sized images.{bcolors.END}")
print()
print(f"{bcolors.CYAN}##################################{bcolors.END}")
print()
print()