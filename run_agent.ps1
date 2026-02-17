# 1. Force PowerShell to read the input file as UTF8
$devpostText = Get-Content -Raw -Path "./devpost_input.txt" -Encoding utf8

# 2. Package it into JSON for the request
$body = @{
    text = $devpostText
} | ConvertTo-Json

# 3. Send it to the agent and CAPTURE the response
Write-Host "🚀 Triggering Hackathon Agent..." -ForegroundColor Cyan

# We store the result in $response instead of piping directly to a file
$response = Invoke-RestMethod -Uri "http://localhost:8080/run" `
                  -Method Post `
                  -ContentType "application/json" `
                  -Body $body

# 4. Convert the PowerShell object BACK to JSON and save it
# -Depth 10 ensures nested data (like your lists) isn't truncated
$response | ConvertTo-Json -Depth 10 | Set-Content -Path "./hackathon_report.json" -Encoding utf8

Write-Host "✅ Analysis Complete! Report saved to: hackathon_report.json" -ForegroundColor Green