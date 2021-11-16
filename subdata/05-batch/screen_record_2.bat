set timestr=%TIME: =0%
set cdate=%date:~0,4%%date:~5,2%%date:~8,2%_%timestr:~0,2%%timestr:~3,2%%timestr:~6,2%
set file=/sdcard/%cdate%.mp4
adb devices
adb shell screenrecord --time-limit 10 %file%
mkdir mp4
adb pull %file% ./mp4/
pause