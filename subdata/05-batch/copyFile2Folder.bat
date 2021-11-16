::复制指定文件到当前所有的文件夹
@echo off
set vcfile=zz_moto_config.xml
::遍历当前所有文件夹
for /d %%i in (*) do (
 ::复制指定文件到所有文件夹
 echo %%i 
 copy %vcfile% %%i
)
pause