# 这里用来记录 Git 常用的一些小技巧<br>想要完整的学习请找其他教程。

## 一、设置项目提交的用户名和邮箱,[知乎](https://zhuanlan.zhihu.com/p/345915480)

1. 找到要提交的项目里面的 .git/config 文件
2. 添加如下语句,如果已经有[user],直接修改 name 和 email
~~~base
[user]
	name = itzheng
	email = itzheng@zoho.com
~~~

## 二、Git 对文件大小写不敏感问题
文件或文件夹改名，只是改了大小写，git add . 文件大小写没有改成功
解决方式有2:[csdn](https://blog.csdn.net/u012814856/article/details/99940160)
1. 备份文件夹，然后删除原来的文件夹，git add . 然后在将备份的文件夹放回去
2. 在 git 命令行中重命名

## 三、覆盖上次提交
使用 Git Gui , 在菜单栏的 Commit 中找到 amend last commit ,打勾就行

## 四、强制提交本地数据
有时候会造成本地版本与远程的不一致，在 push 会提示错误
可以使用 --force 强制推送
~~~bash
git push --force origin main
~~~