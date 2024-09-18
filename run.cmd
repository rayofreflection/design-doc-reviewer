REM Activating Python environment
@REM Scripts\activate

REM Installing all the dependencies
pip install -r requirements.txt

REM Getting current date and time
set currentDate=%date%
set currentTime=%time%

rem Optionally format the date and time with underscores
set formattedDate=%currentDate:~0,2%_%currentDate:~3,2%_%currentDate:~6,4%
set formattedTime=%currentTime:~0,2%_%currentTime:~3,2%_%currentTime:~6,2%

REM Run test file
python test\test.py cmake_source\cmake-example\apps\app1.cc > logs\output_logs_%formattedDate%_%formattedTime%.txt