from pywinauto.findwindows    import find_window
from pywinauto.win32functions import SetForegroundWindow
import wx

from ui.custom_menu_bar import CustomMenuBar
from ui.panel_config import PanelConfig
from ui.tray_icon import TrayIcon
from util.util import singleton


@singleton
class MainWindow(wx.Frame):
    def __init__(self):
        style = (wx.CLIP_CHILDREN | wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR | wx.BORDER_NONE | wx.FRAME_SHAPED)
        wx.Frame.__init__(self, None, title='Tera DPS', style=style)
        self.config = wx.Config('Tera DPS')
        self.panels = []
        self.radius = 12
        self.pin = True
        self.d_w, self.d_h = wx.DisplaySize()
        self.SetSize((250, 0))
        x = self.config.ReadInt('x')
        y = self.config.ReadInt('y')
        self.SetPosition((x if x else self.d_w - self.GetSizeTuple()[0] - 10, y if y else 10))
        self.SetBackgroundColour('#000000')
        self.SetForegroundColour('#FFFFFF')
        self.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL , wx.FONTWEIGHT_BOLD))
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_KEY_UP, self.OnKeyUp)

        gbSizer = wx.GridBagSizer()
        gbSizer.AddGrowableCol(0)

        self.menu_bar = CustomMenuBar(self)
        gbSizer.Add(self.menu_bar, wx.GBPosition(len(self.panels), 0), wx.GBSpan(1, 1), wx.EXPAND | wx.ALL, 0)
        self.panels.append(self.menu_bar)

        self.panel_config = PanelConfig(self)
        gbSizer.Add(self.panel_config, wx.GBPosition(len(self.panels), 0), wx.GBSpan(1, 1), wx.EXPAND | wx.ALL, 0)
        self.panels.append(self.panel_config)

        self.SetSizer(gbSizer)

        self.UpdateSize()
        self.SetTransparent(self.panel_config.slider.GetValue())
        self.Show(True)
        self.menu_bar.btn_pin.SetChecked(True)
        self.menu_bar.btn_config.SetChecked(False)
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

    def SetServerName(self, name):
        self.menu_bar.txtServer.SetLabelText(name)
        self.menu_bar.Layout()

    def GetRoundShape(self, w, h, r):
        return wx.RegionFromBitmap(self.GetRoundBitmap(w, h, r))

    def UpdateSize(self):
        w, h = 250, -2
        for p in self.panels:
            if p.IsShown() : h += p.GetSizeTuple()[1]

        self.Layout()
        self.SetSize((w, h))
        self.SetRoundShape()

    def SetRoundShape(self, event=None):
        w, h = self.GetSizeTuple()
        self.SetShape(self.GetRoundShape(w, h, self.radius))

    def TogglePin(self, event):
        if event.IsChecked():
            try: SetForegroundWindow(find_window(title=self.GetTitle()))
            except: pass
            self.SetWindowStyleFlag((wx.CLIP_CHILDREN | wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR | wx.BORDER_NONE | wx.FRAME_SHAPED))
        else:
            self.SetWindowStyleFlag((wx.CLIP_CHILDREN | wx.FRAME_NO_TASKBAR | wx.BORDER_NONE | wx.FRAME_SHAPED))

    def ToggleConfig(self, event):
        if event.IsChecked():
            self.panel_config.Show()
        else:
            self.panel_config.Hide()

        self.UpdateSize()

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
