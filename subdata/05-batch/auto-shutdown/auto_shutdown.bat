echo off
::���ùػ�ʱ��
set sd_time=20:30

echo ϵͳ���� %sd_time% �Զ��ػ�

set cur_time=%TIME: =0%
set cur_time=%cur_time:~0,5%
echo ��ǰʱ���� %cur_time%

::100%sd_time:~0,2%%%100 ȡ2λ����
set sd_hh=100%sd_time:~0,2%%%100
set sd_mm=100%sd_time:~3,2%%%100
::echo sd_hh is %sd_hh% , sd_mm is %sd_mm%

set cur_hh=100%cur_time:~0,2%%%100
set cur_mm=100%cur_time:~3,2%%%100
::echo cur_hh is %cur_hh% , cur_mm is %cur_mm%

::CD = ����ʱ
set /a cd_time_hh=(%sd_hh%)-(%cur_hh%)
set /a cd_time_mm=(%sd_mm%)-(%cur_mm%)
::echo cd_time_hh is %cd_time_hh%, cd_time_mm is %cd_time_mm%
:: EQU - ���� ; NEQ - ������ ; LSS - С�� ; LEQ - С�ڻ���� ; GTR - ���� ; GEQ - ���ڻ����
:: ��������ڱ���������ִ�У�����ᱨ��
echo Сʱ����%cd_time_hh%�����ӵ���%cd_time_mm%
if %cd_time_hh% GTR 0 (
    ::Сʱ����0
	echo Сʱ����0
    goto after
) else if  %cd_time_hh% EQU 0 (
    ::Сʱ����0�����Ҫ�жϷ��ӣ�������Ӵ��ڻ����0��������ӵ��������������С��0����ôֻ�ܵ�����
	if %cd_time_mm% GEQ 0 (
		echo Сʱ����0�����Ӵ��ڵ���0
	    goto after
	) else (
	    echo Сʱ����0������С��0
	    goto before
	)
) else (
    ::ʱ��С��0��Ҳ�����Ѿ����ˣ��õ�������
	echo СʱС��0
	goto before
)
::�����жϣ��ܽ�����������һ�����Ѿ���ȥ�ˣ������죬һ���ǽ��������
::Сʱ����0,ʣ����������:(ʣ��Сʱ*60��*60��)+(ʣ�����*60��)
:after
::֮��ʱ�����0
    echo ==== ʱ��δ��������ִ�� ====
	set /a hh_to_ss=(%cd_time_hh%*60*60)
    ::echo cd_time_mm=%cd_time_mm%
    set /a mm_to_ss=%cd_time_mm%*60
	::echo mm_to_ss=%mm_to_ss%
	::echo hh_to_ss=%hh_to_ss%��mm_to_ss=%mm_to_ss%
    set /a cd_time_ss=%hh_to_ss%+%mm_to_ss%
    goto shutdown
	
:before
::֮ǰ��С��0����ô�����죬����+24Сʱ
    echo ==== ʱ���ѹ�������ִ�� ====
	set /a hh_to_ss=(24+%cd_time_hh%)*60*60
    ::echo cd_time_mm=%cd_time_mm%
    set /a mm_to_ss=%cd_time_mm%*60
	::echo mm_to_ss=%mm_to_ss%
	::echo hh_to_ss=%hh_to_ss%��mm_to_ss=%mm_to_ss%
    set /a cd_time_ss=%hh_to_ss%+%mm_to_ss%
    goto shutdown
:shutdown
    echo ����ػ�ʣ��:%cd_time_ss% ��
	shutdown -a
	shutdown -s -t %cd_time_ss%

::pause
set /p "input=Ҫȡ���ػ�������Y,�س�ȷ��:"
if "%input%" == "" (
::����Ϊ��
    echo ����Ϊ��
	goto continue_shutdown
)

::ȥ������Ŀո�
set "input=%input: =%"

::�Ѿ�ȥ���ո���Ҫ�ٴ��жϿո�
if "%input%" == "" (
::����Ϊ��
    echo ����Ϊ��
	goto continue_shutdown
)
if %input% EQU Y (
	goto cancel_shutdown
) else if %input% EQU y (
	goto cancel_shutdown
) else (
    echo �����ַ�
	goto continue_shutdown
)

:cancel_shutdown
    shutdown -a
	echo �ػ�������ȡ��
	goto end

:continue_shutdown
    echo �ػ���������ִ��
	goto end
	
	
:end
pause