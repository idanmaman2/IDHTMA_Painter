import kivy  # Required to run Kivy such as the next line of code
kivy.require('1.9.1')  # used to alert user if this code is run on an earlier version of Kivy.
from kivy.app import App  # Imports the base App class required for Kivy Apps
from kivy.lang import Builder  # Imports the KV language builder that provides the layout of kivy screens
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout  import FloatLayout
from kivy.uix.stacklayout  import StackLayout
from kivy.uix.screenmanager import ScreenManager, Screen  # Imports the Kivy Screen manager and Kivys Screen class
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.properties import StringProperty
import time
import math
from kivy.graphics import Rectangle, Color 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Line
from functools import partial
from kivy.core.window import Window
import csv
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
lastpoint=(0,0)
from kivy.base import runTouchApp
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory



from kivy.uix.label import Label
Factory.unregister('ActionPrevious')
name=""
hello=True
arrlen=[]
check=True

Builder.load_string("""

<Touch>:
    #btn: btn

        
    canvas:
        Color:
            rgba:1.0,0.0,0.0,0.0
            
        Rectangle:
            pos: self.pos
            size: self.size
        
    #BoxLayout:
        #col:3 
        #Button:
            #id:btn
            #text: "delete all the draws"
            #color:[1, 0, 0, 1]
        
            #on_press:root.configo()
            #size_hint:0.20,0.20
    


        #Button:
        
            #id:save_last
            #text:"save"
            #size_hint:0.20,0.20
            #color:[12,23,1,1]
            #on_press:root.save()
        #Button:
        
            #id:reload
            #text:"reload"
            #size_hint:0.20,0.20
            #color:[12,23,1,1]
            #on_press:root.reload()
    ActionBar:
        orientation: 'horizontal'
        size_hint:1,0.1
        pos_hint: {'top':1}
        background_color:[0.3,0,255,0.5]
        ActionView:
            use_separator: False
            ActionPrevious:
                title: ''
                app_icon:"idhmtalogo.png"
                color:[255,204,255,1]
                with_previous: False 
            ActionOverflow:

            ActionGroup:
                dropdown_width: 300
                text: 'Operations'
                font_size:'13sp'
                color:[0,0,0,1]
                ActionButton:
                    text: 'delete'
                    background_color:[0,213,255,0.5]
                    on_press:root.configo()
                    color:[1,0,0,1]
                
                ActionButton:
                    text: 'reload'
                    on_press:root.reload()
                    color:[255,248,26,1]
                    background_color:[0,213,255,0.5]
                ActionButton:
                    text: 'save'
                    on_press:root.save()
                    color:[255,248,26,1]
                    background_color:[0,213,255,0.50]
       
            ActionGroup:
                dropdown_width: 300
                text: 'Brush sizes '
                font_size:'13sp'
                color:[0,0,0,1]
          
                ActionButton:
                    text: 'S'
                    background_color:[0,120,0.120,0.5]
                    on_press:root.brushsmall()
                    color:[1,0,0,1]
                ActionButton:
                    text: 'M'
                    background_color:[0,120,0.120,0.5]
                    on_press:root.brushmedium()
                    color:[1,0,0,1]
                ActionButton:
                    text: 'L'
                    background_color:[0,120,0.120,0.5]
                    on_press:root.brushlarge()
                    color:[1,0,0,1]
                ActionButton:
                    text: 'XL'
                    background_color:[0,120,0.120,0.5]
                    on_press:root.brushextra()
                    color:[1,0,0,1]
                ActionButton:
                    text: 'XXXL'
                    background_color:[0,120,0.120,0.5]
                    on_press:root.brushextratwice() 
                    color:[1,0,0,1]

                
                     
            ActionGroup:
                dropdown_width: 300
                text: 'Brush type'
                font_size:'13sp'
                color:[0,0,0,1]
                ActionButton:
                    text: 'pen'
                    background_color:[150,150,0,0.5]
                    on_press:root.brushpen()
                    color:[1,0,0,1]
                ActionButton:
                    text: 'Marker'
                    background_color:[150,150,0,0.5]
                    on_press:root.brushmarker()
                    color:[1,0,0,1]

                   
            ActionGroup:
                dropdown_width: 300
                text: 'Brush color'
                font_size:'13sp'
                color:[0,0,0,1]
                ActionButton:
                    text: 'white'
                    background_color:[0,0.5,0.6,0.5]
                    on_press:root.brushwhite()
                    color:[1,0,0,1]
                ActionButton:
                    text: 'red'
                    background_color:[0,0.5,0.6,0.5]
                    on_press:root.brushred()
                    color:[1,0,0,1]
                ActionButton:
                    text: 'brigth blue'
                    background_color:[0,0.5,0.6,0.5]
                    on_press:root.brushbrightblue()
                    color:[1,0,0,1]
                ActionButton:
                    text: 'green'
                    background_color:[0,0.5,0.6,0.5]
                    on_press:root.brushgreen()
                    color:[1,0,0,1]
                ActionButton:
                    text: 'black'
                    background_color:[0,0.5,0.6,0.5]
                    on_press:root.brushblack() 
                    color:[1,0,0,1]
                ActionButton:
                    text: 'shosh lihot dos '
                    background_color:[0,0.5,0.6,0.5]
                    on_press:root.brushpro() 
                    color:[1,0,0,1]
                
                
  

            
<Save>:
    input:input  
    Label:
        text:"save"
        color:1,0,0,1
        pos_hint: {'center_x': 0.1, 'center_y': 0.8} 

        size_hint: 0.5, 0.1
        font:42
    

    RelativeLayout:
        

        orientation: 'vertical'

        pos: self.pos 

        size: root.size 

        id: test2 

  

        # Defining text input in .kv 

        # And giving it the look . pos and features 

        TextInput: 

            id: input1

            hint_text:'Enter text'

            pos_hint: {'center_x': 1, 'center_y':1.3} 

            size_hint: 0.6, 0.2

            on_text: root.getSave()
        Button:
        
            id:Save 
            text:"Save"
            size_hint:0.20,0.20
            pos_hint: {'center_x': 1, 'center_y':0.96} 
            color:[12,23,1,1]
            on_press:root.check1()
<Mainscreen>
    canvas.before:
        Color:
            rgb: .280,.18888,.95
        Rectangle:
            pos: self.pos
            size: self.size
    Image:
        source: 'logoidhmta1.png'
        size: self.texture_size


""")

