import wx


class PanelPlayer(wx.Panel):
    def __init__(self, parent, name, cls, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.SetBackgroundColour(self.parent.GetBackgroundColour())
        self.SetForegroundColour(self.parent.GetForegroundColour())
        self.SetFont(self.parent.GetFont())
        self.img_size = 20
        self.name = name
        self.cls = cls

        gbSizer = wx.GridBagSizer()
        self.txtTitle = wx.StaticText(self, wx.ID_ANY, u"Tera DPS ", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer.Add(self.txtTitle, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        self.txtServer = wx.StaticText(self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer.Add(self.txtServer, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_HORIZONTAL , 5)


        self.btn_pin = CustomCheckBox(self, 'ui.pin', color_checked='#FF0000', color_hover='#1188FF')
        self.btn_pin.Bind(wx.EVT_CHECKBOX, self.parent.TogglePin)
        gbSizer.Add(self.btn_pin, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 6)

        self.btn_config = CustomCheckBox(self, 'ui.settings', color_checked='#FF0000', color_hover='#1188FF')
        self.btn_config.Bind(wx.EVT_CHECKBOX, self.parent.ToggleConfig)
        gbSizer.Add(self.btn_config, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 6)

        self.btn_close = CustomCheckBox(self, 'ui.close', color_hover='#1188FF')
        self.btn_close.Bind(wx.EVT_CHECKBOX, self.parent.OnClose)
        gbSizer.Add(self.btn_close, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.ALL, 6)

        self.line1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        gbSizer.Add(self.line1, wx.GBPosition(1, 0), wx.GBSpan(1, 5), wx.EXPAND | wx.ALL, 0)

        gbSizer.AddGrowableCol(1)
        self.SetSizer(gbSizer)

    def OnMouse(self, event):
        if not event.Dragging():
            if self._dragPos:
                self.ReleaseMouse()
                x , y = self.parent.GetPosition()
                self.parent.config.WriteInt('x', x)
                self.parent.config.WriteInt('y', y)
            self._dragPos = None
            return
        if not self._dragPos:
            self.CaptureMouse()
            self._dragPos = event.GetPosition()
        else:
            pos = event.GetPosition()
            displacement = self._dragPos - pos
            self.parent.SetPosition(self.parent.GetPosition() - displacement)
