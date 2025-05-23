#! /usr/bin/python3



import os

cmd1 = "cat /proc/cpuinfo"
cmd2 = "cat /proc/meminfo"

print(os.system(cmd1))
print(os.system(cmd2))
