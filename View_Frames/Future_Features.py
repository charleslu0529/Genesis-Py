import os
import wx

class Msg_Feature_Frame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Msg_Feature_Frame, self).__init__(*args, **kwargs)

        self.InitUI()


    def InitUI(self):
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(2,2)

        message = wx.StaticText(panel, label="This feature will be implemented in future versions")
        sizer.Add(message, pos=(0,1), flag=wx.TOP|wx.CENTER, border=5)

        butt_ok = wx.Button(panel, label="OK", size=(90,28))
        sizer.Add(butt_ok, pos=(1,2), flag=wx.RIGHT|wx.BOTTOM, border=10)
        butt_ok.Bind(wx.EVT_BUTTON, self.on_quit)

        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(1)
        panel.SetSizer(sizer)


    def on_quit(self, e):
        self.Close()
