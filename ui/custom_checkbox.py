import wx

from game.services.icon_database import IconDatabase
from util.util import img_transform


class CustomCheckBox(wx.PyControl):
    def __init__(self, parent, img_unchecked, img_checked=None, img_hover=None, color_checked=None, color_unchecked=None, color_hover=None, width=12, height=12, name=None):
        wx.PyControl.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER, wx.DefaultValidator, "CustomCheckBox")
        self.parent = parent
        self.name = name
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
        self.bitmaps = {"CheckedEnable": img_transform(IconDatabase()[img_checked].GetImage(), width=self.width, height=self.height, color=color_checked),
                        "UnCheckedEnable": img_transform(IconDatabase()[img_unchecked].GetImage(), width=self.width, height=self.height, color=color_unchecked),
                        "CheckedHoverEnable": img_transform(IconDatabase()[img_checked].GetImage(), width=self.width, height=self.height, color=color_hover),
                        "UnCheckedHoverEnable": img_transform(IconDatabase()[img_unchecked].GetImage(), width=self.width, height=self.height, color=color_hover),
                        "CheckedDisable": img_transform(IconDatabase()[img_checked].GetImage(), width=self.width, height=self.height, color=color_checked, gray=True),
                        "UnCheckedDisable": img_transform(IconDatabase()[img_unchecked].GetImage(), width=self.width, height=self.height, color=color_unchecked, gray=True)}


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
        if self.name: self.parent.parent.config.WriteBool(self.name, self.checked)