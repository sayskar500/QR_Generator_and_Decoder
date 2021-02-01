import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("My name is Sayantan Sarkar")
qr.png("myName.png", scale=8)

d = decode(Image.open("myName.png"))
print(d[0].data.decode("ascii"))