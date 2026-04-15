@echo off
:: SPDX-License-Identifier: 0BSD
:: Run the interactive mode
setlocal

py -3 "%~dp0mkpw" -i
pause
