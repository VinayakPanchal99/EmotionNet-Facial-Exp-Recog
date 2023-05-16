from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import Paragraph,SimpleDocTemplate,Table,TableStyle,Image
from reportlab.lib.styles import getSampleStyleSheet
import random
import allcode

class Report:
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.pdf=canvas.Canvas("USERS_REPORT.pdf")
        self.pdf.setPageSize((450,650)) 
        self.content()
        #self.drawMyRuler(self.pdf)
        self.numbers = [1,2,3,4]
    
    def content(self,*args):
        self.title = "\'s Report"
        self.image = 'pic.png'   
        #links 1)happy 2)sugar 3)lazzy song 4)DESPACITO 5)KOLAVERI 
        self.linkslist = ['link:https://youtu.be/y6Sxv-sUYtM','link:https://youtu.be/09R8_2nJtjg','link:https://youtu.be/fLexgOxsZu0','link:https://youtu.be/kJQP7kiw5Fk','link:https://youtu.be/YR12Z8f1Dh8'] 
        # 5 contents
        self.contentlist =['Fact: \n McDonald’s once made bubblegum-flavored \n broccoli', 'Fact:\n Some fungi create zombies, then control \nant\'s mind', 'Fact:\n Samsung tests phone durability with a \n butt-shaped robot', 'Fact: \n Climate change is causing flowers to \n change color.', 'Fact: \n The entire world\'s population could fit \n inside Los Angeles.']
        # quotelist for happy and neutral(4 contents)
        self.quote1list = ['Quote: \n Your limitation-its only your imagination.','Quote: \n Great things never come from comfort zones.','Quote: \n The harder you work for something, the \n greater you will feel when you achieve it.','Quote: \n The more you praise and celebrate your life, \n the more there is in life to celebrate.']
        # quotelist for sad(6 contents)
        self.quote2list = ['Quote:\n A good laugh heals a lot of hurts.','Quote:\n A smile is a curve that sets everything \n straight','Quote:\n In my eyes, of course,\n I think I am the best in the world','Quote:\nBreathe, it is just a bad day not bad life','Quote:\n Count your age by friends, not years. \n Count your life by smiles, not tears.','Quote: \n The more you praise and celebrate your life, \n the more there is in life to celebrate.']
        #quotelist for angry(3 contents)
        self.quote3list = ['Quote:\n For every minute you are angry you lose sixty\n  seconds of happiness.','Quote:\nThe more you praise and celebrate your life,\n the more there is in life to celebrate.','Quote:\nDo not be angry with the people who does not \n have capacity to change.']
        #jokelist (5 contents)
        self.jokelist = ['Joke:\n Laughter is a medicine. But if you are \n laughing without  any reason then you need a \n medicine HaHaHaHa!!!','Joke: \n Question: What did the traffic light say \n to the car?, Answer: Do not look! I am about \n to change.','Joke:\n Laugh at your problems, everybody else does.','Joke:\nIf you think nobody cares if you are alive,\n try missing a couple of payments.','Joke:  Money talks \n …but all mine ever says is good-bye.']
        #happy intro
        self.happy_intro = [['Hey! \n Cheering all day my friend!! \n Always be happy as you are now, \n We have something interesting for you']]
        #sad intro
        self.sad_intro = [['Hey! \n Seems to be sad with someting or someone \n We have something interesting for you']]
        #neutral intro
        self.neutral_intro = [['Hey! \n Your expression was expressionless \n We have something interesting for you']]
        #angry intro
        self.angry_intro = [['Hey! \n Calm down... Seems that being angry with \n someone or something is not working out for \n you. We have something interesting for you']]
        #surprise intro
        self.surp_intro = [['Hey! \n Your look Surprised! \n We have something interesting for you']]

    def mainpage(self,select, usrnme):
        self.title = usrnme + self.title
        self.select = select
        self.width = 800
        self.height = 200
        self.design()
        self.pdf.setFillColor(colors.blue)
        self.pdf.setFont('Courier-BoldOblique', 26)
        self.pdf.drawCentredString(220, 610, self.title)
        self.pdf.setStrokeColor(colors.black)
        self.pdf.line(40, 760, 550, 760)
        self.pdf.drawInlineImage(self.image, 250, 420, width=140, height=180)
        self.pdf.setFillColor(colors.black)
        self.pdf.setFont('Times-Roman', 20)
        self.pdf.drawCentredString(120, 500, 'Detected Emotion:')
        

        if self.select == 1:
            self.select = 0 
            #happy
            self.pdf.drawCentredString(110, 450, "HAPPY")
            self.happy_facts = [[self.contentlist[random.randrange(0,4)]]]
            self.happy_link= [[self.linkslist[random.randrange(0,4)]]]
            self.happy_jokes = [[self.jokelist[random.randrange(0,4)]]]
            self.happy_neutral_quote = [[self.quote1list[random.randrange(0,3)]]]
            self.happy_st = Table(self.happy_intro)
            self.happy_st.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.orange),
                ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14),
                ('TOPPADDING',(0,0),(0,0),10),
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.happy_st.wrapOn(self.pdf, self.width, self.height)
            self.happy_st.drawOn(self.pdf,40 , 330)
            
            self.happy_ct = Table(self.happy_facts)
            self.happy_ct.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.yellow), ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14), ('TOPPADDING',(0,0),(0,0),10),
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.happy_ct.wrapOn(self.pdf, self.width, self.height)
            self.happy_ct.drawOn(self.pdf,25 , 250)

            self.happy_qt = Table(self.happy_neutral_quote )
            self.happy_qt.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.lightgreen),
                ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14), ('TOPPADDING',(0,0),(0,0),10),
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.happy_qt.wrapOn(self.pdf, self.width, self.height)
            self.happy_qt.drawOn(self.pdf,25, 170)

            self.happy_jks = Table(self.happy_jokes)
            self.happy_jks.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.lightblue),
                ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14), ('TOPPADDING',(0,0),(0,0),10),
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.happy_jks.wrapOn(self.pdf, self.width, self.height)
            self.happy_jks.drawOn(self.pdf,25 , 80)

            self.happy_lnk = Table(self.happy_link)
            self.happy_lnk.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.pink),
                ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14), 
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.happy_lnk.wrapOn(self.pdf, self.width, self.height)
            self.happy_lnk.drawOn(self.pdf,50 , 30)

        if self.select == 2:
            self.select = 0 
            #sad
            self.pdf.drawCentredString(110, 450, "SAD")
            self.sad_facts = [[self.contentlist[random.randrange(0,4)]]]
            self.sad_link= [[self.linkslist[random.randrange(0,4)]]]
            self.sad_jokes = [[self.jokelist[random.randrange(0,4)]]]
            self.sad_quote = [[self.quote2list[random.randrange(0,5)]]]
            self.sad_st = Table(self.sad_intro)
            self.sad_st.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.orange),
                ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14),
                ('TOPPADDING',(0,0),(0,0),10),
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.sad_st.wrapOn(self.pdf, self.width, self.height)
            self.sad_st.drawOn(self.pdf,40 , 330)
            
            self.sad_ct = Table(self.sad_facts)
            self.sad_ct.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.yellow), ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14), ('TOPPADDING',(0,0),(0,0),10),
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.sad_ct.wrapOn(self.pdf, self.width, self.height)
            self.sad_ct.drawOn(self.pdf,25 , 250)

            self.sad_qt = Table(self.sad_quote )
            self.sad_qt.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.lightgreen),
                ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14), ('TOPPADDING',(0,0),(0,0),10),
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.sad_qt.wrapOn(self.pdf, self.width, self.height)
            self.sad_qt.drawOn(self.pdf,25, 170)

            self.sad_jks = Table(self.sad_jokes)
            self.sad_jks.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.lightblue),
                ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14), ('TOPPADDING',(0,0),(0,0),10),
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.sad_jks.wrapOn(self.pdf, self.width, self.height)
            self.sad_jks.drawOn(self.pdf,25 , 80)

            self.sad_lnk = Table(self.sad_link)
            self.sad_lnk.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.pink),
                ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14), 
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.sad_lnk.wrapOn(self.pdf, self.width, self.height)
            self.sad_lnk.drawOn(self.pdf,50 , 30)

        if self.select == 3:
            self.select = 0 
            #neutral
            self.pdf.drawCentredString(110, 450, "NEUTRAL")
            self.neutral_facts = [[self.contentlist[random.randrange(0,4)]]]
            self.neutral_link= [[self.linkslist[random.randrange(0,4)]]]
            self.neutral_jokes = [[self.jokelist[random.randrange(0,4)]]]
            self.happy_neutral_quote = [[self.quote1list[random.randrange(0,3)]]]
            self.neutral_st = Table(self.neutral_intro)
            self.neutral_st.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.orange),
                ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14),
                ('TOPPADDING',(0,0),(0,0),10),
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.neutral_st.wrapOn(self.pdf, self.width, self.height)
            self.neutral_st.drawOn(self.pdf,40 , 330)
            
            self.neutral_ct = Table(self.neutral_facts)
            self.neutral_ct.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.yellow), ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14), ('TOPPADDING',(0,0),(0,0),10),
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.neutral_ct.wrapOn(self.pdf, self.width, self.height)
            self.neutral_ct.drawOn(self.pdf,25 , 250)

            self.neutral_qt = Table(self.happy_neutral_quote )
            self.neutral_qt.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.lightgreen),
                ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14), ('TOPPADDING',(0,0),(0,0),10),
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.neutral_qt.wrapOn(self.pdf, self.width, self.height)
            self.neutral_qt.drawOn(self.pdf,25, 170)

            self.neutral_jks = Table(self.neutral_jokes)
            self.neutral_jks.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.lightblue),
                ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14), ('TOPPADDING',(0,0),(0,0),10),
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.neutral_jks.wrapOn(self.pdf, self.width, self.height)
            self.neutral_jks.drawOn(self.pdf,25 , 80)

            self.neutral_lnk = Table(self.neutral_link)
            self.neutral_lnk.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.pink),
                ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14), 
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.neutral_lnk.wrapOn(self.pdf, self.width, self.height)
            self.neutral_lnk.drawOn(self.pdf,50 , 30)

        if self.select == 4:
            self.select = 0 
            #angry
            self.pdf.drawCentredString(110, 450, "ANGRY")
            self.angry_facts1 = [[self.contentlist[random.randrange(0,4)]]]
            self.angry_link= [[self.linkslist[random.randrange(0,4)]]]
            self.angry_jokes = [[self.jokelist[random.randrange(0,4)]]]
            self.angry_quote = [[self.quote3list[random.randrange(0,2)]]]
            self.angry_st = Table(self.angry_intro)
            self.angry_st.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.orange),
                ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14),
                ('TOPPADDING',(0,0),(0,0),10),
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.angry_st.wrapOn(self.pdf, self.width, self.height)
            self.angry_st.drawOn(self.pdf,40 , 330)
            
            self.angry_ct = Table(self.angry_facts)
            self.angry_ct.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.yellow), ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14), ('TOPPADDING',(0,0),(0,0),10),
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.angry_ct.wrapOn(self.pdf, self.width, self.height)
            self.angry_ct.drawOn(self.pdf,25 , 250)

            self.angry_qt = Table(self.angry_quote )
            self.angry_qt.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.lightgreen),
                ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14), ('TOPPADDING',(0,0),(0,0),10),
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.angry_qt.wrapOn(self.pdf, self.width, self.height)
            self.angry_qt.drawOn(self.pdf,25, 170)

            self.angry_jks = Table(self.angry_jokes)
            self.angry_jks.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.lightblue),
                ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14), ('TOPPADDING',(0,0),(0,0),10),
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.angry_jks.wrapOn(self.pdf, self.width, self.height)
            self.angry_jks.drawOn(self.pdf,25 , 80)

            self.angry_lnk = Table(self.angry_link)
            self.angry_lnk.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.pink),
                ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14), 
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.angry_lnk.wrapOn(self.pdf, self.width, self.height)
            self.angry_lnk.drawOn(self.pdf,50 , 30)        

        if self.select == 5:
            self.select = 0 
            #surprised
            self.pdf.drawCentredString(110, 450, "SURPRISED")
            self.surp_facts1 = [[self.contentlist[random.randrange(0,2)]]]
            self.surp_link= [[self.linkslist[random.randrange(0,4)]]]
            self.surp_jokes = [[self.jokelist[random.randrange(0,4)]]]
            self.surp_facts2 = [[self.contentlist[random.randrange(3,4)]]]
            self.surp_st = Table(self.surp_intro)
            self.surp_st.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.orange),
                ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14),
                ('TOPPADDING',(0,0),(0,0),10),
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.surp_st.wrapOn(self.pdf, self.width, self.height)
            self.surp_st.drawOn(self.pdf,40 , 330)
            
            self.surp_ct = Table(self.surp_facts1)
            self.surp_ct.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.yellow), ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14), ('TOPPADDING',(0,0),(0,0),10),
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.surp_ct.wrapOn(self.pdf, self.width, self.height)
            self.surp_ct.drawOn(self.pdf,25 , 250)

            self.surp_qt = Table(self.surp_facts2 )
            self.surp_qt.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.lightgreen),
                ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14), ('TOPPADDING',(0,0),(0,0),10),
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.surp_qt.wrapOn(self.pdf, self.width, self.height)
            self.surp_qt.drawOn(self.pdf,25, 80)

            self.surp_jks = Table(self.surp_jokes)
            self.surp_jks.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.lightblue),
                ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14), ('TOPPADDING',(0,0),(0,0),10),
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.surp_jks.wrapOn(self.pdf, self.width, self.height)
            self.surp_jks.drawOn(self.pdf,25 , 170)

            self.surp_lnk = Table(self.surp_link)
            self.surp_lnk.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.pink),
                ("ALIGN",(0,0),(0,0),"CENTER"),
                ('FONTNAME', (0,0),(0,0),'Courier'),
                ('FONTSIZE',(0,0),(0,0),14), 
                ('BOTTOMPADDING',(0,0),(0,0),20)]))
            self.surp_lnk.wrapOn(self.pdf, self.width, self.height)
            self.surp_lnk.drawOn(self.pdf,50 , 30)  

        self.pdf.save()



    def design(self,*args):
        self.pdf.setStrokeColor(colors.orange)
        self.pdf.setFillColor(colors.orange)
        self.pdf.rect(7,25,3,605,stroke=1,fill=1)
        self.pdf.setStrokeColor(colors.green)
        self.pdf.setFillColor(colors.green)
        self.pdf.rect(14,25,3,605,stroke=1,fill=1)

        self.pdf.setStrokeColor(colors.orange)
        self.pdf.setFillColor(colors.orange)
        self.pdf.rect(433,25,3,605,stroke=1,fill=1)
        self.pdf.setStrokeColor(colors.green)
        self.pdf.setFillColor(colors.green)
        self.pdf.rect(440,25,3,605,stroke=1,fill=1)

        self.pdf.setStrokeColor(colors.orange)
        self.pdf.setFillColor(colors.orange)
        self.pdf.rect(10,635,430,8,stroke=1,fill=1)
        self.pdf.setStrokeColor(colors.green)
        self.pdf.setFillColor(colors.green)
        self.pdf.rect(10,10,430,8,stroke=1,fill=1)



    def drawMyRuler(self,*args):
        self.pdf.drawString(100,640, 'x100')
        self.pdf.drawString(200,640, 'x200')
        self.pdf.drawString(300,640, 'x300')
        self.pdf.drawString(400,640, 'x400')
        self.pdf.drawString(500,640, 'x500')

        self.pdf.drawString(10,100, 'y100')
        self.pdf.drawString(10,200, 'y200')
        self.pdf.drawString(10,300, 'y300')
        self.pdf.drawString(10,400, 'y400')
        self.pdf.drawString(10,500, 'y500')
        self.pdf.drawString(10,600, 'y600')
        self.pdf.drawString(10,700, 'y700')
        self.pdf.drawString(10,800, 'y800')  










