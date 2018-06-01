import wx
import View_Frames.Colour_Customiser as colour_cust

class Settings_Frame(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Settings_Frame, self).__init__(*args, **kwargs)

        self.type_of_graph = ""
        self.label = ""
        self.panel = None
        self.sizer = wx.GridBagSizer(4,3)
        self.child = None
        self.Center()

        self.InitUI()

    def InitUI(self):
        self.panel = wx.Panel(self)

        butt_change_colour = wx.Button(self.panel, label="Change Colour")
        self.sizer.Add(butt_change_colour, pos=(0,0), flag=wx.CENTER, border=10)
        butt_change_colour.Bind(wx.EVT_BUTTON, self.show_colour_dialogue)

        self.label = wx.StaticText(self.panel, label="Other settings to be added soon.")
        self.sizer.Add(self.label, pos=(1, 0), flag=wx.TOP | wx.CENTER, border=5)

        # self.sizer.AddGrowableCol(4)
        # self.sizer.AddGrowableRow(3)
        self.panel.SetSizer(self.sizer)

        self.panel.SetSizer(self.sizer)

    def show_colour_dialogue(self, e):
        self.child = colour_cust.Customise_Colour_Frame(self, title="Change Colour")
        self.child.Show()

    def on_quit(self, e):
        self.Close()
