import requests

def line(LINE_NOTIFY_TOKEN, message:str):
   
   LINE_NOTIFY_API = 'https://notify-api.line.me/api/notify'
   headers = {'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}'}
   data = {'message': f'{message}'}
   requests.post(LINE_NOTIFY_API, headers=headers, data=data)
   
   return "通知成功！"