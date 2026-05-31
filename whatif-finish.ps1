# Run from C:\Users\david\Documents\Kiqiq\kiqiq
Set-Location C:\Users\david\Documents\Kiqiq\kiqiq

Write-Host "== sanity ==" -ForegroundColor Cyan
$dup = (Select-String -Path "src\lib\ai-context-formatters.ts" -Pattern "^export function formatWhatIfBlock").Count
if ($dup -ne 1) { Write-Host "FAIL duplicate formatWhatIfBlock exports ($dup)" -ForegroundColor Red; exit 1 }

Write-Host "== npm run build ==" -ForegroundColor Cyan
npm run build
if ($LASTEXITCODE -ne 0) { Write-Host "Build failed - share output with Claude." -ForegroundColor Red; exit $LASTEXITCODE }

Write-Host "== git commit + push ==" -ForegroundColor Cyan
git add src/lib/ai-intent-classifier.ts src/lib/ai-context.ts src/lib/ai-context-formatters.ts scripts/ask-eval/eval-set.ts
git commit -m "ai: whatif intent + hypothetical standings mutator + 3 eval cases"
git push
