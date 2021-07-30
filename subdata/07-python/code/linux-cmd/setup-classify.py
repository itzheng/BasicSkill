#将命令分类

# 将命令与本地的已下载的命令文件进行超链接引用，并生成classfy-cmds.md文件
import requests
import json

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
               'Referer':'https://wangchujiang.com/linux-command/hot.html',
                'sec-ch-ua':'"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"'
                }

# 获取所有的命令列表
def getAllCmd():
    url = 'https://wangchujiang.com/linux-command/js/dt.js?v=1626403178815'
    #Referer: https://wangchujiang.com/linux-command/hot.html
    #sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"
    #sec-ch-ua-mobile: ?0
    print (headers)
    r = requests.get(url,headers=headers)
    print('code : ',r.status_code)
    text = r.text
    print ('text len : ',len(text))
    #得到js文件 var linux_commands=[{"n":"a......"}]
    index = text.index('[')
    json_text = text[index:len(text)]
    #print(json_text)
    linux_commands = json.loads(json_text)
    #  "n": "ed", "p": "/ed", "d": "单行纯文本编辑器"
    print ('linux_commands len ',len(linux_commands))
    return linux_commands

# 将网络获取的列表转成 本地的集合
def get_all_cmd_list():
     linux_commands = getAllCmd()
     list = []          ## 空列表
     for cmd in linux_commands:
          list.append(cmd['n'])
     return list

all_cmd_list = get_all_cmd_list()
#print(cmd_list)

def link_to(name,texts):
     fo = open('classify-cmds.md', "a+",encoding="utf-8")
     fo.write('## {0}'.format(name))
     fo.write('\n')
     cmds = texts.split('、')
     print(len(cmds))
     new_texts = ''
     for cmd in cmds:
          text = ''
          if cmd in all_cmd_list:
               text = '[{0}](hot-cmds//{0}.md)'.format(cmd)
          else:
               text = cmd
          if len(new_texts) > 0:
               new_texts = new_texts + '、'
          new_texts = new_texts + text
     #print(new_texts)
     fo.write(new_texts)
     fo.write('\n')
     #保存数据
     fo.flush()
     fo.close()
          

'''
文件传输
bye、ftp、ftpcount、ftpshut、ftpwho、ncftp、tftp、uucico、uucp、uupick、uuto、scp
'''
link_to('文件传输','bye、ftp、ftpcount、ftpshut、ftpwho、ncftp、tftp、uucico、uucp、uupick、uuto、scp')

