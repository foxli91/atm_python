import os
# 这个是修改文件的一个demo
with open('C:\\Users\\Administrator.SC-201712251822\\Desktop\\大气资料\\T_AIR_SITE_HOUR_METEOROLOGY.sql', mode='rt',
          encoding='utf-8') as f, \
        open('C:\\Users\\Administrator.SC-201712251822\\Desktop\\大气资料\\T_AIR_SITE_HOUR_METEOROLOGY_BAK.sql', mode='wt',
             encoding='utf-8') as f2:
    c = 0
    for line in f:
        c += 1
        f2.write(line.replace('\"DB_GSODS_AREV_BASE\".', ''))
    f2.flush()
