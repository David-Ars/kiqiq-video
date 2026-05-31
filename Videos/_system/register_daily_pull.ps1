# Run ONCE (normal PowerShell) to schedule the daily API-Football pull at 09:00.
# Remove later with: Unregister-ScheduledTask -TaskName "KiqIQ-APIFootball-Pull" -Confirm:$false
$script = Join-Path $PSScriptRoot "run_pull.ps1"
$action = New-ScheduledTaskAction -Execute "powershell.exe" `
  -Argument ('-NoProfile -ExecutionPolicy Bypass -File "{0}"' -f $script)
$trigger = New-ScheduledTaskTrigger -Daily -At 9am
Register-ScheduledTask -TaskName "KiqIQ-APIFootball-Pull" -Action $action -Trigger $trigger `
  -Description "Daily API-Football archive pull until 2026-06-10" -Force
Write-Host "Scheduled: KiqIQ-APIFootball-Pull, daily at 09:00."
