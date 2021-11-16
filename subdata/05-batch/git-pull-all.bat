@echo off
echo start 
for /d %%i in (*) do (
    echo ---dir---
    echo %%i
    cd %%i
    call :subdir
    cd ..
)
echo for end
pause
exit
::执行到这里就算结束了

:subdir
for /d %%i in (*) do (
    echo ---subdir---
    echo %%i
    cd %%i
    git pull
    cd ..
)
goto :eof
::eof 应该是系统关键字，不用另外定义，定义也没有效果


::https://cloud.tencent.com/developer/article/1347373