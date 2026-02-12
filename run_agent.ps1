# 1. Force PowerShell to read the file as UTF8
$devpostText = Get-Content -Raw -Path "./devpost_input.txt" -Encoding utf8

# 2. Package it into JSON
$body = @{
    text = $devpostText
} | ConvertTo-Json

# 3. Send it to the agent
Write-Host "🚀 Triggering Hackathon Agent..." -ForegroundColor Cyan

Invoke-RestMethod -Uri "http://localhost:8080/run" `
                  -Method Post `
                  -ContentType "application/json" `
                  -Body $body | Out-File -FilePath "./hackathon_report.json" -Encoding utf8

Write-Host "✅ Analysis Complete! Report saved to: hackathon_report.json" -ForegroundColor Green