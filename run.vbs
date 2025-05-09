' Get the full path of the current script
currentScriptPath = WScript.ScriptFullName

' Get the current directory by extracting the folder part of the path
currentDirectory = Left(currentScriptPath, InStrRev(currentScriptPath, "\") - 1)

CreateObject("WScript.Shell").Run """" & currentDirectory & "\execute.bat""", 0 , True
