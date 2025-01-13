# Create or clear the output file
$outputFile = "C:\ScriptingTasks\output.txt"
New-Item -Path $outputFile -ItemType File -Force

# 1. Find all scripting commands related to "print"
Get-Command -Name *print* | Out-File -FilePath $outputFile -Append

# 2. Append the current date and time
Get-Date -Format "F" | Out-File -FilePath $outputFile -Append

# 3. Close all Notepad files
Get-Process -Name notepad -ErrorAction SilentlyContinue | Stop-Process -Force

# 4. Append the last 20 errors from the event log
Get-EventLog -LogName System -EntryType Error -Newest 20 | Out-File -FilePath $outputFile -Append

# 5. Append a list of all available WMI classes
Get-WmiObject -List | Out-File -FilePath $outputFile -Append

# 6. List the start command or full path of every executable
Get-CimInstance Win32_Process | Select-Object Name, ExecutablePath | Out-File -FilePath $outputFile -Append

# 7. Identify the account the spooler service is running as
Get-WmiObject -Class Win32_Service -Filter "Name='Spooler'" | Select-Object StartName | Out-File -FilePath $outputFile -Append