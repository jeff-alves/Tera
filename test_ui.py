from pywinauto.findwindows    import find_window
from pywinauto.win32functions import SetForegroundWindow
import wx


class TrayIcon(wx.TaskBarIcon):
    TBMENU_RESTORE = wx.NewId()
    TBMENU_CLOSE = wx.NewId()

    def __init__(self, frame):
        wx.TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon(wx.IconFromBitmap(wx.Bitmap('icon.ico')), self.frame.GetTitle())
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

def GetRoundBitmap(w, h, r):
    maskColor = wx.Color(0, 0, 0)
    shownColor = wx.Color(5, 5, 5)
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

def GetRoundShape(w, h, r):
    return wx.RegionFromBitmap(GetRoundBitmap(w, h, r))

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def get_img(path, scale=None, width=None, height=None, rotate=None, color=None):
    img = wx.Image(path, wx.BITMAP_TYPE_ANY)
    if color:
        if type(color) == str: color = hex_to_rgb(color)
        while len(color) < 4: color += (255,)
        img = img.AdjustChannels(color[0] / 255., color[1] / 255., color[2] / 255., color[3] / 255.)
    if rotate:
        w, h = img.GetSize()
        img = img.Rotate(rotate, (w / 2., h / 2.))
    if scale:
        w, h = img.GetSize()
        img = img.Rescale(w * scale, h * scale, quality=wx.IMAGE_QUALITY_HIGH)
    elif width and height:
        img = img.Rescale(width, height, quality=wx.IMAGE_QUALITY_HIGH)
    return wx.BitmapFromImage(img)


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
        gbSizer.Add(self.txtServer, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.btn_pin = wx.BitmapButton(self, wx.ID_ANY, get_img('pin-inverted.png', width=self.img_size, height=self.img_size, color='#FF2222'))
        self.btn_pin.SetBitmapSelected(get_img('pin-inverted.png', width=self.img_size, height=self.img_size))
        self.btn_pin.SetBackgroundColour(self.GetBackgroundColour())
        self.btn_pin.SetWindowStyle(wx.BORDER_NONE)
        self.btn_pin.Bind(wx.EVT_BUTTON, self.parent.TogglePin)
        gbSizer.Add(self.btn_pin, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 6)

        self.btn_config = wx.BitmapButton(self, wx.ID_ANY, get_img('settings-inverted.png', width=self.img_size, height=self.img_size, color='#FF2222'))
        self.btn_config.SetBitmapSelected(get_img('settings-inverted.png', width=self.img_size, height=self.img_size))
        self.btn_config.SetBackgroundColour(self.GetBackgroundColour())
        self.btn_config.SetWindowStyle(wx.BORDER_NONE)
        self.btn_config.Bind(wx.EVT_BUTTON, self.parent.ToggleConfig)
        gbSizer.Add(self.btn_config, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 6)

        self.btn_close = wx.BitmapButton(self, wx.ID_ANY, get_img('close-inverted.png', width=self.img_size, height=self.img_size))
        self.btn_close.SetBitmapFocus(get_img('close-inverted.png', width=self.img_size, height=self.img_size, color='#1188FF'))
        self.btn_close.SetBitmapSelected(get_img('close-inverted.png', width=self.img_size, height=self.img_size, color='#FF2222'))
        self.btn_close.SetBackgroundColour(self.GetBackgroundColour())
        self.btn_close.SetWindowStyle(wx.BORDER_NONE)
        self.btn_close.Bind(wx.EVT_BUTTON, self.parent.OnClose)
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
        self.txtTitle = wx.StaticText(self, wx.ID_ANY, u"Opacity ", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer.Add(self.txtTitle, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.slider = wx.Slider(self, wx.ID_ANY, 200, 20, 255, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        self.slider.Bind(wx.EVT_SLIDER, self.slider_evt)
        gbSizer.Add(self.slider, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 0)

        self.line1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        gbSizer.Add(self.line1, wx.GBPosition(1, 0), wx.GBSpan(1, 2), wx.EXPAND | wx.ALL, 0)

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
        self.tbIcon = TrayIcon(self)
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

        self.SetTransparent(self.panel_config.slider.GetValue())
        self.Show(True)
        self.SetFocus()
        self.ToggleConfig(None)

    def CalcSize(self):
        h = 0
        for w in self.panels:
            if w.IsShown() : h += w.GetSizeTuple()[1]
        return (250 , h - 2)

    def SetRoundShape(self, event=None):
        w, h = self.GetSizeTuple()
        self.SetShape(GetRoundShape(w, h, self.radius))

    def TogglePin(self, event):
        if self.pin:
            self.pin = False
            self.SetWindowStyleFlag((wx.CLIP_CHILDREN | wx.FRAME_NO_TASKBAR | wx.BORDER_NONE | wx.FRAME_SHAPED))
        else:
            self.pin = True
            SetForegroundWindow(find_window(title=self.GetTitle()))
            self.SetWindowStyleFlag((wx.CLIP_CHILDREN | wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR | wx.BORDER_NONE | wx.FRAME_SHAPED))
        img = self.panel_main.btn_pin.GetBitmapLabel()
        self.panel_main.btn_pin.SetBitmapLabel(self.panel_main.btn_pin.GetBitmapSelected())
        self.panel_main.btn_pin.SetBitmapSelected(img)

    def ToggleConfig(self, event):
        if self.panel_config.IsShown():
            self.panel_config.Hide()
        else:
            self.panel_config.Show()
        img = self.panel_main.btn_config.GetBitmapLabel()
        self.panel_main.btn_config.SetBitmapLabel(self.panel_main.btn_config.GetBitmapSelected())
        self.panel_main.btn_config.SetBitmapSelected(img)

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
