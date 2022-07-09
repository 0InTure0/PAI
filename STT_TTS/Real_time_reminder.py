from time import localtime, time
strmsg = " "+"7시간 50분 뒤에 알람 맞춰줘"
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
  time_count = 5
  msg_time = 0
  a = 0
  #빅스비 = 시간이라는 말이 있거나 분만 있을 경우 몇 time 뒤로 인식

  for idx, val in enumerate(time_set_list):
    if not(val == -1):
      list_to_str = "".join(list_msg[val-2:val])
      if(idx == 3 and list_msg[val+1] == "간"):
        int_msg = int(list_to_str)
        int1 = (tm.tm_hour+int_msg)*(10**(2*time_count))
        if(int1 >= 240000):
          int1 = int1 + 760000
        msg_time = msg_time + int1
      elif(idx == 3 and tm.tm_hour > 12):
        int_msg = int(list_to_str)
        int1 = (int_msg+12)*(10**(2*time_count))
        msg_time = msg_time + int1
      elif(idx == 2 and "내일" in strmsg):
        msg_time = msg_time + (tm.tm_mday*1000000)
      elif(idx == 4 and "뒤" in list_msg[min_find:min_find+5]):
        int_msg = int(list_to_str)
        int1 = (tm.tm_min+int_msg)*(10**(2*time_count))
        if(int1 >= 6000):
          int1 = int1 +4000
        msg_time = msg_time + int1


      else:
        int_msg = int(list_to_str)
        int1 = int_msg*(10**(2*time_count))
        msg_time = msg_time + int1
      msg_start = val
    else:
      if not(a == 5):
        int1 = real_time_list[a]*(10**(2*time_count))
        msg_time = msg_time + int1
    a = a+1
    time_count = time_count-1
  real_time_count = 5
  real_time_int = 0
  #리얼타임 하나의 수열로 변환
  for i in real_time_list:
    int2 = i*(10**(2*real_time_count))
    real_time_int = real_time_int + int2
    real_time_count = real_time_count-1
  print(real_time_int)
  if("내일" in strmsg):
    msg_time = msg_time + 1000000
  elif("모레" in strmsg):
    msg_time = msg_time + 2000000
  elif("글피" in strmsg):
    msg_time = msg_time + 3000000
  elif("그글피" in strmsg):
    msg_time = msg_time + 4000000
  if("뒤" in strmsg):
    if("하루" in strmsg):
      msg_time = msg_time + 1000000
    if("이틀" in strmsg):
      msg_time = msg_time + 2000000
    if("사흘" in strmsg):
      msg_time = msg_time + 3000000
    if("나흘" in strmsg):
      msg_time = msg_time + 4000000
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
  print(msg_time)
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
