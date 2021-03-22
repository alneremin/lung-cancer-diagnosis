cd Window
del authorizationWindow.py
del mainWindow.py
pyuic5 ui/authorizationWindow.ui -o authorizationWindow.py
pyuic5 ui/mainWindow.ui -o mainWindow.py
cd ../
python start.py
pause