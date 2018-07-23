; 等待5秒钟，让上传窗口出现
WinWait("[CLASS:#32770]","",5)

;把输入焦点定位到上传输入文本框中
ControlFocus("打开", "","Edit1")

;在文件名那里，使用参数
ControlSetText("打开", "", "Edit1", $CmdLine[1])

;等待上传时间，单位是毫秒 1秒 = 1000 毫秒
Sleep(5000)

;点击"打开"按钮，也就是上传
ControlClick("打开", "","Button1");