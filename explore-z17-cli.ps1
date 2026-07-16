param(
    [string]$PlaywrightCli = "playwright-cli"
)

Set-StrictMode -Version Latest

function Fail([string]$message) {
    Write-Error $message
    exit 1
}

Write-Host "Checking playwright-cli availability..."
& $PlaywrightCli --version > $null 2>&1
if ($LASTEXITCODE -ne 0) { Fail "playwright-cli is not available. Install it and ensure it is on PATH." }

$targetUrl = 'https://www.ibm.com/z'
$screenshotPath = Join-Path $PSScriptRoot 'explore-z17-cli.png'

Write-Host "Opening IBM Z page with playwright-cli..."
& $PlaywrightCli open $targetUrl
if ($LASTEXITCODE -ne 0) { Fail "Failed to open $targetUrl with playwright-cli." }

Write-Host "Clicking the 'Explore the new IBM z17' link..."
$js = '(() => { const link = Array.from(document.querySelectorAll("a")).find(a => a.textContent.includes("Explore the new IBM z17")); if (!link) throw new Error("Link text not found"); const href = link.href; link.click(); return href; })()'
$href = & $PlaywrightCli eval $js
if ($LASTEXITCODE -ne 0) { Fail "Failed to click the IBM z17 link." }

Write-Host "Link clicked. Target href: $href"
Write-Host "Waiting for navigation to complete..."
Start-Sleep -Seconds 5

Write-Host "Taking a full-page screenshot..."
& $PlaywrightCli screenshot --filename $screenshotPath
if ($LASTEXITCODE -ne 0) { Fail "Failed to capture screenshot." }

Write-Host "Closing browser session..."
& $PlaywrightCli close > $null 2>&1

Write-Host "Done. Screenshot saved to $screenshotPath"
