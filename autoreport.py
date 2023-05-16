from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import Paragraph,SimpleDocTemplate,Table,TableStyle,Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.graphics.shapes import String

pdf = canvas.Canvas("rep2.pdf")
pdf.setPageSize((450,650)) 

from reportlab.graphics.charts.linecharts import(
    HorizontalLineChart
)
def getLineChart(emolst):
    dta = []
    for i in emolst:
        if i =="Happy":
            dta.append(1)
        if i =="Sad":
            dta.append(2)
        if i =="Surprised":
            dta.append(3)
        if i =="Neutral":
            dta.append(4)
        if i =="Angry":
            dta.append(5)
    data = [ tuple(dta)
    ]
    pdf.setFillColor(colors.black)
    pdf.setFont('Courier-BoldOblique', 12)
    pdf.drawCentredString(70, 380, "Happy")
    pdf.drawCentredString(70, 400, "Sad")
    pdf.drawCentredString(60, 420, "Surprised")
    pdf.drawCentredString(70, 440, "Neutral")
    pdf.drawCentredString(70, 460, "Angry")

    chart = HorizontalLineChart()
    chart.data = data
    chart.x = 5
    chart.y = 5
    chart.height = 100
    chart.width = 240
    chart.categoryAxis.categoryNames = [ f"{i+1}" for i in range(len(emolst))
    ]

    title = String(
        50, 110, 
        'Line Chart', 
        fontSize = 24
    )   

    chart.valueAxis.valueMin = 0
    chart.valueAxis.valueMax = 5
    chart.valueAxis.valueStep = 1

    chart.lines[0].strokeWidth = 3.5
    chart.lines[1].strokeWidth = 1
    chart.lines[0].strokeColor = colors.red

    drawing = Drawing(300, 150)
    drawing.add(title)
    drawing.add(chart)

    return drawing

from reportlab.graphics.charts.piecharts import (
    Pie
)
from reportlab.graphics.charts.legends import (
    Legend
)
from reportlab.lib.validators import Auto
def getPieChart(emlst):
    HE=0
    SAE =0
    SUE = 0
    NE = 0
    AE = 0
    for i in emlst:
        if i =="Happy":
            HE +=1
        if i =="Sad":
            SAE +=1
        if i =="Surprised":
            SUE +=1
        if i =="Neutral":
            NE +=1
        if i =="Angry":
            AE +=1
    
    data = [HE, SAE, SUE, NE,AE]

    chart = Pie()
    chart.data = data
    chart.x = 50
    chart.y = 5

    chart.labels = ['Happy','Sad','Surprised','Neutral', 'Angry']

    chart.sideLabels = True

    chart.slices[0].fillColor = colors.red
    chart.slices[0].popout = 8

    title = String(
        210, 110, 
        'Pie Chart', 
        fontSize = 24
    )   

    legend = Legend()
    legend.x = 150
    legend.y = 10
    #legend.alignment = 'left'  

    legend.colorNamePairs = Auto(obj=chart)

    drawing = Drawing(240, 120)
    drawing.add(title)
    drawing.add(chart)
    drawing.add(legend)

    return drawing


def content(em,usrnme):
    design()
    #drawMyRuler()
    emos = []
    ems = em
    for i in ems:
        if i==1:
            emos.append("Happy")
        if i==2:
            emos.append("Sad")
        if i==3:
            emos.append("Neutral")
        if i==4:
            emos.append("Angry")
        if i==5:
            emos.append("Surprised")
    width = 500
    height = 200
    title = '{}\'s Report'.format(usrnme)
    pdf.setFillColor(colors.blue)
    pdf.setFont('Courier-BoldOblique', 26)
    pdf.drawCentredString(220, 610, title)
    pdf.setFont('Courier', 15)
    pdf.setFillColor(colors.black)
    pdf.drawCentredString(220, 560, "Capturing emotions every 2 sec for 20 secs")
    pdf.setFillColor(colors.black)
    pdf.setFont('Courier', 11)
    prlst = [f"{i+1}: {emos[i]}" for i in range(len(emos))]
    pdf.drawCentredString(220, 520, ", ".join(prlst[:5]))
    pdf.drawCentredString(220, 500, ", ".join(prlst[5:]))

    pieChart = getPieChart(emos)
    lineChart = getLineChart(emos)
    graphs = Table([[lineChart],["\n\n\n\n\n"],[pieChart]])
    graphs.wrapOn(pdf, width, height)
    graphs.drawOn(pdf,100 , 150)
    pdf.save()


def design():
    pdf.setStrokeColor(colors.orange)
    pdf.setFillColor(colors.orange)
    pdf.rect(7,25,3,605,stroke=1,fill=1)
    pdf.setStrokeColor(colors.green)
    pdf.setFillColor(colors.green)
    pdf.rect(14,25,3,605,stroke=1,fill=1)

    pdf.setStrokeColor(colors.orange)
    pdf.setFillColor(colors.orange)
    pdf.rect(433,25,3,605,stroke=1,fill=1)
    pdf.setStrokeColor(colors.green)
    pdf.setFillColor(colors.green)
    pdf.rect(440,25,3,605,stroke=1,fill=1)

    pdf.setStrokeColor(colors.orange)
    pdf.setFillColor(colors.orange)
    pdf.rect(10,635,430,8,stroke=1,fill=1)
    pdf.setStrokeColor(colors.green)
    pdf.setFillColor(colors.green)
    pdf.rect(10,10,430,8,stroke=1,fill=1)



def drawMyRuler():
    pdf.drawString(100,640, 'x100')
    pdf.drawString(200,640, 'x200')
    pdf.drawString(300,640, 'x300')
    pdf.drawString(400,640, 'x400')
    pdf.drawString(500,640, 'x500')

    pdf.drawString(10,100, 'y100')
    pdf.drawString(10,200, 'y200')
    pdf.drawString(10,300, 'y300')
    pdf.drawString(10,400, 'y400')
    pdf.drawString(10,500, 'y500')
    pdf.drawString(10,600, 'y600')
    pdf.drawString(10,700, 'y700')
    pdf.drawString(10,800, 'y800')  


