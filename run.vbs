currentScriptPath = WScript.ScriptFullName
currentDirectory = Left(currentScriptPath, InStrRev(currentScriptPath, "\") - 1)
Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")
tempFile = currentDirectory & "\cmd_processes.txt"

' Kill existing processes from the file
If objFSO.FileExists(tempFile) Then
    objShell.Run "powershell -Command ""Get-Content '" & tempFile & "' | ForEach-Object { if ($_ -match '\d+') { $id = [int]$matches[0]; try { Stop-Process -Id $id -Force -ErrorAction Stop } catch { } } }""", 0, True
    objFSO.DeleteFile(tempFile)
End If

' Run your execute.bat
processID = objShell.Run("""" & currentDirectory & "\execute.bat""", 0, False)
WScript.Sleep 2000

' Save processes specifically for execute.bat
objShell.Run "powershell -Command """ & _
    "$processes = @(); " & _
    "$executeCmd = Get-WmiObject Win32_Process | Where-Object { $_.Name -eq 'cmd.exe' -and $_.CommandLine -like '*execute.bat*' }; " & _
    "$processes += $executeCmd; " & _
    "$executeCmd | ForEach-Object { " & _
        "$conhost = Get-WmiObject Win32_Process | Where-Object { $_.Name -eq 'conhost.exe' -and $_.ParentProcessId -eq $_.ProcessId }; " & _
        "$processes += $conhost; " & _
    "}; " & _
    "$processes | Select-Object ProcessId | Out-File -FilePath '" & tempFile & "' -Encoding UTF8" & _
    """", 0, True

WScript.Sleep 500

Set objFSO = Nothing
Set objShell = Nothing
