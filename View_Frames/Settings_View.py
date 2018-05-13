import os
import wx

class Settings_View(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Settings_View, self).__init__(*args, **kwargs)

        self.Show_Frame()

    def Show_Frame(self):
        self.SetSize((400,300))
        self.SetTitle('Settings')
        self.Centre()


    ###Panel###
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5, 4)

        butt_col_opt = wx.Button(panel, label="Colour Options") # button for colour options
        sizer.Add(butt_col_opt, pos=(0,0), flag=wx.LEFT, border=10)
        #butt_col_opt.Bind(wx.EVT_BUTTON, self.)
