echo off
::-f 不弹出提示
schtasks /delete /tn "itzheng_shutdown" -f
pause