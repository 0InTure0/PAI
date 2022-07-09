from time import localtime, time
strmsg = "리마인더 7월 20일 11시 30분에 알람 맞춰줘"
reminder_dic = {999999999999999: 999999999999999}
tm = localtime(time())
#print(tm.tm_year,"년",tm.tm_mon,"월",tm.tm_mday,"일",tm.tm_hour,"시",tm.tm_min,"분",tm.tm_sec,"초")
def string_to_time(strmsg, list_msg):
  year_find = strmsg.find("년")
  mon_find = strmsg.find("월")
  day_find = strmsg.find("일")
  hour_find = strmsg.find("시")
  min_find = strmsg.find("분")
  sec_find = strmsg.find("초")
  real_time_list = [tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec]
  time_set_list = [year_find, mon_find, day_find, hour_find, min_find, sec_find]
  reminder_time_list = []
  time_count = 5
  msg_time = 0
  a = 0
  for j in time_set_list:
    if not(j == -1):
      if (j == year_find):
        list_to_str = "".join(list_msg[j-4:j])
      else:
        list_to_str = "".join(list_msg[j-2:j])
      int_msg = int(list_to_str)
      #reminder_time_list.append(int_msg)
      int1 = int_msg*(10**(2*time_count))
      msg_time = msg_time + int1
      msg_start = j
    else:
      reminder_time_list.append(0)
      if not(a == 5):
        int1 = real_time_list[a]*(10**(2*time_count))
        msg_time = msg_time + int1
      else:
        pass
    a = a+1
    time_count = time_count-1
  real_time_count = 5
  real_time_int = 0
  for i in real_time_list:
    int2 = i*(10**(2*real_time_count))
    real_time_int = real_time_int + int2
    real_time_count = real_time_count-1
  return msg_time, real_time_int, msg_start

def reminder_save(strmsg):
  list_msg = list(strmsg)
  msg_time, real_time_int, msg_start = string_to_time(strmsg, list_msg)
  if(list_msg[msg_start+1] == "에"):
    msg_start = msg_start+1
  if(list_msg[msg_start+1] == " " or list_msg[msg_start+2] == " "):
    msg_start = msg_start+1
  remind_msg = "".join(list_msg[msg_start+1:])
  if ("알람" in remind_msg):
    reminder_dic[msg_time] = "알람"
  else:
    reminder_dic[msg_time] = remind_msg
  return real_time_int

def reminder_play():
  real_time_list = [tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec]
  real_time_count = 5
  real_time_int = 0
  for i in real_time_list:
    int2 = i*(10**(2*real_time_count))
    real_time_int = real_time_int + int2
    real_time_count = real_time_count-1 
  for k in reminder_dic.keys():
    if(real_time_count >= k):
      if(reminder_dic[k] == "알람"):
        print("알람소리 띠리링띠리링")
      else:
        print("리마인더 알림입니다. ", end='')
        print(reminder_dic[k])


reminder_save(strmsg)
reminder_play()