'''
备份压缩
ar、bunzip2、bzip2、bzip2recover、compress、cpio、dump、gunzip、gzexe、gzip、lha、restore、tar、unarj、unzip、zip、zipinfo
'''
link_to('备份压缩','ar、bunzip2、bzip2、bzip2recover、compress、cpio、dump、gunzip、gzexe、gzip、lha、restore、tar、unarj、unzip、zip、zipinfo')
'''
文件管理
diff、diffstat、file、find、git、gitview、ln、locate、lsattr、mattrib、mc、mcopy、mdel、mdir、mktemp、mmove、mread、mren、mshowfat、mtools、mtoolstest、mv、od、paste、patch、rcp、rhmask、rm、slocate、split、tee、tmpwatch、touch、umask、whereis、which、cat、chattr、chgrp、chmod、chown、cksum、cmp、cp、cut、indent
'''
link_to('文件管理','diff、diffstat、file、find、git、gitview、ln、locate、lsattr、mattrib、mc、mcopy、mdel、mdir、mktemp、mmove、mread、mren、mshowfat、mtools、mtoolstest、mv、od、paste、patch、rcp、rhmask、rm、slocate、split、tee、tmpwatch、touch、umask、whereis、which、cat、chattr、chgrp、chmod、chown、cksum、cmp、cp、cut、indent')
'''
磁盘维护
badblocks、cfdisk、dd、e2fsck、ext2ed、fdisk、fsck.ext2、fsck、fsck.minix、fsconf、hdparm、losetup、mbadblocks、mformat、mkbootdisk、mkdosfs、mke2fs、mkfs.ext2、mkfs、mkfs.minix、mkfs.msdos、mkinitrd、mkisofs、mkswap、mpartition、sfdisk、swapoff、swapon、symlinks、sync
'''
link_to('磁盘维护','badblocks、cfdisk、dd、e2fsck、ext2ed、fdisk、fsck.ext2、fsck、fsck.minix、fsconf、hdparm、losetup、mbadblocks、mformat、mkbootdisk、mkdosfs、mke2fs、mkfs.ext2、mkfs、mkfs.minix、mkfs.msdos、mkinitrd、mkisofs、mkswap、mpartition、sfdisk、swapoff、swapon、symlinks、sync')
'''
系统设置
alias、apmd、aumix、bind、chkconfig、chroot、clock、crontab、declare、depmod、dircolors、dmesg、enable、eval、export、fbset、grpconv、grpunconv、hwclock、insmod、kbdconfig、lilo、liloconfig、lsmod、minfo、mkkickstart、modinfo、modprobe、mouseconfig、ntsysv、passwd、pwconv、pwunconv、rdate、resize、rmmod、rpm、set、setconsole、setenv、setup、sndconfig、SVGAText Mode、timeconfig、ulimit、unalias、unset
'''
link_to('系统设置','alias、apmd、aumix、bind、chkconfig、chroot、clock、crontab、declare、depmod、dircolors、dmesg、enable、eval、export、fbset、grpconv、grpunconv、hwclock、insmod、kbdconfig、lilo、liloconfig、lsmod、minfo、mkkickstart、modinfo、modprobe、mouseconfig、ntsysv、passwd、pwconv、pwunconv、rdate、resize、rmmod、rpm、set、setconsole、setenv、setup、sndconfig、SVGAText Mode、timeconfig、ulimit、unalias、unset')
'''
系统管理
adduser、chfn、chsh、date、exit、finger、free、fwhois、gitps、groupdel、groupmod、halt、id、kill、last、lastb、login、logname、logout、logrotate、newgrp、nice、procinfo、ps、pstree、reboot、renice、rlogin、rsh、rwho、screen、shutdown、sliplogin、su、sudo、suspend、swatch、tload、top、uname、useradd、userconf、userdel、usermod、vlock、w、who、whoami、whois
'''
link_to('系统管理','adduser、chfn、chsh、date、exit、finger、free、fwhois、gitps、groupdel、groupmod、halt、id、kill、last、lastb、login、logname、logout、logrotate、newgrp、nice、procinfo、ps、pstree、reboot、renice、rlogin、rsh、rwho、screen、shutdown、sliplogin、su、sudo、suspend、swatch、tload、top、uname、useradd、userconf、userdel、usermod、vlock、w、who、whoami、whois')
'''
文本处理
awk、col、colrm、comm、csplit、ed、egrep、ex、fgrep、fmt、fold、grep、ispell、jed、joe、join、look、mtype、pico、rgrep、sed、sort、spell、tr、uniq、vi、wc
'''
link_to('文本处理','awk、col、colrm、comm、csplit、ed、egrep、ex、fgrep、fmt、fold、grep、ispell、jed、joe、join、look、mtype、pico、rgrep、sed、sort、spell、tr、uniq、vi、wc')
'''
网络通讯
dip、getty、mingetty、ppp-off、smbd(samba daemon)、telnet、uulog、uustat、uux、cu、dnsconf、efax、httpd、ip、ifconfig、mesg、minicom、nc、netconf、netconfig、netstat、ping、pppstats、samba、setserial、shapecfg(shaper configuration)、smbd(samba daemon)、statserial(status ofserial port)、talk、tcpdump、testparm(test parameter)、traceroute、tty(teletypewriter)、uuname、wall(write all)、write、ytalk、arpwatch、apachectl、smbclient(samba client)、pppsetup
'''
link_to('网络通讯','dip、getty、mingetty、ppp-off、smbd(samba daemon)、telnet、uulog、uustat、uux、cu、dnsconf、efax、httpd、ip、ifconfig、mesg、minicom、nc、netconf、netconfig、netstat、ping、pppstats、samba、setserial、shapecfg(shaper configuration)、smbd(samba daemon)、statserial(status ofserial port)、talk、tcpdump、testparm(test parameter)、traceroute、tty(teletypewriter)、uuname、wall(write all)、write、ytalk、arpwatch、apachectl、smbclient(samba client)、pppsetup')
'''
设备管理
dumpkeys、loadkeys、MAKEDEV、rdev、setleds
'''
link_to('设备管理','dumpkeys、loadkeys、MAKEDEV、rdev、setleds')
'''
电子邮件与新闻组
archive、ctlinnd、elm、getlist、inncheck、mail、mailconf、mailq、messages、metamail、mutt、nntpget、pine、slrn、X WINDOWS SYSTEM、reconfig、startx(start X Window)、Xconfigurator、XF86Setup、xlsatoms、xlsclients、xlsfonts
'''
link_to('电子邮件与新闻组','archive、ctlinnd、elm、getlist、inncheck、mail、mailconf、mailq、messages、metamail、mutt、nntpget、pine、slrn、X WINDOWS SYSTEM、reconfig、startx(start X Window)、Xconfigurator、XF86Setup、xlsatoms、xlsclients、xlsfonts')
'''
其他命令
yes
'''
link_to('其他命令','yes')



