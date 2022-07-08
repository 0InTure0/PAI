from time import localtime, time
strmsg = "리마인더 2022년 10시 10분에 저녁밥 해먹기"

tm = localtime(time())

print(tm.tm_year,"년",tm.tm_mon,"월",tm.tm_mday,"일",tm.tm_hour,"시",tm.tm_min,"분",tm.tm_sec,"초")

year_find = strmsg.find("년")
mon_find = strmsg.find("월")
day_find = strmsg.find("일")
hour_find = strmsg.find("시")
min_find = strmsg.find("분")
sec_find = strmsg.find("초")
real_time_list = [tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec]
time_set_list = [year_find, mon_find, day_find, hour_find, min_find, sec_find]
list_msg = list(strmsg)

reminder_time_list = []

for j in time_set_list:
    if not(j == -1):
        if (j == year_find):
            list_to_str = "".join(list_msg[j-4:j])
        else:
            list_to_str = "".join(list_msg[j-2:j])
        int_msg = int(list_to_str)
        reminder_time_list.append(int_msg)
    else:
        reminder_time_list.append(0)
print(real_time_list)
print(reminder_time_list)




#오후라는 말이 있으면 시간이 12시 이하일 때 알람 시간 플러스 12시간 오전은 그대로
#문자열에서 년, 월, 일, 시, 분, 초를 인식해서 그 문자열의 2단계 전까지 인식
