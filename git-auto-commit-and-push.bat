@echo off
@title bat 交互执行git命令

D:
cd D:\workspace\learning\note
git add .
git commit -m "update note commit by system at %date:~0,4%-%date:~5,2%-%date:~8,2% %time%"
git push