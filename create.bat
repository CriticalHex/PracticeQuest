@echo off
set formatted_input=%*
mkdir %formatted_input%
set top_dir=%CD%
cd %formatted_input%
copy "%top_dir%\template.py" "%formatted_input%.py" >nul
nul> input.txt
cd %top_dir%
call code %formatted_input%\%formatted_input%.py
call code %formatted_input%\input.txt