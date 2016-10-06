import sys

from pywinauto.findwindows    import find_window
from pywinauto.win32functions import SetForegroundWindow
import wx

from util.util import get_img


class TrayIcon(wx.TaskBarIcon):
    TBMENU_RESTORE = wx.NewId()
    TBMENU_CLOSE = wx.NewId()

    def __init__(self, frame):
        wx.TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon(wx.IconFromBitmap(wx.Bitmap('res/icon.ico')), self.frame.GetTitle())
        self.Bind(wx.EVT_MENU, self.OnTaskBarClose, id=self.TBMENU_CLOSE)
        self.Bind(wx.EVT_MENU, self.OnTaskBarRestore, id=self.TBMENU_RESTORE)
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.OnTaskBarLeftClick)

    def CreatePopupMenu(self, event=None):
        menu = wx.Menu()
        menu.Append(self.TBMENU_RESTORE, "Open Program")
        menu.AppendSeparator()
        menu.Append(self.TBMENU_CLOSE, "Exit Program")
        return menu

    def OnTaskBarRestore(self, event):
        if not self.frame.pin: self.frame.TogglePin(None)

    def OnTaskBarClose(self, event):
        self.frame.Close()

    def OnTaskBarLeftClick(self, event):
        menu = self.CreatePopupMenu()
        self.PopupMenu(menu)
        menu.Destroy()

class CustomCheckBox(wx.PyControl):
    def __init__(self, parent, img_unchecked, img_checked=None, img_hover=None, color_checked=None, color_unchecked=None, color_hover=None, width=12, height=12):
        wx.PyControl.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER, wx.DefaultValidator, "CustomCheckBox")
        self.width = width
        self.height = height
        self.InitializeBitmaps(img_unchecked, img_checked if img_checked else img_unchecked, color_checked, color_unchecked, color_hover)
        self.checked = False
        self.hover = False
        self.SetBackgroundColour(parent.GetBackgroundColour())
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)

    def OnEnterWindow(self, event):
        if not self.IsEnabled(): return
        self.hover = True
        self.Refresh()

    def OnLeaveWindow(self, event):
        if not self.IsEnabled(): return
        self.hover = False
        self.Refresh()

    def OnMouseUp(self, event):
        if not self.IsEnabled():
            return
        self.checked = not self.IsChecked()
        self.SendCheckBoxEvent()
        event.Skip()

    def OnSize(self, event):
        self.Refresh()

    def InitializeBitmaps(self, img_unchecked, img_checked, color_checked, color_unchecked, color_hover):
        self.bitmaps = {"CheckedEnable": get_img(img_checked, width=self.width, height=self.height, color=color_checked),
                        "UnCheckedEnable": get_img(img_unchecked, width=self.width, height=self.height, color=color_unchecked),
                        "CheckedHoverEnable": get_img(img_checked, width=self.width, height=self.height, color=color_hover),
                        "UnCheckedHoverEnable": get_img(img_unchecked, width=self.width, height=self.height, color=color_hover),
                        "CheckedDisable": get_img(img_checked, width=self.width, height=self.height, color=color_checked, gray=True),
                        "UnCheckedDisable": get_img(img_unchecked, width=self.width, height=self.height, color=color_unchecked, gray=True)}


    def GetBitmap(self):
        if self.IsEnabled():
            if self.IsChecked():
                if self.IsHover(): return self.bitmaps["CheckedHoverEnable"]
                return self.bitmaps["CheckedEnable"]
            else:
                if self.IsHover(): return self.bitmaps["UnCheckedHoverEnable"]
                return self.bitmaps["UnCheckedEnable"]
        else:
            if self.IsChecked():
                return self.bitmaps["CheckedDisable"]
            else:
                return self.bitmaps["UnCheckedDisable"]


    def DoGetBestSize(self):
        best = wx.Size(self.width, self.height)
        self.CacheBestSize(best)
        return best

    def SetForegroundColour(self, colour):
        wx.PyControl.SetForegroundColour(self, colour)
        self.Refresh()


    def SetBackgroundColour(self, colour):
        wx.PyControl.SetBackgroundColour(self, colour)
        self.Refresh()

    def Enable(self, enable=True):
        wx.PyControl.Enable(self, enable)
        self.Refresh()

    def IsChecked(self):
        return self.checked

    def IsHover(self):
        return self.hover

    def SetChecked(self, value=True):
        self.checked = value
        self.SendCheckBoxEvent()

    def OnPaint(self, event):
        dc = wx.BufferedPaintDC(self)
        dc.Clear()
        dc.DrawBitmap(self.GetBitmap(), 0, 0, True)

    def OnEraseBackground(self, event):
        pass

    def SendCheckBoxEvent(self):
        checkEvent = wx.CommandEvent(wx.wxEVT_COMMAND_CHECKBOX_CLICKED, self.GetId())
        checkEvent.SetInt(int(self.checked))
        checkEvent.SetEventObject(self)
        self.GetEventHandler().ProcessEvent(checkEvent)
        self.Refresh()

