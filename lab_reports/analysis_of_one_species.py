# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 10:35:12 2016

@author: aidanrocke
"""

from behavioral_syntax import lab_reports

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import date
from behavioral_syntax.visualization.view_postures import view_postures
from behavioral_syntax.visualization.posture_mds_view import mds_view

#data:
postures = '/Users/cyrilrocke/Documents/c_elegans/data/postures'


#image file paths:
gen = lab_reports.__file__

image_1 = gen[:-11]+ 'figures/postures.png'
image_2 = gen[:-11]+ 'figures/mds.png'

#import PIL
#from cStringIO import StringIO
#from reportlab.platypus.flowables import Image

today = date.today()

canvas = canvas.Canvas("bazooka370.pdf", pagesize=letter)
canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 20)
 
canvas.drawString(30,750,'Behavioral Syntax lab report:')
canvas.drawString(500,750,str(today.day)+'/'+str(today.month)+'/'+str(today.year))
canvas.line(480,747,580,747)
 
canvas.setFont('Courier', 15)
canvas.drawString(30,725,'number of teplate postures:')
canvas.drawString(500,725,"90")
#canvas.Canvas.drawImage('/Users/cyrilrocke/multimodal_angles.png')

#from behavioral_syntax.visualization.posture_mds_view import mds_view
#show distance between postures using MDS:
postures = '/Users/cyrilrocke/Documents/c_elegans/data/postures'


mds_view(postures)

#canvas.drawImage(file_path,x = 50, y = 50)

#'/Users/cyrilrocke/multimodal_angles.png'

#visualize k template postures:

view_postures(postures)
#mds_view(postures)

canvas.drawImage(image_1,x=30,y=200,width=400,preserveAspectRatio=True)

#visualize distance between postures:

#mds_view(postures)

canvas.drawImage(image_2,x=30,y=100,width=600,preserveAspectRatio=True)

#Image(PIL.Image.open('/Users/cyrilrocke/multimodal_angles.png'))

canvas.save()


#R2 info:



#look at n most common tri-grams:



#plot heat-map of posture probabilities:



#plot discovery rate:
