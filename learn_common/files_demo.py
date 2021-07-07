import os
import time

start = time.time()
# 这个是修改文件的一个demo
with open('C:\\Users\\Administrator.SC-201712251822\\Desktop\\大气资料\\T_AIR_SITE_MICRO_HOUR_QUALITY.sql', mode='rt',
          encoding='utf-8') as f, \
        open('C:\\Users\\Administrator.SC-201712251822\\Desktop\\大气资料\\T_AIR_SITE_MICRO_HOUR_QUALITY_BAK1.sql', mode='wt',
             encoding='utf-8') as f1, open(
    'C:\\Users\\Administrator.SC-201712251822\\Desktop\\大气资料\\T_AIR_SITE_MICRO_HOUR_QUALITY_BAK2.sql', mode='wt',
    encoding='utf-8') as f2, open(
    'C:\\Users\\Administrator.SC-201712251822\\Desktop\\大气资料\\T_AIR_SITE_MICRO_HOUR_QUALITY_BAK3.sql', mode='wt',
    encoding='utf-8') as f3, open(
    'C:\\Users\\Administrator.SC-201712251822\\Desktop\\大气资料\\T_AIR_SITE_MICRO_HOUR_QUALITY_BAK4.sql', mode='wt',
    encoding='utf-8') as f4, open(
    'C:\\Users\\Administrator.SC-201712251822\\Desktop\\大气资料\\T_AIR_SITE_MICRO_HOUR_QUALITY_BAK5.sql', mode='wt',
    encoding='utf-8') as f5:
    c = 0
    for line in f:

        if c <= 192439:
            f1.write(line.replace('\"DB_GSODS_AREV_BASE\".', ''))
        elif c <= 292439:
            f2.write(line.replace('\"DB_GSODS_AREV_BASE\".', ''))
        elif c <= 692439:
            f3.write(line.replace('\"DB_GSODS_AREV_BASE\".', ''))
        elif c <= 992439:
            f4.write(line.replace('\"DB_GSODS_AREV_BASE\".', ''))
        else:
            f5.write(line.replace('\"DB_GSODS_AREV_BASE\".', ''))
        c += 1
    f1.flush()
    f2.flush()
    f3.flush()
    f4.flush()
    f5.flush()
end = time.time()
print(end - start)
