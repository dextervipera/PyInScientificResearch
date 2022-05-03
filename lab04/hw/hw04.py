# homework
# +-+ main script
# | |-- execute bmi-calc script with some args
# |
# +-+ calculator script
# | |-- argparses arguments
# | |-- calculates BMI
# | |-- displays full info or simplified info
# +-EOF
from pathlib import Path
import sys
import subprocess

def main():
    print('Main')
    sys.path.insert(0,str(Path.cwd().parent)+'.')
    subprocess.run(['python', 'bmicalc.py', '88.7','1.75', '-n', 'Agatka', '-d', 'full'])
    subprocess.run(['python', 'bmicalc.py', '45','1.45','-n','Jacek', '-d', 'full'])
    
if __name__ == "__main__":
    main()