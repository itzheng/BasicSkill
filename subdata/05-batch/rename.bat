@echo off
set /p str1= 请输入要替换的文件(文件夹)名字符串（可替换空格）：
set /p str2= 请输入替换后的文件(文件夹)名字符串（去除则直接回车）：
echo.echo 正在修改文件(夹)名中，请稍候……
for /f "delims=" %%a in ('dir /s /b ^|sort /+65535') do (
if "%%~nxa" neq "%~nx0" (
set "file=%%a"
set "name=%%~na"
set "extension=%%~xa"
call set "name=%%name:%str1%=%str2%%%"
setlocal enabledelayedexpansion
ren "!file!" "!name!!extension!" 2>nul
endlocal))

作者：何先生
链接：https://www.zhihu.com/question/29446913/answer/218671011
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。