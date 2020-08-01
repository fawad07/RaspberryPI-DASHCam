#!/bin/bash

dir="/home/pi/Videos"	#/sharpTest.py";
remoteDevice="fawad@10.0.0.198:";
remoteDir="/home/fawad/Videos/DashCam_Arch";
if [ -d "$dir" ];	#! sign issue
then
	#TO-DO check if dir exists!! if not mkdir
	scp -r $dir $remoteDevice$remoteDir;
	echo "Command Execution Complete";
else
	echo "Error: $dir does not exist ";
fi
