import wx

class TrayIcon(wx.TaskBarIcon):
    TBMENU_RESTORE = wx.NewId()
    TBMENU_CLOSE = wx.NewId()
    TBMENU_CHANGE = wx.NewId()
    TBMENU_REMOVE = wx.NewId()
    TRAY_TOOLTIP = 'Tera DPS'

    def __init__(self, frame):
        wx.TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon(wx.IconFromBitmap(wx.Bitmap('icon.ico')), self.TRAY_TOOLTIP)
        self.Bind(wx.EVT_MENU, self.OnTaskBarClose, id=self.TBMENU_CLOSE)
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.OnTaskBarLeftClick)

    def CreatePopupMenu(self, evt=None):  # default rightclick action
        menu = wx.Menu()
        menu.Append(self.TBMENU_RESTORE, "Open Program")
        menu.Append(self.TBMENU_CHANGE, "Show all the Items")
        menu.AppendSeparator()
        menu.Append(self.TBMENU_CLOSE, "Exit Program")
        return menu

    def OnTaskBarActivate(self, evt):
        pass

    def OnTaskBarClose(self, evt):
        self.frame.Close()

    def OnTaskBarLeftClick(self, evt):
        menu = self.CreatePopupMenu()
        self.PopupMenu(menu)
        menu.Destroy()


def GetRoundBitmap(w, h, r):
    maskColor = wx.Color(0, 0, 0)
    shownColor = wx.Color(5, 5, 5)
    b = wx.EmptyBitmap(w, h)
    dc = wx.MemoryDC(b)
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

class TeraFrame(wx.Frame):
    def __init__(self):
        style = (wx.CLIP_CHILDREN | wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR | wx.NO_BORDER | wx.FRAME_SHAPED)
        wx.Frame.__init__(self, None, title='Tera DPS', style=style)
        self.radius = 8
        self.SetSize((250, 200))
        self.SetPosition((10, 10))
        self.SetTransparent(200)
        self.tbIcon = TrayIcon(self)
        self.Bind(wx.EVT_MOUSE_CAPTURE_LOST, self.OnMouseLost)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
        self.Bind(wx.EVT_MOTION, self.OnMouse)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.SetRoundShape()
        self.Show(True)

    def SetRoundShape(self, event=None):
        w, h = self.GetSizeTuple()
        self.SetShape(GetRoundShape(w, h, self.radius))

    def OnMouseLost(self, event):  # bug avoid
        pass

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc = wx.GCDC(dc)
        dc.SetUserScale(1.0, 1.0)
        w, h = self.GetSizeTuple()
        dc.SetPen(wx.Pen("#FFFFFF", width=1))
        dc.SetBrush(wx.Brush("#000000"))
        dc.DrawRoundedRectangle(0, 0, w, h, self.radius)
        dc.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL , wx.FONTWEIGHT_BOLD))
        dc.SetTextForeground("#FFFFFF")
        dc.DrawLabel('TERA Bot/DPS', wx.Rect(125, 10, 0, 0), wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL)

        dc.SetPen(wx.Pen("#993333", width=1))
        dc.SetBrush(wx.Brush("#111111", wx.TRANSPARENT))
        dc.DrawRoundedRectangle(40, 40, 200, 30, 2)
        dc.GradientFillLinear((140, 41, 99, 14), '#454545', '#3B3B3B', wx.NORTH)
        dc.GradientFillLinear((140, 55, 99, 14), '#454545', '#3B3B3B', wx.SOUTH)

        dc.GradientFillLinear((41, 41, 99, 14), '#526687', '#303C4F', wx.SOUTH)
        dc.GradientFillLinear((41, 55, 99, 14), '#526687', '#303C4F', wx.NORTH)

        dc.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL , wx.FONTWEIGHT_BOLD))
        dc.SetTextForeground("#FFFFFF")
        dc.DrawLabel('Player.Name', wx.Rect(45, 45, 0, 0))

    def OnKeyUp(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.Close()
        elif event.ControlDown() and event.GetKeyCode() == wx.WXK_INSERT:
            pass  # paste to TERA chat
        else:
            event.Skip()

    def OnMouse(self, event):
        if not event.Dragging():
            self._dragPos = None
            return
        self.CaptureMouse()
        if not self._dragPos:
            self._dragPos = event.GetPosition()
        else:
            pos = event.GetPosition()
            displacement = self._dragPos - pos
            self.SetPosition(self.GetPosition() - displacement)

    def OnClose(self, event):
        dial = wx.MessageDialog(None, 'Are you sure to quit TERA DPS?', 'Quit?', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dial.ShowModal() == 5104: return
        self.tbIcon.RemoveIcon()
        self.tbIcon.Destroy()
        self.Destroy()

app = wx.App()
f = TeraFrame()
app.MainLoop()
