import win32gui
import win32con
import win32clipboard as w


# 获取粘贴板内容
def getText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_UNICODETEXT)
    w.CloseClipboard()
    return d

	

# 设置粘贴板内容
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT,aString)
    w.CloseClipboard()

# 发送内容
def send_qq(to_who,msg):
    setText(msg)
    qq = win32gui.FindWindow(None,to_who)
    win32gui.SendMessage(qq,258,22,2080193)
    win32gui.SendMessage(qq,770,0,0)
    win32gui.SendMessage(qq,win32con.WM_KEYDOWN,win32con.VK_RETURN,0)
    win32gui.SendMessage(qq,win32con.WM_KEYUP,win32con.VK_RETURN,0)



to_who = '***' # 设置接收人
msg = getText()  # 可自定义信息模板
send_qq(to_who,msg)










