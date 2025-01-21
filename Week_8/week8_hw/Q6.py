import tkinter
import tkinter.messagebox


total = 0.0  #ASSIGN GLOBAL CACHE VARIABLE

class Checkout:
   
    def __init__(self):
        # Create the main window widget.
        global total
    
        self.main_window = tkinter.Tk()

        # Create frames to group widgets.
        self.frame1 = tkinter.Frame()
        self.frame2 = tkinter.Frame()
        self.frame3 = tkinter.Frame()
        self.frame4 = tkinter.Frame()
        self.frame5 = tkinter.Frame()
        self.frame6 = tkinter.Frame()


        #create label
        self.menu_label = tkinter.Label(self.frame1, \
                                        text= "Joes's Automotive")
        #pack widget
        self.menu_label.pack()
        
        #create buttons
        self.oil_button = tkinter.Button(self.frame2, \
                                        text='Oil_Change', \
                                        command= self.add_oil)
        self.lube_button = tkinter.Button(self.frame2, \
                                        text='Lube Job', \
                                        command= self.add_lube)
        #pack buttons
        self.oil_button.pack(side='left')
        self.lube_button.pack(side='left')

        #create buttons        
        self.radiator_button = tkinter.Button(self.frame3, \
                                        text='Radiator flush', \
                                        command= self.add_radiator)
        self.transmission_button = tkinter.Button(self.frame3, \
                                        text='Transmission Flush', \
                                        command= self.add_transmission)
        #pack buttons
        self.radiator_button.pack(side='left')
        self.transmission_button.pack(side='left')
        
        #create buttons
        self.inspection_button = tkinter.Button(self.frame4, \
                                        text='Inspection', \
                                        command= self.add_inspection)
        
        self.muffler_button = tkinter.Button(self.frame4, \
                                        text='Muffler Replacement', \
                                        command= self.add_muffler)
        #pack buttons
        self.inspection_button.pack(side='left')
        self.muffler_button.pack(side='left')
        
        #create buttons
        self.tire_button = tkinter.Button(self.frame5, \
                                        text='Tire Rotation', \
                                        command= self.add_tire)
        
        self.total_button = tkinter.Button(self.frame5, \
                                        text='Total', \
                                        command= self.display_total)
        #pack buttons
        self.tire_button.pack(side='left')
        self.total_button.pack(side='left')
        
        #create quit button
        self.quit_button = tkinter.Button(self.frame6,
                                          text='Quit',
                                          command=self.main_window.destroy)
        #pack button
        self.quit_button.pack()
       

        # Pack the Button.
        # Pack the frames
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        
        # Enter the tkinter main loop.
        tkinter.mainloop()

    # Callback functions for the Buttons.
    
    def display_total(self):
        # Display an info dialog box.
        global total
        tkinter.messagebox.showinfo('Cart Total', \
                                    f'Total: {total}')

    
    def add_oil(self):
        global total
        total += 30.00
    
    def add_lube(self):
        global total
        total += 20.00
    
    def add_radiator(self):
        global total
        total += 40.00
    
    def add_transmission(self):
        global total
        total += 100.00

    def add_inspection(self):
        global total
        total += 35.00

    def add_muffler(self):
        global total
        total += 200.00
        
    def add_tire(self):
        global total
        total += 20.00
  
        
# Create an instance of the class.
if __name__ == '__main__':
    checkout = Checkout()