class Save(App):
    input1= ObjectProperty(None)
    def getSave(self):
       global name
       #print(self.input1.text)
    def check1 (self ):
        global check
        check =False 
    pass

class Mainscreen(App,FloatLayout):
    def build(self):
        return self;



    
def calc(height,width,point):
    x=point[0]
    y=point[1]
    s1=abs(width*y)/2
    s2=abs(x*height)/2
    s3=abs((y-height)*width)/2
    s4=abs((x-width)*height)/2 
    sT=height*width

    if(sT==(s1+s2+s3+s4)):
        return False  
    return True
class Touch(FloatLayout ):


    #btn = ObjectProperty(None)
    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.brushsize = 3
        self.brushcolor= [0,0,0]
        
        Window.clearcolor = (1, 1, 1, 1)
        self.brushopacity=1
        pass
    def brushsmall(self):
        self.brushsize=0.5
    def brushmedium(self):
        self.brushsize=1.5
    def brushlarge(self):
        self.brushsize=3
    def brushextra(self):
        self.brushsize=7 
        
    def brushextratwice(self):
        self.brushsize=22
    def brushgreen(self):
        self.brushcolor=[150,150,0]
    def brushpro(self):
        self.brushcolor=[0,0,0]
    def brushred(self):
        self.brushcolor=[1000,0,0]
    def brushwhite(self):
        self.brushcolor=[0.9875*1000, 0.97*1000, 1.9575*1000]
    def brushblack(self):
        self.brushcolor=[255,0,0]
    def brushbrightblue(self):
        self.brushcolor=[701.25,831.666,1531]
    def brushmarker(self):
        self.brushopacity=0.4
    def brushpen(self):
        self.brushopacity=1
    def configo(self):
        #print("delte all ")
        global arrlen
        global check
        
        self.canvas.remove_group("idm")
        arrlen=[]

    def save(self):
        global check
        global name

        '''
        show = Save()

        popupWindow = Popup(title="Popup Window", content=show, size_hint=(0.5,0.5))

        popupWindow.open()
        '''
        global arrlen
        
            
        ##print(arrlen)
            
        ##print(name )
            #((val1,val2),(val3,val4))
       
        with open('C:\\Users\\idang\\Desktop\\id.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                        quotechar=' ', quoting=csv.QUOTE_MINIMAL)
            for i in range(len (arrlen)):
                temp=arrlen[i]
                temp=list(temp)
               
                

                spamwriter.writerow([temp[0][0],temp[0][1],temp[1][0],temp[1][1]])
          
        
        
  
 
    def reload(self):
        
        temp=[]
        global arrlen 
        with open('C:\\Users\\idang\\Desktop\\id.csv', newline='') as csvfile:
             spamreader = csv.reader(csvfile, delimiter=',', quotechar=' ')
             for row in spamreader:
                temp.append(row)
             
       
        for i in range (len(temp)):
            with self.canvas:
                Color(1,0,0,1)

                Line(points=(float(temp[i][0]),float(temp[i][1]),float(temp[i][2]),float(temp[i][3])), width=1.5 ,group=("idm"))
                tmp=((float(temp[i][0]),float(temp[i][1])),(float(temp[i][2]),float(temp[i][3])))
                ##print("tmp:  ",tmp)
            
        # Seting the size and position of canvas
                arrlen.append(tmp)
        
               #fix the bug !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        

                #temp contain all the point each index contain arr wich this arr contain 2 points(x,y) of where are the firsf layout line 

           
    def on_touch_down(self, touch):
        global lastpoint
        global arrlen
        global check
        lastpoint=(0,0)


        
    
        return super(Touch ,self).on_touch_down(touch)
  
    def on_touch_move(self, touch):
        global lastpoint
        global arrlen
        global check
        
        #print((touch.pos))
       # and(calc((self.btn.height),(self.btn.width+self.ids.save_last.width)*8,(touch.pos))) and (calc((self.btn.height),(self.btn.width+self.ids.save_last.width)*8,(lastpoint))))
        if( (not(lastpoint == (0,0) ))):
            with self.canvas:
                if(self.brushcolor[0]==0 and self.brushcolor[1]==0 and self.brushcolor[2]==0  ):
                    Color(touch.spos[0],touch.spos[1], touch.spos[0]+touch.spos[1], self.brushopacity)
                     #the colour  
                else:
                    Color(self.brushcolor[0]*0.001,self.brushcolor[1]*0.01,self.brushcolor[2]*0.001,self.brushopacity)
                    
                # Seting the size and position of canvas
                
                Line(points=(touch.pos,lastpoint), width=self.brushsize ,group=("idm"))
               
            arrlen.append((touch.pos,lastpoint))
        lastpoint=touch.pos
        
        return super(Touch, self).on_touch_move(touch)      
    def printus(self,*args):
        ##print(Window.size)
        global hello
        if(hello):

                  # set the colour  
                  
                # Seting the size and position of canvas
                  
                    #(x,(,x+0.1,((4-((x+0.1-2)**2))**0.5))
                   
            hello=False

        pass

    def on_touch_up(self, touch):
       
        #self.btn.opacity = 1
  
        pass
class idans_painter_Alpah(App):

    def build(self):
        a=Touch()
            
        
        Clock.schedule_interval(a.printus, 1/2)
        return a;




class MainWindow(FloatLayout):
    pass


if __name__ == "__main__":
    
 
    idans_painter_Alpah().run()
    
    #Mainscreen().run()
