@echo off
@title bat 交互执行git命令：提交代码

D:
cd D:\workspace\learning\learning-dome-code
git add .
git commit -m "update code commit by system at %date:~0,4%-%date:~5,2%-%date:~8,2% %time%"
git push