import wx


'''class MyFrame(wx.Frame):
    def __init__(self,parent,title):
        super(MyFrame,self).__init__(parent,title=title,size=(300,200))
        panel= wx.Panel(self)
        self.center()

class myApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None,title="Our first window")
        self.frame.Show()

        return True
    
if __name__ == "__main":
    app = myApp(False)
    app.Mainloop()'''


app = wx.App()

frame = wx.Frame(None,-1,"Window title")

frame.Show()

app.MainLoop()