# Установка
## Windows
Запускаем **powershell** с правами администратора:

<img src="gifs/1.gif" width="500">

1. Устанавливаем chocolotey
```sh
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
2. Устанавливаем vscode 
```sh
choco install -y vscode
```
3. Устанавливаем python
```sh
choco install -y python
```
4. Устанавливаем telebot
```sh
pip install pyTelegramBotAPI --user
```
5. Устанавливаем requests
```sh
pip install requests --user
```
