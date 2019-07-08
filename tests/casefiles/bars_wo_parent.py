#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyMenuBar(wx.MenuBar):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyMenuBar.__init__
        wx.MenuBar.__init__(self, *args, **kwds)
        wxglade_tmp_menu = wx.Menu()
        self.Append(wxglade_tmp_menu, "File")
        # end wxGlade

# end of class MyMenuBar

class MyToolBar(wx.ToolBar):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyToolBar.__init__
        kwds["style"] = kwds.get("style", 0)
        wx.ToolBar.__init__(self, *args, **kwds)
        self.Realize()
        # end wxGlade

# end of class MyToolBar

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0)
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((200, 200))
        self.SetTitle("frame_1")
        
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        
        self.label_1 = wx.StaticText(self, wx.ID_ANY, "placeholder - every design\nneeds a toplevel window", style=wx.ALIGN_CENTER)
        sizer_1.Add(self.label_1, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 0)
        
        self.SetSizer(sizer_1)
        
        self.Layout()
        # end wxGlade

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame_1 = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame_1)
        self.frame_1.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
