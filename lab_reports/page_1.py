# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 22:10:58 2015

@author: aidanrocke
"""
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import date
#import PIL
#from cStringIO import StringIO
#from reportlab.platypus.flowables import Image

today = date.today()
 
canvas = canvas.Canvas("bazinga4.pdf", pagesize=letter)
canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 12)
 
canvas.drawString(30,750,'Behavioral Syntax lab report:')
canvas.drawString(500,750,str(today.day)+'/'+str(today.month)+'/'+str(today.year))
canvas.line(480,747,580,747)
 
canvas.drawString(275,725,'number of teplate postures:')
canvas.drawString(500,725,"90")
#canvas.Canvas.drawImage('/Users/cyrilrocke/multimodal_angles.png')


canvas.drawImage('/Users/cyrilrocke/multimodal_angles.png',x=100,y=100,width=200,preserveAspectRatio=True)

#Image(PIL.Image.open('/Users/cyrilrocke/multimodal_angles.png'))

canvas.save()