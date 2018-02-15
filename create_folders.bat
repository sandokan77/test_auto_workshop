echo off
set DRIVE=C:
%DRIVE%
cd \
mkdir dev
cd dev
mkdir install
mkdir projects
cd projects
mkdir python
mkdir selenium
cd ..
mkdir util
cd util
mkdir python344
mkdir scripts
mkdir selenium_drivers
net use t: \\vboxsvr\transfer /PERSISTENT:YES