# GUI Prototype for GenesisPy
# Nandi, 1064787

# Test version for the basic window layout
import os
import wx

name = 'GenesisPy_v0.0.1b' # GenesisPy version name

class Test_Frame(wx.Frame):
    def __init__(self, parent, title):
        super(Test_Frame, self).__init__(parent, title=name,
                                         size=(800,600))
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Test_Frame(None, name)
    app.MainLoop()
