currentScriptPath = WScript.ScriptFullName
currentDirectory = Left(currentScriptPath, InStrRev(currentScriptPath, "\") - 1)

Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

tempFile = currentDirectory & "\cmd_processes.txt"

objShell.Run "powershell -Command ""Get-Content '" & tempFile & "' | ForEach-Object { if ($_ -match '\d+') { $id = [int]$matches[0]; Stop-Process -Id $id -Force -ErrorAction SilentlyContinue } }""", 0, True

If objFSO.FileExists(tempFile) Then
    objFSO.DeleteFile(tempFile)
End If

processID = objShell.Run("""" & currentDirectory & "\execute.bat""", 0, False)

WScript.Sleep 2000

objShell.Run "powershell -Command ""Get-Process cmd | Select-Object Id | Out-File -FilePath '" & tempFile & "'""", 0, True

WScript.Sleep 500

Set objFSO = Nothing
Set objShell = Nothing