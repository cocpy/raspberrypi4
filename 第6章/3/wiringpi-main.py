# static int setDSclock (void)
# {
#   # struct tm t ;
#   struct tm* t = NULL;
#   time_t now ;
#   int clock [8] ;
#
#   printf ("Setting the clock in the DS1302 from Linux time... ") ;
#
#   now = time (NULL) ; # 获取系统时间
#   # gmtime_r (&now, &t) ;转换成本地时间
#   t = localtime(&now)
#
#   clock [ 0] = dToBcd (t.tm_sec) ;	// seconds
#   clock [ 1] = dToBcd (t.tm_min) ;	// mins
#   clock [ 2] = dToBcd (t.tm_hour) ;	// hours
#   clock [ 3] = dToBcd (t.tm_mday) ;	// date
#   clock [ 4] = dToBcd (t.tm_mon + 1) ;	// months 0-11 --> 1-12
#   clock [ 5] = dToBcd (t.tm_wday + 1) ;	// weekdays (sun 0)
#   clock [ 6] = dToBcd (t.tm_year - 100) ;       // years
#   clock [ 7] = 0 ;			// W-Protect off
#
#   ds1302clockWrite (clock) ;
#
#   printf ("OK\n") ;
#
#   return 0 ;
# }
#
# int main(int argc, char * argv[])
# {
#     int i;
#     int clock[8];
#
#     wiringPiSetup();
#     # ds1302setup(int clockPin, int dataPin, int csPin)
#     # 设置树莓派GPIO引脚
#     ds1302setup(14, 30, 10);
#
#     if (argc == 2)
#     {
#       / ** / if (strcmp(argv[1], "-slc") == 0)
#         # 设置系统的时间
#         return setLinuxClock();
#       else if (strcmp(argv[1], "-sdsc") == 0)
#         # 根据系统时间设置DS模块的时间
#         return setDSclock();
#       else if (strcmp (argv[1], "-rtest") == 0)
#         # 对DS模块的RAM进行测试
#         return ramTest();
#       else
#       {
#         printf("Usage: ds1302 [-slc | -sdsc | -rtest]\n");
#         return EXIT_FAILURE;
#       }
#     }
#
#     for (i = 0;; ++i)
#     {
#       printf("%5d:  ", i) ;
#       # 从DS模块读出时间
#       ds1302clockRead (clock);
#       printf (" %2d:%02d:%02d",
#           bcdToD(clock[2], masks[2]), bcdToD(clock[1], masks[1]), bcdToD(clock[0], masks[0]));
#
#       printf(" %2d/%02d/%04d",
#           bcdToD(clock[3], masks[3]), bcdToD(clock[4], masks[4]), bcdToD(clock[6], masks[6]) + 2000);
#
#       printf("\n");
#
#       delay(200);
#     }
#
#     return 0;
# }