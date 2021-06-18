#! importing packages
from tkinter import *
from tkinter import ttk
import random
from package import bubble, selection, insertion, mergeSort, quick, shell, radix, cocktail, gnome, heap, bucket, bitonic, tim, bogo, comb

class App:
    def __init__(self):
        #! Initialization
        self.root = Tk()
        self.root.title("Sorting Visualizer")
        icon = PhotoImage(file = 'app/icon/sort_1.png')
        self.root.iconphoto(True, icon)
        self.w, self.h = 1200, 700
        self.posr = int(self.root.winfo_screenwidth()/2 - self.w/2)
        self.posd = int(self.root.winfo_screenheight()/2 - self.h/2)
        self.root.geometry("%dx%d+%d+%d" % (self.w, self.h, self.posr, self.posd))
        self.root.resizable(0,0)
        self.root.config(bg="Black") 
        self.root.bind("<Escape>", self.quit)
        
        #! All variables
        self.select_alg = StringVar() 
        self.data = [] 
        
        #! Title
        title = Label(self.root,text='Sorting Visualizer',bd=10,relief=GROOVE,font=('times new roman',20,'bold'),bg='Grey',fg='white')
        title.pack(side=TOP,fill=X)
        
        #! Manage Frame
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg='Grey')
        Manage_Frame.place(x=875,y=70,width=300,height=575)
        
        #! Canvas
        self.canvas = Canvas(self.root,bd=4,relief=RIDGE,bg='Grey')
        self.canvas.place(x=20,y=70,width=830,height=575)
        
        #! Label & Entry algo
        lblAlgo = Label(Manage_Frame, text="ALGORITHM: ", bg='Grey',fg="white",font=('times new roman',10,'bold')).place(x=5,y=20,width=125)
        
        #! Algorithm menu
        self.algmenu = ttk.Combobox(Manage_Frame, textvariable=self.select_alg, values=["Bubble Sort","Selection Sort","Insertion Sort","Merge Sort","Quick Sort","Shell Sort","Radix Sort","Cocktail Sort","Gnome Sort","Heap Sort","Bucket Sort","Bitonic Sort","Tim Sort","Comp sort","Bogo Sort"], state= 'readonly') 
        self.algmenu.place(x=130,y=20,width=125)
        self.algmenu.current(0) 
        
        #! Slidder Frame
        Slidder_Frame = Frame(Manage_Frame,bd=4,relief=GROOVE,bg='Grey')
        Slidder_Frame.place(x=5,y=60,width=280,height=330)
        
        #! Speed slidder
        self.speedbar = Scale(Slidder_Frame, from_=0, to=1.0, length=250, digits=2, resolution=0.1, orient=HORIZONTAL, label="Select Slowness") 
        self.speedbar.grid(row=0, column=0, padx=8, pady=11)
        
        #! Size slidder
        self.sizeEntry = Scale(Slidder_Frame, from_=5, to=100, length=250, resolution=1, orient=HORIZONTAL, label="Size") 
        self.sizeEntry.grid(row=1, column=0, padx=8, pady=11) 
        
        #! Minmum value slidder
        self.minEntry = Scale(Slidder_Frame, from_=1, to=10, length=250, resolution=1, orient=HORIZONTAL, label="Minimun Value") 
        self.minEntry.grid(row=2, column=0, padx=8, pady=11) 
        
        #! Maxmum value slidder
        self.maxEntry = Scale(Slidder_Frame, from_=10, to=200, length=250, resolution=1, orient=HORIZONTAL, label="Maximun Value") 
        self.maxEntry.grid(row=3, column=0, padx=8, pady=11) 
        
        #! Button Frame
        Button_Frame = Frame(Manage_Frame,bd=4,relief=GROOVE,bg='Grey')
        Button_Frame.place(x=5,y=400,width=280,height=145)
        
        #! Start button
        start_btn = Button(Button_Frame, text="Start", bg="Orange", width=33,command=self.start_sort).grid( row=0, column=0, padx=15, pady=10) #?, 
        
        #! Generate button
        self.generate()
        start_btn = Button(Button_Frame, text="Generate", bg="Orange", width=33, command=self.generate).grid( row=1, column=0, padx=15, pady=10) #?, command=start_algorithm
        
        #! Interupt button
        # interupt_btn = Button(Button_Frame, text="Interupt", bg="Orange", width=33, command=self.interupt).grid( row=2, column=0, padx=15, pady=10) #?
        
        #! Info Keys log
        self.lblInstruction = Label(self.root,text="F11 - Toggle Fullscreen , Escape - Quit",bg="Grey",fg="white",font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        self.lblInstruction.pack(side=BOTTOM,fill=X)
        
        #! Mainloop
        self.root.mainloop() 
        
    #! Quit program
    def quit(self, event):
        self.root.quit()
        
    #! Generating random array
    def generate(self):
        minval = int(self.minEntry.get())
        maxval = int(self.maxEntry.get()) 
        sizeval = int(self.sizeEntry.get()) 
        self.data = [] 
        for _ in range(sizeval):
            self.data.append(random.randrange(minval, maxval+1)) 
        self.drawData(self.data, ['Red' for x in range(len(self.data))]) 
        
    #! Draw bar graph
    def drawData(self,data,colourlist):
        self.canvas.delete("all")
        # TODO adjest
        can_height = 575
        can_width = 800
        x_width = can_width/(len(self.data)+1)
        offset = 15
        spacing = 10
        
        normalize_data = [i/max(self.data) for i in self.data]
        
        for i, height in enumerate(normalize_data):
            # top left corner 
            x0 = i*x_width + offset + spacing 
            y0 = can_height - height*500

            # bottom right corner 
            x1 = ((i+1)*x_width) + offset 
            y1 = can_height 

            # data bars are generated as Red colored vertical rectangles 
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=colourlist[i]) 
            self.canvas.create_text(x0+2, y0, anchor=SE, text=str(self.data[i])) 
        self.root.update_idletasks() 
        
    #! Select & Start sorting
    # TODO sort arrange
    def start_sort(self):
        if self.algmenu.get() == "Selection Sort":
            selection(self.data, self.drawData, self.speedbar.get())
        elif self.algmenu.get() == "Insertion Sort":
            insertion(self.data, self.drawData, self.speedbar.get())
        elif self.algmenu.get() == "Merge Sort":
            mergeSort(self.data, self.drawData, self.speedbar.get(),0,self.sizeEntry.get()-1)
        elif self.algmenu.get() == "Quick Sort":
            quick(self.data, self.drawData, self.speedbar.get(),0,self.sizeEntry.get()-1)
        elif self.algmenu.get() == "Shell Sort":
            shell(self.data, self.drawData, self.speedbar.get())
        elif self.algmenu.get() == "Radix Sort":
            radix(self.data, self.drawData, self.speedbar.get())
        elif self.algmenu.get() == "Cocktail Sort":
            cocktail(self.data, self.drawData, self.speedbar.get())
        elif self.algmenu.get() == "Gnome Sort":
            gnome(self.data, self.drawData, self.speedbar.get())
        elif self.algmenu.get() == "Heap Sort":
            heap(self.data, self.drawData, self.speedbar.get()) 
        elif self.algmenu.get() == "Bucket Sort":
            bucket(self.data, self.drawData, self.speedbar.get())
        elif self.algmenu.get() == "Bitonic Sort":
            bitonic(self.data, self.drawData, self.speedbar.get())
        elif self.algmenu.get() == "Tim Sort":
            tim(self.data, self.drawData, self.speedbar.get()) 
        elif self.algmenu.get() == "Comb Sort":
            comb(self.data, self.drawData, self.speedbar.get()) 
        elif self.algmenu.get() == "Bogo Sort":
            bogo(self.data, self.drawData, self.speedbar.get())
        else:
            bubble(self.data, self.drawData, self.speedbar.get())
    
if __name__ == '__main__':
    app = App()  
