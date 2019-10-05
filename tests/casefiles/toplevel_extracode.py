#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.9pre on Sat Oct  5 23:55:59 2019
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# frame extra code
# dialog extra code
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        # frame extra code before
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.SetTitle("frame")
        
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        
        sizer_1.Add((0, 0), 0, 0, 0)
        
        self.SetSizer(sizer_1)
        
        self.Layout()
        # frame extra code after

        self.Bind(wx.EVT_CLOSE, self.on_close_frame, self)
        self.Bind(wx.EVT_MENU_CLOSE, self.on_menu_close_frame, self)
        # end wxGlade

    def on_close_frame(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'on_close_frame' not implemented!")
        event.Skip()

    def on_menu_close_frame(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'on_menu_close_frame' not implemented!")
        event.Skip()

# end of class MyFrame

class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        # dialog extra code before
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle("dialog")
        
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        
        sizer_1.Add((0, 0), 0, 0, 0)
        
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        
        self.Layout()
        # dialog extra code after

        self.Bind(wx.EVT_CLOSE, self.on_close_dialog, self)
        # end wxGlade

    def on_close_dialog(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_close_dialog' not implemented!")
        event.Skip()

# end of class MyDialog

class MyMenuBar(wx.MenuBar):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyMenuBar.__init__
        # menubar extracode before
        wx.MenuBar.__init__(self, *args, **kwds)
        # menubar extracode after
        # end wxGlade

# end of class MyMenuBar

class wxToolBar(wx.ToolBar):
    def __init__(self, *args, **kwds):
        # begin wxGlade: wxToolBar.__init__
        # toolbar extracode before
        kwds["style"] = kwds.get("style", 0)
        wx.ToolBar.__init__(self, *args, **kwds)
        self.Realize()
        # toolbar extracode after
        # end wxGlade

# end of class wxToolBar

class MyDialog1(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog1.__init__
        # panel extracode before
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        
        sizer_1.Add((0, 0), 0, 0, 0)
        
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        
        self.Layout()
        # panel extracode after
        # end wxGlade

# end of class MyDialog1

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
