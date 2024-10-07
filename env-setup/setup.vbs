Set shell = CreateObject("WScript.Shell")
shell.Run "install-package.bat", 1 , True
shell.Run "run.bat", 0 , True

' batFiles = Array("install-package.bat", "run.bat")
' For i = LBound(batFiles) To UBound(batFiles)
'     shell.Run batFiles(i), 1, True ' True means wait for the script to finish
' Next
