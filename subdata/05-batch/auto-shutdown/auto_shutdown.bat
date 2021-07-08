echo off
::设置关机时间
set sd_time=20:30

echo 系统将于 %sd_time% 自动关机

set cur_time=%TIME: =0%
set cur_time=%cur_time:~0,5%
echo 当前时间是 %cur_time%

::100%sd_time:~0,2%%%100 取2位数字
set sd_hh=100%sd_time:~0,2%%%100
set sd_mm=100%sd_time:~3,2%%%100
::echo sd_hh is %sd_hh% , sd_mm is %sd_mm%

set cur_hh=100%cur_time:~0,2%%%100
set cur_mm=100%cur_time:~3,2%%%100
::echo cur_hh is %cur_hh% , cur_mm is %cur_mm%

::CD = 倒计时
set /a cd_time_hh=(%sd_hh%)-(%cur_hh%)
set /a cd_time_mm=(%sd_mm%)-(%cur_mm%)
::echo cd_time_hh is %cd_time_hh%, cd_time_mm is %cd_time_mm%
:: EQU - 等于 ; NEQ - 不等于 ; LSS - 小于 ; LEQ - 小于或等于 ; GTR - 大于 ; GEQ - 大于或等于
:: 条件语句内必须有内容执行，否则会报错
echo 小时等于%cd_time_hh%，分钟等于%cd_time_mm%
if %cd_time_hh% GTR 0 (
    ::小时大于0
	echo 小时大于0
    goto after
) else if  %cd_time_hh% EQU 0 (
    ::小时等于0，这个要判断分钟，如果分钟大于或等于0，计算分钟的秒数，如果分钟小于0，那么只能等明天
	if %cd_time_mm% GEQ 0 (
		echo 小时等于0，分钟大于等于0
	    goto after
	) else (
	    echo 小时等于0，分钟小于0
	    goto before
	)
) else (
    ::时间小于0，也就是已经过了，得等明天了
	echo 小时小于0
	goto before
)
::经过判断，总结就两种情况，一种是已经过去了，等明天，一种是今天就能做
::小时大于0,剩余秒数等于:(剩余小时*60分*60秒)+(剩余分钟*60秒)
:after
::之后，时间大于0
    echo ==== 时间未到，今天执行 ====
	set /a hh_to_ss=(%cd_time_hh%*60*60)
    ::echo cd_time_mm=%cd_time_mm%
    set /a mm_to_ss=%cd_time_mm%*60
	::echo mm_to_ss=%mm_to_ss%
	::echo hh_to_ss=%hh_to_ss%，mm_to_ss=%mm_to_ss%
    set /a cd_time_ss=%hh_to_ss%+%mm_to_ss%
    goto shutdown
	
:before
::之前，小于0，那么等明天，就是+24小时
    echo ==== 时间已过，明天执行 ====
	set /a hh_to_ss=(24+%cd_time_hh%)*60*60
    ::echo cd_time_mm=%cd_time_mm%
    set /a mm_to_ss=%cd_time_mm%*60
	::echo mm_to_ss=%mm_to_ss%
	::echo hh_to_ss=%hh_to_ss%，mm_to_ss=%mm_to_ss%
    set /a cd_time_ss=%hh_to_ss%+%mm_to_ss%
    goto shutdown
:shutdown
    echo 距离关机剩余:%cd_time_ss% 秒
	shutdown -a
	shutdown -s -t %cd_time_ss%

::pause
set /p "input=要取消关机请输入Y,回车确认:"
if "%input%" == "" (
::输入为空
    echo 输入为空
	goto continue_shutdown
)

::去掉输入的空格
set "input=%input: =%"

::已经去掉空格，需要再次判断空格
if "%input%" == "" (
::输入为空
    echo 输入为空
	goto continue_shutdown
)
if %input% EQU Y (
	goto cancel_shutdown
) else if %input% EQU y (
	goto cancel_shutdown
) else (
    echo 其他字符
	goto continue_shutdown
)

:cancel_shutdown
    shutdown -a
	echo 关机操作已取消
	goto end

:continue_shutdown
    echo 关机操作继续执行
	goto end
	
	
:end
pause