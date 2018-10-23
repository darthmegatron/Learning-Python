import os
import subprocess

subprocess.call(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", '--new-window',
                 'https://support.zenimax.com', 'https://portal.infra.dfw', 'https://gateway.rds.dfw',
                 'http://zmi-master.signin.aws.amazon.com/console'])

subprocess.call(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", '--new-window', 'support.zenimax.com',
                 'bnet-confluence.zenimax.com'])

subprocess.call(['C:\Program Files\Oracle\VirtualBox\VBoxManage.exe', 'startvm', 'CentOS 7 for NOC'])

os.startfile('C:Users\Robert.Collins\AppData\Local\slack\slack.exe')
os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2016\Outlook 2016')
os.startfile('Spotify')
os.startfile('C:\Program Files (x86)\\Notepad++\\Notepad++.exe')
