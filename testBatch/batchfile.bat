@echo off
setlocal enabledelayedexpansion

for %%f in (*.md) do (
  set "inputfile=%%f"
  set "outputfile=%%~nf.Rmd"

  >"%outputfile%" (
    for /f "usebackq delims=" %%i in ("!inputfile!") do (
      set "line=%%i"
      set "newline=!line:\`\`r=\`\`\{r\}!"
      echo !newline!
    )
  )
)
