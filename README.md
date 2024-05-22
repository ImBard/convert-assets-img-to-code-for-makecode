## First create a virtual enviroment
Run on your terminal
```
python -3 -m venv venv
```
after run this code you need to activate the enviroment
```
cd venv/Scripts/
activate
```
then run 
```
cd ../..
pip install -r requirements.txt
```

## Adding a image to covert
1 - upload your image inside the directory "assets"
2 - modify the code passing the path of the image e.g "assets/myImage.png"
3 - inside your terminal with activated environment run the following code
```
py main.py
```
