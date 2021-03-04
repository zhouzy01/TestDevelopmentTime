E:

cd E:\python\Workspace\TestDevelopmentTime\test_ui_app

adb connect 127.0.0.1:7555

pytest

start cmd /C allure generate ./result/ -o ./report/ --clean


for /f "tokens=5" %%i in ('netstat -aon ^| findstr ":4723"') do (
    set n=%%i
)

# taskkill /f /pid %n%

taskkill /f /im cmd.exe

start cmd /C java -jar agent.jar -jnlpUrl http://192.168.126.128:8080/computer/mywindows/slave-agent.jnlp -secret 4fb85fc518c3f81a29cd3daa9cc0cfe249130bd2a1e3b447864549964481eae5 -workDir "E:\temp"

allure open -h 127.0.0.1 -p 8888 ./report

@cmd.exe