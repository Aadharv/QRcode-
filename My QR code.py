from re import S
from tkinter import Scale
import pyqrcode
from pyqrcode import QRCode

import png

s="www.amazon.in"

a=pyqrcode.create(s)
a.svg('MyQRcode.svg',scale=8)
a.png('MyQRcode.png',scale=8)

d="www.google.com"

w=pyqrcode.create(d)
w.svg("Google.svg",scale=8)
w.png("Google.png",scale=8)