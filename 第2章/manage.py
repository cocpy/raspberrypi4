import os


# 以字符串形式返回CPU温度
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return (res.replace("temp=", "").replace("'C\n", ""))


# 以列表的形式返回RAM信息（单位=kb）
# Index 0: total RAM
# Index 1: used RAM
# Index 2: free RAM
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return (line.split()[1:4])


# 返回占用CPU百分比的字符串
def getCPUuse():
    return (str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))


# 以列表形式返回有关磁盘空间的信息
# Index 0: total disk space
# Index 1: used disk space
# Index 2: remaining disk space
# Index 4: percentage of disk used
def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return (line.split()[1:5])


# CPU信息
CPU_temp = getCPUtemperature()
CPU_usage = getCPUuse()

# 内存信息
# 输出使用的是kb，转换为Mb
RAM_stats = getRAMinfo()
RAM_total = round(int(RAM_stats[0]) / 1000, 1)
RAM_used = round(int(RAM_stats[1]) / 1000, 1)
RAM_free = round(int(RAM_stats[2]) / 1000, 1)

# 硬盘信息
DISK_stats = getDiskSpace()
DISK_total = DISK_stats[0]
DISK_used = DISK_stats[1]
DISK_perc = DISK_stats[3]

if __name__ == '__main__':
    print('')
    print('CPU Temperature = ' + CPU_temp)
    print('CPU Use = ' + CPU_usage)
    print('')
    print('RAM Total = ' + str(RAM_total) + ' MB')
    print('RAM Used = ' + str(RAM_used) + ' MB')
    print('RAM Free = ' + str(RAM_free) + ' MB')
    print('')
    print('DISK Total Space = ' + str(DISK_total) + 'B')
    print('DISK Used Space = ' + str(DISK_used) + 'B')
    print('DISK Used Percentage = ' + str(DISK_perc))
