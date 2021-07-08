schtasks /create /tn "itzheng_shutdown" /tr "shutdown -s -t 30" /sc daily /st 20:20 -f
pause
