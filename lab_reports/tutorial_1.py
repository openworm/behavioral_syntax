# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 16:57:12 2016

@author: aidanrocke
"""

from PIL import Image
import matplotlib.pyplot as plt
from io import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm

from reportlab.lib.utils import ImageReader

fig = plt.figure(figsize=(4, 3))
plt.plot([1,2,3,4])
plt.ylabel('some numbers')

imgdata = StringIO()
fig.savefig(imgdata, format='png')
imgdata.seek(0)  # rewind the data

Img = ImageReader(imgdata)

c = canvas.Canvas('test.pdf')
c.drawImage(Img, cm, cm, inch, inch)
c.save()