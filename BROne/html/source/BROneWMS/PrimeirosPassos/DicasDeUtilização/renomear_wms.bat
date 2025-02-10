@echo off
setlocal enabledelayedexpansion

rem Percorre todos os arquivos na pasta atual
for %%F in (*.png *.gif) do (
    rem Verifique se o nome do arquivo já contém "WMS-"
    echo %%F | findstr /C:"WMS-" > nul
    if errorlevel 1 (
        rem Se não contém, então renomeie o arquivo
        set "filename=%%~nF"
        set "extension=%%~xF"
        ren "%%F" "WMS-!filename!!extension!"
    )
)

echo Renomeacao concluida.
pause