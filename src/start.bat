cd window
del authorizationWindow.py
del mainWindow.py
pyuic5 authorizationWindow.ui -o authorizationWindow.py
pyuic5 mainWindow.ui -o mainWindow.py
cd ../
python start.py