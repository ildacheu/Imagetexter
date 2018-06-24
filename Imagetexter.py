from docx.shared import Pt
from docx import Document
from docx.shared import Inches
from PIL import Image

document = Document()

style = document.styles['Normal']
font = style.font
font.name = 'Courier New'
font.size = Pt(2)

textfile = open("text.txt", 'r')#this text will replace the image. No any space and not XML compatibel charakters. 

im = Image.open('image.jpg')

currentpara = ''
xpixel = 1
ypixel = 1

while ypixel < 190:#number of pixels of the image
    
    xpixel = 1
    while xpixel < 256:#number of pixels of the image       
        rgb_im = im.convert('RGB')
        r, g, b = rgb_im.getpixel((xpixel, ypixel))
        
        if r < 115:
            ran = textfile.read(1)           
            currentpara = currentpara + ran

        if r >= 115:
            currentpara = currentpara + ' '

        xpixel = xpixel + 1

    p = document.add_paragraph(currentpara)
    p.style = document.styles['Normal']
    currentpara = ''

    ypixel = ypixel + 1
       
document.add_page_break()

document.save('demo.docx')
textfile.close
