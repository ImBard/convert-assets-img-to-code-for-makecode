## First create a virtual environment
Run in your terminal
```
python -3 -m venv venv
```
After running this code, you need to activate the environment
```
cd venv/Scripts/
activate
```
Then run 
```
cd ../..
pip install -r requirements.txt
```

## Adding a image to covert
1 - Upload your image inside the directory "assets";
2 - Modify the code passing the path of the image e.g "assets/myImage.png";
3 - Inside your terminal with activated environment run the following code.
```
py main.py
```
