
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create three frames to group widgets.
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create a Button widget.
        self.sinister_button = tkinter.Button(self.top_frame, \
                                        text='Sinister', \
                                        command=self.show_sinister)
        
        self.dexter_button = tkinter.Button(self.mid_frame, \
                                        text='Dexter', \
                                        command=self.show_dexter)
        
        self.medium_button = tkinter.Button(self.bottom_frame,  \
                                        text='Medium', \
                                        command=self.show_medium)
        
      
        # Pack the Button.
        self.sinister_button.pack()
        self.dexter_button.pack()
        self.medium_button.pack()
        
        # Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
        # Enter the tkinter main loop.
        tkinter.mainloop()

    # Callback functions for the Button widget.
    
    def show_sinister(self):
        # Display an info dialog box.
        tkinter.messagebox.showinfo('English Translation', \
                                    'Left')
        
    def show_dexter(self):
        # Display an info dialog box.
        tkinter.messagebox.showinfo('English Translation', \
                                    'Right')
        
    def show_medium(self):
        # Display an info dialog box.
        tkinter.messagebox.showinfo('English Translation', \
                                    'Center')


# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()
