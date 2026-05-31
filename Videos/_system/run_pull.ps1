# KiqIQ: daily API-Football archive pull. Reads the key from the local key file,
# then runs the resumable ingester. Used by a Windows Task Scheduler daily job.
$ErrorActionPreference = "Stop"
$kf = (Get-ChildItem "$PSScriptRoot\apifootball.key*" | Select-Object -First 1).FullName
$env:APIFOOTBALL_KEY = (Get-Content $kf -Raw).Trim()
python "$PSScriptRoot\apifootball_archive.py"
