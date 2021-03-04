@echo off

for /f "tokens=5" %%i in ('netstat -aon ^| findstr ":4723"') do (

    set n=%%i

)
taskkill /f /pid %n%

@ echo. & paus