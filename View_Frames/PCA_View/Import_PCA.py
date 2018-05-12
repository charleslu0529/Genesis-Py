import os
import wx

class PCA_Import_View(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(PCA_Import_View, self).__init__(*args, **kwargs)

        self.ShowWindow()

    def ShowWindow(self):
        self.SetSize((400, 300))
        self.SetTitle('Import PCA Files')
        self.Centre

    ###Panel###
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(4, 4)

        button_import = wx.Button(panel, label="Import data:")
        sizer.Add(button_import, pos=(0,0))

        text_import_loc = wx.TextCtrl(panel)
        sizer.Add(text_import_loc, pos=(0,1), span=(1,3), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        label_01 = wx.StaticText(panel, label="Import Settings")
        sizer.Add(label_01, pos=(2,0), flag=wx.LEFT, border=5)

        butt_ok = wx.Button(panel, label="Ok")
        sizer.Add(butt_ok, pos=(3,2), flag=wx.RIGHT|wx.BOTTOM, border=10)

        butt_no = wx.Button(panel, label="Cancel")
        sizer.Add(butt_no, pos=(3,3), flag=wx.RIGHT|wx.BOTTOM, border=10)

        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)
        panel.SetSizer(sizer)


def main():
    app = wx.App()
    ex = PCA_Import_View(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
        
