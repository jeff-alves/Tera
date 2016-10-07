import wx
from game.services.icon_database import IconDatabase

class TrayIcon(wx.TaskBarIcon):
    TBMENU_RESTORE = wx.NewId()
    TBMENU_CLOSE = wx.NewId()

    def __init__(self, frame):
        wx.TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon(wx.IconFromBitmap(IconDatabase()['ui.icon'].GetBitmap()), self.frame.GetTitle())
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
        self.frame.menu_bar.btn_pin.SetChecked(True)

    def OnTaskBarClose(self, event):
        self.frame.Close()

    def OnTaskBarLeftClick(self, event):
        menu = self.CreatePopupMenu()
        self.PopupMenu(menu)
        menu.Destroy()