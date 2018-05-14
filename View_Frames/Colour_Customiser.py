import wx

class Customise_Colour_Frame(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Customise_Colour_Frame, self).__init__(*args, **kwargs)

        self.type_of_graph = ""
        self.label = ""
        self.panel = None
        self.sizer = None

        self.Center()

        self.InitUI()

    def InitUI(self):
        self.panel = wx.Panel(self)
        self.sizer = wx.GridBagSizer(3,4)

        self.label = wx.StaticText(self.panel, label="This feature will be implemented in future versions")
        self.sizer.Add(self.label, pos=(0,1), flag=wx.TOP|wx.CENTER, border=5)

        butt_ok = wx.Button(self.panel, label="OK", size=(90,28))
        self.sizer.Add(butt_ok, pos=(1,2), flag=wx.RIGHT|wx.BOTTOM, border=10)
        butt_ok.Bind(wx.EVT_BUTTON, self.on_quit)

        self.sizer.AddGrowableCol(1)
        self.sizer.AddGrowableRow(1)
        self.panel.SetSizer(self.sizer)


    def on_quit(self, e):
        self.Close()
