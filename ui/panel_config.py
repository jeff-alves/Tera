import wx
from ui.custom_checkbox import CustomCheckBox

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

        self.btn_boss = CustomCheckBox(self, 'ui.checkbox_1', 'ui.checkbox_2', width=15, height=15)
        self.btn_boss.SetChecked(True)
        gbSizer.Add(self.btn_boss, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_RIGHT, 5)

        txt = wx.StaticText(self, wx.ID_ANY, "Include Party", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer.Add(txt, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btn_party = CustomCheckBox(self, 'ui.checkbox_1', 'ui.checkbox_2', width=15, height=15)
        self.btn_party.SetChecked(True)
        gbSizer.Add(self.btn_party, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_RIGHT, 5)

        txt = wx.StaticText(self, wx.ID_ANY, "Include Others", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer.Add(txt, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btn_others = CustomCheckBox(self, 'ui.checkbox_1', 'ui.checkbox_2', width=15, height=15)
        gbSizer.Add(self.btn_others, wx.GBPosition(3, 1), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_RIGHT, 5)

        self.line1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        gbSizer.Add(self.line1, wx.GBPosition(4, 0), wx.GBSpan(1, 2), wx.EXPAND | wx.ALL, 0)

        gbSizer.AddGrowableCol(1)
        self.SetSizer(gbSizer)
        self.Layout()

    def slider_evt(self, event):
        self.parent.SetTransparent(self.slider.GetValue())
