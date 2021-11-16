set time=%TIME: =0%
set cdate=%date:~0,4%%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%%time:~6,2%
set file=/sdcard/%cdate%.mp4
adb devices
adb shell screenrecord %file%
mkdir mp4
adb pull %file% ./mp4/
pause