class PanelMain(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.SetBackgroundColour(self.parent.GetBackgroundColour())
        self.SetForegroundColour(self.parent.GetForegroundColour())
        self.SetFont(self.parent.GetFont())
        self.img_size = 12
        self._dragPos = None
        self.Bind(wx.EVT_MOTION, self.OnMouse)

        gbSizer = wx.GridBagSizer()
        self.txtTitle = wx.StaticText(self, wx.ID_ANY, u"Tera DPS ", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer.Add(self.txtTitle, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        self.txtServer = wx.StaticText(self, wx.ID_ANY, u"Server Name", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer.Add(self.txtServer, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_HORIZONTAL , 5)


        self.btn_pin = CustomCheckBox(self, 'res/pin-inverted.png', color_checked='#FF0000', color_hover='#1188FF')
        self.btn_pin.Bind(wx.EVT_CHECKBOX, self.parent.TogglePin)
        gbSizer.Add(self.btn_pin, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 6)

        self.btn_config = CustomCheckBox(self, 'res/settings-inverted.png', color_checked='#FF0000', color_hover='#1188FF')
        self.btn_config.Bind(wx.EVT_CHECKBOX, self.parent.ToggleConfig)
        gbSizer.Add(self.btn_config, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 6)

        self.btn_close = CustomCheckBox(self, 'res/close-inverted.png', color_hover='#1188FF')
        self.btn_close.Bind(wx.EVT_CHECKBOX, self.parent.OnClose)
        gbSizer.Add(self.btn_close, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.ALL, 6)

        self.line1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        gbSizer.Add(self.line1, wx.GBPosition(1, 0), wx.GBSpan(1, 5), wx.EXPAND | wx.ALL, 0)

        gbSizer.AddGrowableCol(1)
        self.SetSizer(gbSizer)

    def OnMouse(self, event):
        if not event.Dragging():
            if self._dragPos: self.ReleaseMouse()
            self._dragPos = None
            return
        if not self._dragPos:
            self.CaptureMouse()
            self._dragPos = event.GetPosition()
        else:
            pos = event.GetPosition()
            displacement = self._dragPos - pos
            self.parent.SetPosition(self.parent.GetPosition() - displacement)

class PanelConfig(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.SetBackgroundColour(self.parent.GetBackgroundColour())
        self.SetForegroundColour(self.parent.GetForegroundColour())
        self.SetFont(self.parent.GetFont())
        self.SetFont(wx.Font(8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL , wx.FONTWEIGHT_BOLD))

        gbSizer = wx.GridBagSizer()

        txt = wx.StaticText(self, wx.ID_ANY, "Opacity", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer.Add(txt, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.slider = wx.Slider(self, wx.ID_ANY, 200, 30, 255, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        self.slider.Bind(wx.EVT_SLIDER, self.slider_evt)
        gbSizer.Add(self.slider, wx.GBPosition(0, 1), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 0)

        txt = wx.StaticText(self, wx.ID_ANY, "Only Boss", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer.Add(txt, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btn_boss = CustomCheckBox(self, 'res/checkbox1.png', 'res/checkbox2.png', width=15, height=15)
        self.btn_boss.SetChecked(True)
        gbSizer.Add(self.btn_boss, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_RIGHT, 5)

        txt = wx.StaticText(self, wx.ID_ANY, "Include Party", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer.Add(txt, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btn_party = CustomCheckBox(self, 'res/checkbox1.png', 'res/checkbox2.png', width=15, height=15)
        self.btn_party.SetChecked(True)
        gbSizer.Add(self.btn_party, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_RIGHT, 5)

        txt = wx.StaticText(self, wx.ID_ANY, "Include Others", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer.Add(txt, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btn_others = CustomCheckBox(self, 'res/checkbox1.png', 'res/checkbox2.png', width=15, height=15)
        gbSizer.Add(self.btn_others, wx.GBPosition(3, 1), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_RIGHT, 5)

        self.line1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        gbSizer.Add(self.line1, wx.GBPosition(4, 0), wx.GBSpan(1, 2), wx.EXPAND | wx.ALL, 0)

        gbSizer.AddGrowableCol(1)
        self.SetSizer(gbSizer)
        self.Layout()

    def slider_evt(self, event):
        self.parent.SetTransparent(self.slider.GetValue())

class TeraFrame(wx.Frame):
    def __init__(self):
        style = (wx.CLIP_CHILDREN | wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR | wx.BORDER_NONE | wx.FRAME_SHAPED)
        wx.Frame.__init__(self, None, title='Tera DPS', style=style)
        self.panels = []
        self.radius = 12
        self.pin = True
        self.d_w, self.d_h = wx.DisplaySize()
        self.SetSize(self.CalcSize())
        self.SetPosition((self.d_w - self.GetSizeTuple()[0] - 10, 0 + 10))
        self.SetBackgroundColour('#000000')
        self.SetForegroundColour('#FFFFFF')
        self.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL , wx.FONTWEIGHT_BOLD))
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_KEY_UP, self.OnKeyUp)

        gbSizer = wx.GridBagSizer()
        gbSizer.AddGrowableCol(0)

        self.panel_main = PanelMain(self)
        gbSizer.Add(self.panel_main, wx.GBPosition(len(self.panels), 0), wx.GBSpan(1, 1), wx.EXPAND | wx.ALL, 0)
        self.panels.append(self.panel_main)

        self.panel_config = PanelConfig(self)
        gbSizer.Add(self.panel_config, wx.GBPosition(len(self.panels), 0), wx.GBSpan(1, 1), wx.EXPAND | wx.ALL, 0)
        self.panels.append(self.panel_config)

        self.SetSizer(gbSizer)

        self.Layout()
        self.SetSize(self.CalcSize())
        self.SetRoundShape()
        self.SetTransparent(self.panel_config.slider.GetValue())
        self.Show(True)
        self.panel_main.btn_pin.SetChecked(True)
        self.panel_main.btn_config.SetChecked(False)
        self.SetFocus()
        self.tbIcon = TrayIcon(self)

    def GetRoundBitmap(self, w, h, r):
        maskColor = wx.Colour(0, 0, 0)
        shownColor = wx.Colour(5, 5, 5)
        b = wx.EmptyBitmap(w, h)
        dc = wx.MemoryDC(b)
        dc.SetBackgroundMode(wx.TRANSPARENT)
        dc.SetBrush(wx.Brush(maskColor))
        dc.DrawRectangle(0, 0, w, h)
        dc.SetBrush(wx.Brush(shownColor))
        dc.SetPen(wx.Pen(shownColor))
        dc.DrawRoundedRectangle(0, 0, w, h, r)
        dc.SelectObject(wx.NullBitmap)
        b.SetMaskColour(maskColor)
        return b

    def GetRoundShape(self, w, h, r):
        return wx.RegionFromBitmap(self.GetRoundBitmap(w, h, r))

    def CalcSize(self):
        h = 0
        for w in self.panels:
            if w.IsShown() : h += w.GetSizeTuple()[1]
        return (250 , h - 2)

    def SetRoundShape(self, event=None):
        w, h = self.GetSizeTuple()
        self.SetShape(self.GetRoundShape(w, h, self.radius))

    def TogglePin(self, event):
        if event.IsChecked():
            SetForegroundWindow(find_window(title=self.GetTitle()))
            self.SetWindowStyleFlag((wx.CLIP_CHILDREN | wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR | wx.BORDER_NONE | wx.FRAME_SHAPED))
        else:
            self.SetWindowStyleFlag((wx.CLIP_CHILDREN | wx.FRAME_NO_TASKBAR | wx.BORDER_NONE | wx.FRAME_SHAPED))

    def ToggleConfig(self, event):
        if event.IsChecked():
            self.panel_config.Show()
        else:
            self.panel_config.Hide()

        self.SetSize(self.CalcSize())
        self.SetRoundShape()
        self.SetFocus()

    def OnKeyUp(self, event):
        if event.ControlDown() and event.GetKeyCode() == wx.WXK_INSERT:
            pass  # paste to TERA chat
        else:
            event.Skip()

    def OnClose(self, event):
        dial = wx.MessageDialog(None, 'Are you sure to quit TERA DPS?', 'Quit?', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dial.ShowModal() == 5104: self.SetFocus(); return
        self.tbIcon.RemoveIcon()
        self.tbIcon.Destroy()
        self.Destroy()

app = wx.App()
f = TeraFrame()
app.MainLoop()
