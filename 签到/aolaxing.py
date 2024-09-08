import time

import requests


def user(headers):
    url = "http://service.100bt.com/creditmall/my/user_info.jsonp"
    user_json = requests.get(url, headers=headers).json()
    user_data = user_json["jsonResult"]["data"]
    try:
        credit = user_data["credit"]
        creditHistory = user_data["creditHistory"]
        phoneNum = user_data["phoneNum"]
        signInTotal = user_data["signInTotal"]
    except Exception as e:
        return [{"name": "签到", "value": str(e)}]
    msgs = [
        {"name": "用户", "value": phoneNum},
        {"name": "当前积分", "value": credit},
        {"name": "总共获得积分", "value": creditHistory},
        {"name": "总签到", "value": signInTotal},
    ]
    return msgs


def practise(headers, task_id):
    url = f"http://service.100bt.com/creditmall/activity/do_task.jsonp?taskId={task_id}&gameId=2&_=1643440166690"
    task_json = requests.get(url, headers=headers).json()
    try:
        message = task_json["jsonResult"]["message"]
    except:
        message = "NO"
    return message


def task(headers, msg: bool = False):
    url = "http://service.100bt.com/creditmall/activity/daily_task_list.jsonp?gameId=2&_=1643437206026"
    task_json = requests.get(url, headers=headers).json()
    task_data = task_json["jsonResult"]["data"]
    task_finish_count = 0
    for task_item in task_data:
        name = task_item["name"]
        status_desc = task_item["status_desc"]
        task_id = task_item["taskID"]
        if msg:
            if status_desc == "已完成":
                task_finish_count += 1
        else:
            if status_desc == "未完成":
                print(f"开始任务：{name}")
                res = practise(task_id=task_id, headers=headers)
                print(f"返回状态：{res}")
                time.sleep(2.5)
    msgs = [
        {"name": "今日任务总数", "value": len(task_data)},
        {"name": "今日任务完成数", "value": task_finish_count},
    ]
    return msgs


cookie = 'ywzc_UUID=383e98c1-6028-4374-c93a-6bf9c390a390; can_use_cookie_test=test; ywzc_new_UUID=0fad1eb7-e79c-4f6c-e008-5e9ffcaf000f; Hm_lvt_7fc3681c21a26a2022ae0ca72e2d6fa5=1723770116,1725261278; Hm_lpvt_7fc3681c21a26a2022ae0ca72e2d6fa5=1725261278; HMACCOUNT=F3465F57354F235E; BT_AUTO_tt_common=8af17776-a4cf-4155-a9af-98d0bad73504; BT_LOGIN_tt_common=16059818:185****9251'

headers = {
    "Host": "service.100bt.com",
    "Proxy-Connection": "keep-alive",
    "Accept": "*/*",
    "Referer": "http://www.100bt.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": cookie,
}
_ = task(headers)
task_msgs = task(headers=headers, msg=True)
user_msgs = user(headers=headers)
msgs = task_msgs + user_msgs
msg = "\n".join([f"{one.get('name')}: {one.get('value')}" for one in msgs])
print(msg)
