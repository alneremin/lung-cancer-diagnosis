cd src
cd Window
rm authorizationWindow.py
rm mainWindow.py
pyuic5 ui/authorizationWindow.ui -o authorizationWindow.py
pyuic5 ui/mainWindow.ui -o mainWindow.py
cd ../
python3.7 start.py